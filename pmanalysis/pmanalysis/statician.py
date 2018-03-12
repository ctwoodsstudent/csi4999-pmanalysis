import numpy as np
from scipy.stats import ttest_ind

def getTestResults(samples, cNum, eNum, pval):
    conMeans, expMeans = getDict(samples, cNum, eNum)
    tstats, pvals = runTTest(conMeans, expMeans)
    counter = 0
    for key in samples.keys():
        if pvals[counter] > pval:
            my_dict.pop(key, None)
        else:
            samples[key] = [tstats[counter], pvals[counter]]
    return samples


def getDict(samples, cNum, eNum):
    con, exp = []
    for key in samples.keys():
        cmean = 0
        for i in range(0, cNum):
           cmean += i
        con.append(cmean/cNum)
        emean = 0
        for j in range(cNum+1, cNum+eNum):
            emean += j
        exp.append(emean/eNum)
    return con, exp


def runTTest(con, exp):
    # Use scipy.stats.ttest_ind.
    tstat, pval = ttest_ind(con, exp, equal_var=False)
    return tstat, pval
