import numpy as np
from scipy.stats import ttest_ind




def Ttest(a, b):
    # Use scipy.stats.ttest_ind.
    t, p = ttest_ind(a, b, equal_var=False)
    print("ttest_ind:            t = %g  p = %g" % (t, p))
