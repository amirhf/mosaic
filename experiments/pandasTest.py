
import pandas as pd
class A:
    def __init__(self, a: int, b: str):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"A({self.a}, {self.b})"


a = A(1, "a")
b = A(2, "b")
print([(x,a.__getattribute__(x)) for x in dir(a) if not x.startswith("__")])
a= list(zip([1, 2, 3], ["a", "b", "c"]))
print([x for x in map(lambda x: x[0], a)])

print(a)
d= dict(a)
print (d)
for i, item in enumerate(a):
    print(i, item)
"""
l = range(1, 6)
# l is [1, 2, 3, 4, 5]
idx = ["aa", "bb", "ccc", "dddd", "eeeeee"]
s = pd.Series(index=l, data=idx)
print(s)
print("------------------")
#i = "ccc"
#print("the index {} -> value is {}".format(i, s[i]))
d = {'bb': 1, 'a': 0, 'ccc': 2}
s = pd.Series(d)
print(s)
print("------------------")
i = "ccc"
print("the index {} -> value is {}".format(i, s[i]))

import numpy as np


l = np.arange(1, 10)
print(type(l))
print("----------------------------")
s = pd.Series(l)
print(s)
i = 3
print("the index {} -> value is {}".format(i, s[3]))

def f(x: list):
    x.append(1)


l = [1, 2, 3]
f(l)
print(l)
"""
