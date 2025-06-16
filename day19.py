#memeoization o(2n)
'''def fib(n):
    if dp[n-1] != -1:
        return dp[n-1]
    if n==0:
        return 0
    if n==1:
        return 1
    dp[n-1] = fib(n-1) + fib(n-2)
    return dp[n-1]
n=7
dp = [-1] * n
fib(n)
print(dp)'''

#tabulation, o(n-2)
'''def fib_tab(n):
    for i in range(2,n):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n-1]

dp=[1,1]
print(fib_tab(n=7))
print(dp)'''

#optimized tabulation, o(n-2),o(1)
'''def fib_tab_nospace(n):
    f1 = 1
    f2 = 1
    ans = 0
    for i in range(2, n):
        ans = f1+f2
        f1=f2
        f2=ans
    return ans
print(fib_tab_nospace(n=7))'''


#find the total energy consumed to reach the nth step
# [10,20,30,10] , either one or two step
# o/p:20 (10->20,20->10)
def frog(i, a):
    if i < 0:
        return float('inf')  # very large cost so it's not chosen
    if i == 0:
        return 0
    if i == 1:
        return abs(a[1] - a[0])
    
    cost1 = frog(i - 1, a)
    jump1 = cost1 + abs(a[i] - a[i - 1])

    cost2 = frog(i - 2, a)
    jump2 = cost2 + abs(a[i] - a[i - 2])
    
    return min(jump1, jump2)
  # Output: 20

arr= [10, 20, 30, 10]
print(frog(len(arr)-1,arr))


'''a = [10, 20, 30, 10]
n = len(a) - 1
dp = [-1] * (n + 1)  # Memoization table

def frog(n):
    if n <= 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    
    one_step = frog(n - 1) + abs(a[n] - a[n - 1])
    two_steps = float('inf')
    if n > 1:
        two_steps = frog(n - 2) + abs(a[n] - a[n - 2])
    
    dp[n] = min(one_step, two_steps)
    return dp[n]

print(frog(n)) ''' # Output: 20

# Optimized tabulation approach
#Two jumps
'''a=[10,20,30,10,30,20,10]
dp=[0]*len(a)
dp[1] = abs(a[1] - a[0])
for i in range(2, len(a)):
    one_step = dp[i - 1] + abs(a[i] - a[i - 1])
    two_steps = dp[i - 2] + abs(a[i] - a[i - 2])
    dp[i] = min(one_step, two_steps)
print(dp[-1])'''


# k jumps
'''a=[10,20,30,10,30,20,10]
dp=[0]*len(a)
dp[1] = abs(a[1] - a[0])
k =3
for i in range(2, len(a)):
    mini = float('inf')
    for j in range(1, k + 1):
        if i-j>0:
            val=dp[i-j]+abs(a[i] - a[i - j])
            mini = min(mini, val)
    dp[i] = mini
print(dp[-1])'''


#inputs: [(1,2),(2,5),(4,6),(5,8),(6,7),(7,9)]
#pay    = [5,     6,     5.   4,     11,    2]
#output:22

