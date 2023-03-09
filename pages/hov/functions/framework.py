import pandas as pd
import numpy as np
import itertools
from scipy.stats import obrientransform, f_oneway, levene, normaltest, describe
import rpy2.robjects.packages as rpackages
from rpy2.robjects import r, pandas2ri

utils = rpackages.importr('utils')
expdes = rpackages.importr('ExpDes')



def samiuddinTest(df, groupVar, numVar, alpha):

    # convert pandas DataFrame to R data frame
    data_sub = pd.DataFrame(df[[groupVar, numVar]])
    pandas2ri.activate()
    
    # get replications
    reps = str(tuple(df.groupby(groupVar).count()[numVar]))
    

    # Conduct the Samiuddin test
    result = expdes.samiuddin(
      trat = data_sub[groupVar],
      resp = data_sub[numVar],
      t = 3,
      r = robjects.IntVector(r(f'c{reps}'))
    )


    # Get the p-value
    p = result[0]
    
    if p > alpha:
        return 'HEV'
    
    else:
        return 'HOV'
    



def find_closest(lst, target):
    """
    Finds the closest number in a list of numbers greater or equal to the current number.
    """
    lst.sort()
    for num in lst:
        if num >= target:
            return num
    
    return None




def fMaxTest(df, groupVar, numVar, alpha):
    
    # get the table
    if alpha == 0.01:
        table = pd.read_csv('../fmaxTables/fmax_1.csv')
        
    elif alpha == 0.05:
        table = pd.read_csv('../fmaxTables/fmax_5.csv')
    
    else:
        raise ValueError("Choose .01 or .05 for alpha value")
    
    # compute the variance of each group
    group_variances = df.groupby(groupVar)[numVar].var()
    
    # Divide the largest variance by the smallest variance
    maxVar = group_variances.max()
    minVar = group_variances.min()
    ratio = maxVar / minVar
    
    # find number of groups and degrees of freedom
    groupCount = len(group_variances)
    degFree = len(df) - 1
    
    # find table value for comparison
    numList = table['DF'].unique()
    tableDeg = find_closest(numList, degFree)
    tableCol = str(groupCount)
    tableVal = float(table[(table['DF'] == tableDeg)][tableCol])
    
    if ratio <= tableVal:
        return 'HOV'
    else:
        return 'HEV'
    


def getGroups(df, groupVar, numVar):
    
    groups = df[groupVar].unique()
    n_groups = len(groups)
    
    groupList = []
    for i in range(n_groups):
        groupList.append(df[df[groupVar] == groups[i]][numVar])
        
    return groupList




def brownForsytheTest(df, groupVar, numVar, alpha):
    
    groupList = getGroups(df, groupVar, numVar)
    
    stat, p = levene(*groupList, center='median')
    
    if p < alpha:
        return 'HEV'
    else:
        return 'HOV'
    

def leveneTest(df, groupVar, numVar, alpha):
    
    groupList = getGroups(df, groupVar, numVar)
    
    stat, p = levene(*groupList, center='mean')
    
    if p < alpha:
        return 'HEV'
    else:
        return 'HOV'



def obrienTest(df, groupVar, numVar, alpha):
    
    groupList = getGroups(df, groupVar, numVar)
    transGroups = obrientransform(*groupList)
    F, p = f_oneway(*transGroups)
    
    if p < alpha:
        return 'HEV'
    else:
        return 'HOV'
    

def distributionTest(df, targetCol, alpha):
    
    # intialize 
    dist = {}
    data = df[targetCol]
    
    # perform normality test
    stat, pval = normaltest(data)
    
    # get skewness and kurtosis
    skewness = describe(data).skewness
    kurtosis = describe(data).kurtosis
    
    # determine if normal
    if pval < alpha:
        dist['normality'] = False
    else:
        dist['normality'] = True
        
        
    # determine level of skew    
    if abs(skewness) <= .5:
        dist['skew'] = 'none'
    elif abs(skewness) <= 1 and abs(skewness) > .5:
        dist['skew'] = 'moderate'
    else:
        dist['skew'] = 'high'
        
        
    # determine level of kurtosis
    if kurtosis > 3:
        dist['kurtosis'] = 'leptokurtic'
    elif kurtosis < 3:
        dist['kurtosis'] = 'platykurtic'
    else:
        dist['kurtosis'] = 'mesokurtic'
        
        
    return dist


def sampleSize(df):
    '''Determine if the sample size is small or large'''
    if len(df) >= 30:
        return 'large'
    
    else:
        return 'small'
    


