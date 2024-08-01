import pandas as p
t={
    'course':["py","jv","dbms","mma","mma"],
    'fee':[300,150,250,180,170],
    'complexity':[150,160,230,320,350]
}
d=p.DataFrame(t)
print(d)
c=d.groupby('course').agg({'fee':'min'})
print("\n",c)