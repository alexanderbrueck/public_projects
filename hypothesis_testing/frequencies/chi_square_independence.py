#Chi-square test of independence

import numpy as np
import scipy

table = np.array([[176,153,11],
                  [196,20,64]])

chi2, p, dof, expected = scipy.stats.chi2_contingency(table)

critical_value = scipy.stats.chi2.ppf(0.95, df=dof)

print(f"chi2 statistic:     {chi2:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print(f"expected frequencies:\n {expected}")

if chi2 > critical_value:
   print("Reject the null hypothesis")
else:
   print("Fail to reject the null hypothesis")  