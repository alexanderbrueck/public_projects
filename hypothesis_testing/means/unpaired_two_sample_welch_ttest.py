#Unpaired 2-sample t-test: Welch's t-test

from google.colab import files
import io
import pandas as pd

# 1 - upload csv and convert to dataframe
uploaded = files.upload()
filename = list(uploaded.keys())[0]
samples = pd.read_csv(io.BytesIO(uploaded[filename]), index_col=False)

# 2 - plot distributions of samples
def plot(df,sample):
  return alt.Chart(df).mark_bar().encode(
    alt.X(sample, bin=True),
    y='count()')

plot(samples,"Sample 1:Q") | plot(samples,"Sample 2:Q")

# 3 - create a list for each sample considering different sample sizes
sample_1 = pd.Series(samples['Sample 1']).to_list()
sample_1 = [x for x in sample_1 if pd.isnull(x) == False]

sample_2 = pd.Series(samples['Sample 2']).to_list()
sample_2 = [x for x in sample_2 if pd.isnull(x) == False]

# 4 - conducting t test
from statsmodels.stats.weightstats import ttest_ind

tstat, pvalue, dof = ttest_ind(
    x1=sample_1,
    x2=sample_2,
    alternative='two-sided', 
    usevar='unequal', 
    value=0)

# 5 - calculating critical value
from scipy.stats import t

confidence_level = 0.95  
alpha = 1 - confidence_level
critical_value = t.ppf(1-alpha/2, dof)

# 6 - Interpreting results
print('tstat: %0.5f, pvalue: %0.5f, dof: %0.5f, critical_value: %0.5f' % (tstat, pvalue, dof, critical_value))

if tstat > critical_value or tstat < critical_value *-1:
   print("Reject the null hypothesis")
else:
   print("Fail to reject the null hypothesis")  
