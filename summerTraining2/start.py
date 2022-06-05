import numpy as np
import pandas as pd

myArr = np.array([1,2,3,4,"ahmed","mansour"])

print(type(myArr))


x=[1,2,3,4]
s=pd.Series(x, index=['A','N','S','V'])
print(s)

print(s.index)

print(s.values)

# or

g={
    'name':'ahmed ayman',
    'age':21,
    'skills':['C#','Python','C++'],
    'Education':'Medical Informatics'
}

r=pd.Series(g)
print(r)

#Condition
print(s[s>2])

df = pd.DataFrame(r)
print(df)