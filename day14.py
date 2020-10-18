#Descriptive Statistics
import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}
df = pd.DataFrame(d)
print(df)

#sum
print(df.sum())

#mean
print(df.mean())

#axis=1
print(df.sum(1))

#count
print(df.count())

#median
print(df.median())

#mode
print(df.mode())

#min
print(df.min())

#max
print(df.max())

#prod
print(df.prod())

#std
print(df.std())

#Summarizing Data
print(df.describe())
print(df.describe(include=['object']))
print(df. describe(include='all'))

#Function Application
def adder(ele1,ele2):
   return ele1+ele2
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
print(df.apply(np.mean))

#Row or Column Wise Function Application
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean)
print(df.apply(np.mean))

#----------------------------------------------------------------------
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean,axis=1)
print(df.apply(np.mean))

#----------------------------------------------------------------------
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(lambda x: x.max() - x.min())
print(df.apply(np.mean))

#Element Wise Function Application
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df['col1'].map(lambda x:x*100)
print(df.apply(np.mean))

#----------------------------------------------------------------------
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.applymap(lambda x:x*100)
print(df.apply(np.mean))
