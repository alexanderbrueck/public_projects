# Chi-Square Goodness of Fit Test

import scipy

critical_value = scipy.stats.chi2.ppf(0.95, df=dof)

observed_counts = [121,288,91]
expected_counts =[100,150,250]

chi_stat, p_value =  scipy.stats.chisquare(observed_counts, expected_counts)

print('chi_stat: %0.5f, p_value: %0.5f' % (chi_stat, p_value))

if chi_stat > critical_value:
   print("Reject the null hypothesis")
else:
   print("Fail to reject the null hypothesis")  