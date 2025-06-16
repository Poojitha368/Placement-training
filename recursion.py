'''def qwer(n):
    if n==0:
        return
    print(n)
    qwer(n-1)
    print(n)

qwer(5)'''


'''def qwer(n):
    if n==0:
        return
    print("first time",n)
    qwer(n-1)
    print("second time",n)
    qwer(n-1)

qwer(5)'''



'''def qwer(n,cnt=0):
    if n==0:
        return 0
    return 1+qwer(n-1,cnt+1)

print(qwer(5))'''


'''def qwer(n):
    if n>5:
        return
    qwer(n+1)
    print(n)

qwer(n=1)'''

'''def sum_n(n,s=0):
    if n==0:
        return s
    return sum_n(n-1,s+n)
print(sum_n(5))'''

'''def sum_n(n):
    if n==0:
        return 0
    return n+sum_n(n-1)

print(sum_n(5))'''

'''def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    s = fib(n-1) + fib(n-2)
    return s
print(fib(7))'''