def chooseHOVTest(df, groupVar, numVar, alphaDist, alphaHOV):
    
    
    # intialize conditions
    size = sampleSize(df)
    distDict = distributionTest(df, numVar, alphaDist)
    distDict['size'] = size
    
    
    # get distribution values
    skew = distDict['skew']
    kurtosis = distDict['kurtosis']
    normality = distDict['normality']
    
    # HOV results intialize
    power = None
    powerName = ''
    robust = None
    robustName = ''
    PnR = None
    PnRName = ''
    
    
    # get data
        
    # choose best test (robust, power, both)
    if size == 'small':
        
        if kurtosis == 'leptokurtic' and skew == 'none': 
            
            # apply o'brien test for robustness
            robust = obrienTest(df, groupVar, numVar, alphaHOV)
            robustName = "O'Brien"
            
            # apply Hartley fmax test for power
            power = fMaxTest(df, groupVar, numVar, alphaHOV)
            powerName = "Hartley FMax"
            
            # apply Hartley fmax test for power and robustness
            PnR = power
            PnRName = "Hartley FMax"
            
            
        
        elif kurtosis == 'platykurtic' and skew == 'none':
            
            # apply Z-VAR original test for robustness
            robust = 'Working on developing code'
            robustName = 'Z-VAR Original'
            
            
            # apply Brown-Forsythe test for power
            power = brownForsytheTest(df, groupVar, numVar, alphaHOV)
            powerName = 'Brown-Forsythe'
            
            # apply Brown-Forsythe test for power and robustness
            PnR = power
            PnRName = 'Brown-Forsythe'
        
        elif skew == 'moderate' and kurtosis == 'mesokurtic':
            
            # apply Brown-Forsythe for robustness
            robust = brownForsytheTest(df, groupVar, numVar, alphaHOV)
            robustName = 'Brown-Forsythe'
            
            # apply Z-VAR original for power
            power = 'Working on developing code'
            powerName = 'Z-VAR Original'
            
            # apply Samiuddin cube for power and robustness
            PnR = samiuddinTest(df, groupVar, numVar, alphaHOV)
            PnRName = 'Samiuddin Cube Root'
        
        elif skew == 'high' and kurtosis == 'mesokurtic':
            
            # apply Brown-Forsythe for robustness
            robust = brownForsytheTest(df, groupVar, numVar, alphaHOV)
            robustName = 'Brown-Forsythe'
            
            # apply Z-VAR original for power
            power = 'Working on developing code'
            powerName = 'Z-VAR Original'
            
            # apply any test for power and robustness (brownForsythe chosen)
            PnR = robust
            PnRName = 'Brown-Forsythe'
        
        elif skew=='none' and normality == True and kurtosis == 'mesokurtic':
            
            # Z-VAR original for robustness
            robust = 'Working on developing code'
            robustName = 'Z-Var Original'
            
            # apply Samiuddin cube for power
            power = samiuddinTest(df, groupVar, numVar, alphaHOV)
            powerName = 'Samiuddin Cube Root'
            
            # apply Z-VAR original for power and robustness
            PnR = robust
            PnRName = 'Z-Var Original'
            
        
        else:

            # apply Brown-Forsythe for robustness due to multiple violation
            robust = brownForsytheTest(df, groupVar, numVar, alphaHOV)
            robustName = 'Brown-Forsythe'

            # apply Z-VAR Original for power due to multiple violations
            power = 'Working on developing code'
            powerName = 'Z-Var Original'

            # apply Brown-Forsythe for power and robustness due to multiple violations
            PnR = robust
            PnRName = 'Brown-Forsythe'

            
        
    else:
        if kurtosis == 'leptokurtic' and skew == 'none': 
            
            # apply Z-VAR: Overwood test for robustness
            robust = 'Working on developing code'
            robustName = 'Z-VAR: Overwood'
            
            
            # apply Z-VAR: original or Hartley FMAX or Samiuddin cube for power
            power = fMaxTest(df, groupVar, numVar, alphaHOV)
            powerName = 'Hartley FMax'
            
            # apply Hartley FMAX and Z-VAR: Over-wood test for power and robustness
            PnR = power
            PnRName = 'Hartley FMax'
            
            
        
        elif kurtosis == 'platykurtic' and skew == 'none':
            
            # apply Z-VAR original test for robustness
            robust = 'Working on developing code'
            robustName = 'Z-VAR Original'
            
            
            # apply Z-VAR: Over-wood test for power
            power = 'Working on developing code'
            powerName = 'Z-VAR: Over-wood'
            
            
            # apply Z-VAR: Over-wood test for power and robustness
            PnR = power
            PnRName = 'Z-VAR Over-wood'
            
        
        elif skew == 'moderate' and kurtosis == 'mesokurtic':
            
            # apply Brown-Forsythe for robustness
            robust = brownForsytheTest(df, groupVar, numVar, alphaHOV)
            robustName = 'Brown-Forsythe'
            
            # apply Z-VAR original for power
            power = 'Working on developing code'
            powerName = 'Z-VAR Original'
            
            # apply Brown-Forsythe test for power and robustness
            PnR = robust
            PnRName = 'Brown-Forsythe'
        
        elif skew == 'high' and kurtosis == 'mesokurtic':
            
            # apply Brown-Forsythe for robustness
            robust = brownForsytheTest(df, groupVar, numVar, alphaHOV)
            robustName = 'Brown-Forsythe'
            
            # apply Hartley FMAX for power
            power = fMaxTest(df, groupVar, numVar, alphaHOV)
            powerName = 'Hartley FMax'
            
            # apply Hartley FMAX test for power and robustness
            PnR = power
            PnRName = 'Hartley FMax'
        
        elif skew =='none' and normality == True and kurtosis == 'mesokurtic':
            
            # Samiuddin cube for robustness
            robust = samiuddinTest(df, groupVar, numVar, alphaHOV)
            robustName = 'Samiuddin Cube Root'
            
            # apply Samiuddin cube for power
            power = samiuddinTest(df, groupVar, numVar, alphaHOV)
            powerName = 'Samiuddin Cube Root'
            
            # apply Samiuddin cube for power and robustness
            PnR = robust
            PnRName = 'Samiuddin Cube Root'
            
        else:
            # apply Brown-Forsythe for robustness due to multiple violation
            robust = brownForsytheTest(df, groupVar, numVar, alphaHOV)
            robustName = 'Brown-Forsythe'

            # apply Z-VAR Original for power due to multiple violations
            power = leveneTest(df, groupVar, numVar, alphaHOV)
            powerName = 'Levene'

            # apply Brown-Forsythe for power and robustness due to multiple violations
            PnR = power
            PnRName = 'Levene'
        
    # store results and features
    results = pd.DataFrame({'Test': [robustName, powerName, PnRName],
                         'Strength': ['robust', 'power', 'both'],
                        'Result': [robust, power, PnR]})
    
    
    
    return results, distDict