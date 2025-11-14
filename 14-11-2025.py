base=5
exp=2
res=1
while exp!=1:
    if exp%2!=0:
        res*=2
    exp = exp//2
    base=base*base

print(base*res)