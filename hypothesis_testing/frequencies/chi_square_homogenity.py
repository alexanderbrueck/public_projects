#Chi-square test of homogenity

import numpy as np
import scipy

table = np.array([[12,108,30],
                  [24,130,46],
                  [44,132,44]])

chi2, p, dof, expected = scipy.stats.chi2_contingency(table)

critical_value = scipy.stats.chi2.ppf(0.99, df=dof)

print(f"chi2 statistic:     {chi2:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print(f"expected frequencies:\n {expected}")

if chi2 > critical_value:
   print("Reject the null hypothesis")
else:
   print("Fail to reject the null hypothesis")  