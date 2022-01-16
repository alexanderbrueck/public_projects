# this model predicts y-values base on given x-values using simple linear regression

from sklearn import linear_model
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
reg = linear_model.LinearRegression()
reg.fit(x,y)
r_squared = reg.score(x,y)
print('intercept: %0.5f,\nregression coefficient: %0.5f,\nR squared: %0.10f' % (reg.intercept_,reg.coef_,r_squared))

# predict values
predictions = {'x': [20,10,25]}  
predictions = pd.DataFrame(predictions)  

y_head = reg.predict(predictions)
predictions['y_head'] = y_head

predictions