import pandas as pd
import numpy as np

#Series
s=pd.Series()
print(s)

#Creating series from array
data=np.array(['a','b','c','d','e'])
s=pd.Series(data)
print(s)

data=np.array(['a','b','c','d','e'])
s=pd.Series(data,index=[10,11,12,13,14])
print(s)

#Creating series from dictionary
data={'a':11,'b':12,'c':13,'d':14,'e':15}
s=pd.Series(data)
print(s)

data={'a':11,'b':12,'c':13,'d':14,'e':15}
s=pd.Series(data,index=['e','b','c','a','j'])
print(s)

#Creating series from Scalar
s = pd.Series(5,index=[1,2,3,4])
print(s)

#Accessing data from series with position
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[0])
print(s[:3])
print(s[-3:])
print(s['a'])
print(s[['a','d']])

#Dataframe
df=pd.DataFrame()
print(df)

#Creating dataframe from lists
data=[1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

data=[['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

#Creating dataframe from dictionary
data={'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df=pd.DataFrame(data)
print(df)

data={'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df=pd.DataFrame(data, index=['a','b','c','d'])
print(df)

#Creating a DataFrame from List of Dicts
data=[{'a': 1,'b': 2},{'a': 5,'b': 10,'c': 20}]
df=pd.DataFrame(data)
print(df)

#Create a DataFrame from Dict of Series
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

#Column selection
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print (df ['two'])

#Column Addition
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)

print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']
print(df)

#Column deletion
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
   'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
print ("Our dataframe is:")
print(df)

print ("Deleting the first column using DEL function:")
del df['one']
print(df)

print ("Deleting another column using POP function:")
df.pop('two')
print(df)

#Selection by Label
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df.loc['b'])


#Addition of Rows
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = df.append(df2)
print(df)

#Deletion of Rows
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = df.append(df2)
df = df.drop(0)
print(df)