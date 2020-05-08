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

a = 45545454
b = a + 55
