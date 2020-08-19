#1
"""import numpy as np
import random

data = []

for x in range(317):
    data.append(random.randrange(59))
    
print("mean: " , np.mean(data))
print("median: " , np.median(data))
print("50th percentile (median): " , np.percentile(data, 50))
print("25th percentile: " , np.percentile(data, 25))
print("75th percentile: " , np.percentile(data, 75))
print("standard deviation: " , np.std(data))
print("variance: ", np.var(data))"""


#2
"""import pandas as pd

#df = pd.read_csv("https://sololearn.com/uploads/files/titanic.csv")
df = pd.read_csv("titanic.csv")
print(df.head())
pd.options.display.max_columns = 8
pd.set_option('display.expand_frame_repr', False)
print(df.describe())

col = df['Fare']
print(col)

small_df = df[['Age','Sex','Survived']]
print(small_df.head())

print("\n\n")

df['male'] = df['Sex'] == 'male'

print(df.head())


print("\n\n\n")
####Creating a numpy array from a pandas series.
#print(df['Fare'].values)
#print(df[['Pclass','Fare','Age']].values)

arr = df[['Pclass','Fare','Age']].values
print(arr.shape)"""



"""#3
import pandas as pd
df = pd.read_csv("titanic.csv")
arr = df[['Pclass','Fare','Age']].values
print(arr[0, 1])
print(arr[0])
#print(arr[:,2])


#A mask is a boolean array (True/False values) that tells us which values from the array we’re interested in.
mask = arr[:,2] < 18
#print(arr[mask])
print(arr[arr[:,2] < 18])

#Summing an array of boolean values gives the count of the number of True values.
print(mask.sum())
print((arr[:,2] < 18).sum())"""



#4
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('titanic.csv')

plt.scatter(df['Age'], df['Fare'], c=df['Pclass'])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.plot([0, 80], [85, 5])
plt.colorbar()
plt.show()

