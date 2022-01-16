# this model checks the linear relationship of then independet variable x and the dependent variable y using simple linear regression

import statsmodels.api as sm
import pandas as pd
import altair as alt

#load data 
from google.colab import files
upload = files.upload()
data = pd.read_excel(upload['reg_data.xlsx'])

x = data[['x']]
y = data[['y']]

#Plot data 
alt.Chart(data).mark_point().encode(
    x=alt.X('x', title=''),
    y=alt.Y('y', title=''),
    )

#create model
x = sm.add_constant(x)
model = sm.OLS(y, x)
results = model.fit()
print(results.summary())