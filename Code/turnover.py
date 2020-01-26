## Predicting Employee Turnover ##

# Importing the data #
import pandas as pd
fname = 'https://raw.githubusercontent.com/mcanela-iese/ML_Course/master/Data/' \
    'turnover.csv'
df = pd.read_csv(fname)
df.shape
df.head(10)
df.info()

# Summarizing numeric variables #
df.describe().round(1)

# Summarizing categorical variables #
df['Department'].value_counts()
pd.crosstab(df['Department'], df['BusinessTravel'])

# Pivot tables #
tab1 = pd.pivot_table(data=df, columns='Education', values='Wages', aggfunc='mean')
tab1.round(1)
import matplotlib.pyplot as plt
tab1.plot.bar(title='Figure 1. Barplot', figsize=(6,6), color='0.7')
plt.show()
tab2 = pd.pivot_table(data=df, index='Education', columns='Department',
    values='Wages', aggfunc='mean')
tab2.round(1)

# Correlation #
R = df[['Age', 'JobSatisfaction', 'Wages', 'PerfoRating']].corr()
R.round(2)

# Histogram #
df['Wages'].plot.hist(title='Figure 2. Histogram', figsize=(6,6), color='0.7')
plt.xlabel('Wages')
plt.show()

# Scatter plot #
df.plot.scatter(x='Age', y='Wages', title='Figure 3. Scatterplot', figsize=(6,6), color='0.7', s=1)
plt.show()
