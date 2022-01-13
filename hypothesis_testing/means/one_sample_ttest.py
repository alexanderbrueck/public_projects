# 1-sample t-test

from scipy import stats
from google.colab import files
import io
import pandas as pd

# 1 - upload csv and convert to dataframe
uploaded = files.upload()
filename = list(uploaded.keys())[0]
sample = pd.read_csv(io.BytesIO(uploaded[filename]), index_col=False)

# 2 - plot distribution of sample
alt.Chart(sample).mark_bar().encode(
    alt.X("xxx", bin=True),
    y='count()',
)

# 3 - conducting t test
statistic, pvalue = stats.ttest_1samp(
    sample, 
    popmean=93, 
    axis=0, 
    nan_policy='omit', 
    )

# 4 - calculating critical value
from scipy.stats import t

dof = len(sample['Sample 1'].dropna())-1
confidence_level = 0.95  
alpha = 1 - confidence_level
critical_value = t.ppf(1-alpha/2, dof)

# 5 - Interpreting results
print('statistic: %0.5f, pvalue: %0.5f, critical_value: %0.5f' % (statistic, pvalue, critical_value))

if statistic > critical_value or statistic < critical_value *-1:
   print("Reject the null hypothesis")
else:
   print("Fail to reject the null hypothesis")  