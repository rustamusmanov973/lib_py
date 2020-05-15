from collections import defaultdict
fl = "/Users/rst/Library/Mobile Documents/com~apple~CloudDocs/ARCHIVE/uniprot3rep2.txt"
with open(fl, 'r') as f:
    fls = f.readlines()
    fls = [i.strip() for i in fls][1:]
    # d = defaultdict(frozenset)
    v = defaultdict(int)
    
    for j in fls:
        js = j.split()
        # v[js[0]] += int(js[-1])
        v[frozenset(js[:-1])] += int(js[-1])

dfv = {" ".join(k): v for k, v in v.items()}
from pandas import DataFrame
df = DataFrame.from_dict(dfv, orient='index')
print(df)
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
# plt.show()
a = 45545454
b = a + 55

import sys
sys.path.append("/usr/local/lib/python3.7/site-packages")

import termplotlib as tpl
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x) + x
fig = tpl.figure()
fig.plot(x, y, width=60, height=20)
fig.show() 

x = np.linspace(0, 2*np.pi, 100)
y = np.cos(x) + x
fig = tpl.figure()
fig.plot(x, y, width=60, height=20)
fig.show() 

print("aa")
print("aa")
k = "adda"
v = "lkjkjkjkjadda"
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

