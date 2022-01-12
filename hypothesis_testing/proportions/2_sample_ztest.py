#2-sample z-test for proportions

from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import norm

confidence_level = 0.95
alpha = 1 - confidence_level
critical_value = norm.ppf(1-alpha/2)

stat, p_value = proportions_ztest(
	count=(41,351),
	nobs=(195,605),
	alternative="two-sided"
	)

print('stat: %0.5f, p_value: %0.5f, critical_value: %0.5 f' % (stat, p_value, critical_value))
if stat > critical_value or stat < critical_value *-1:
	print("Reject the null hypothesis")
else:
	print("Fail to reject the null hypothesis")
