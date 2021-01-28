# %%
import numpy as np 
import gvar as gv  
from fit import Fit
from prior_setting import prior_ho_width_1
prior = prior_ho_width_1

file_name = 'a09m310_e_gA_srcs0-15.h5'
pt2_nstates = 5
pt3_nstates = pt2_nstates
sum_nstates = 5
sum_tau_cut = 1
include_2pt = True
include_3pt = True
include_sum = True

fitter = Fit(file_name, prior, pt2_nstates, pt3_nstates, sum_nstates, sum_tau_cut,  include_2pt, include_3pt, include_sum)

# fitter.pt2_fit_function(gA_tsep_fit, p)
# fitter.pt3_fit_function(np.array(gA_tsep_data), np.array(gV_tsep_data), np.array(gA_tau_data), np.array(gV_tau_data), p)
# summation(self, A3_t, V4_t, p)
# summation_same_can(self, A3_t, V4_t, p) for situation when pt2_nstates = sum_nstates

fit_result = gv.load("fit_result.pickle")
# %% 
########## time range of best fit: ############

## here b is not included in [a, b], same for all below

# 2pt + 3pt + sum

# 2pt_range = [3, 18], nstates=5      
# 3pt_range = [3, 15], tau_cut=1 for [2, 11], tau_cut=2 for [11, 15] 
# sum_range = [3, 14], nstates=5

# 2pt + sum

# 2pt_range = [5, 18], nstates=2
# sum_range = [5, 14]

# 2pt + 3pt

# 2pt_range = [3, 18], nstates=5
# 3pt_range = [3, 15], tau_cut=1
