#Series Basic Functionality

import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(4))
print(s)

#axes
print ("The axes are:")
print(s.axes)

#empty
print ("Is the Object empty?")
print(s.empty)

#ndim
print ("The dimensions of the object:")
print(s.ndim)

#size
print ("The size of the object:")
print(s.size)

#values
print ("The actual data series is:")
print(s.values)

#head()
print ("The first two rows of the data series:")
print(s.head(2))

#tail()
print ("The last two rows of the data series:")
print(s.tail(2))

#DataFrame Basic Functionality
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df = pd.DataFrame(d)
print ("Our data series is:")
print(df)

#T (Transpose)
print ("The transpose of the data series is:")
print(df.T)

#axes
print ("Row axis labels and column axis labels are:")
print(df.axes)

#dtypes
print ("The data types of each column are:")
print(df.dtypes)

#empty
print ("Is the object empty?")
print(df.empty)

#ndim
print ("The dimension of the object is:")
print(df.ndim)

#shape
print ("The shape of the object is:")
print(df.shape)

#size
print ("The total number of elements in our object is:")
print(df.size)

#values
print ("The actual data in our data frame is:")
print(df.values)

#head
print ("The first two rows of the data frame is:")
print(df.head(2))

#tail
print ("The last two rows of the data frame is:")
print(df.tail(2))

