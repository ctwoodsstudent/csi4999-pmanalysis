import numpy as np
from scipy.stats import ttest_ind_from_stats

def getTestResults(pvals, probe_names, p_input):
    sig_probes = []
    for i in range(0, len(probe_names)):
        if float(pvals[i]) <= p_input:
            sig_probes.append(probe_names[i])
    return sig_probes

def runTTest(con_samples, exp_samples):
    con_means = []
    con_var = []
    con_n = len(con_samples[list(con_samples.keys())[0]])
    for key in con_samples:
        con_means.append(np.mean(con_samples[key]))
        con_var.append(np.var(con_samples[key]))
    con_dof = con_n - 1

    exp_means = []
    exp_var = []
    exp_n = len(exp_samples[list(exp_samples.keys())[0]])
    for key in  exp_samples:
        exp_n = len(exp_samples[key])
        exp_means.append(np.mean(exp_samples[key]))
        exp_var.append(np.var(exp_samples[key]))
    exp_dof = exp_n - 1

    tstats = [0]*(len(con_means))
    pvalues = [0]*(len(con_means))

    for i in range(0, len(con_means)):
        tstats[i], pvalues[i] = ttest_ind_from_stats(con_means[i], np.sqrt(con_var[i]), con_n, exp_means[i], np.sqrt(exp_var[i]), exp_n, equal_var=False)

    return tstats, pvalues
