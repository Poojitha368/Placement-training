
#array = [],k= , print the count of k in array
'''def count_k(arr,k,i,count):
    if i==len(arr):
        return count
    if arr[i]==k:
        return count_k(arr,k,i+1,count+1)
    return count_k(arr,k,i+1,count)

arr=[2,4,6,3,3,2,6,1,2,3,6,6,5]
k=6
print(count_k(arr,k,0,0))'''

#array =[2,3,3,4,4,4,5,6,6,6] ,print the array with count=2 #output=3
'''def count_k(arr,k,i):
    if i==len(arr):
        return 0
    if arr[i]==k:
        return 1+count_k(arr,k,i+1)
    return count_k(arr,k,i+1)
def iterate(arr,i,freq):
    if i==len(arr):
        return
    if(count_k(arr,arr[i],0)==freq):
        return arr[i]
    return iterate(arr,i+1,freq)


arr=[2,3,3,4,4,4,5,6,6,6]
print(iterate(arr,0,2))  #3'''

#finding frequency of elements using dictionary
'''
def freq_d(arr,i,d):
    if i==len(arr):
        return d
    if arr[i] not in d:
        d[arr[i]] = 1
    else:
        d[arr[i]] += 1
    return freq_d(arr,i+1,d)

arr=[2,2,3,3,4,5,4,5,4]
freq=3
print(freq_d(arr,0,{}))'''


#finding frequency of elements using dictionary and find ele with k frequency
'''def value(x,i,f,d):
    if i==len(x):
        return "not found"
    if(d[x[i]] == f):
        return x[i]
    return value(x,i+1,f,d)

def freq_d(arr,i,d,f):
    if i==len(arr):
        return value(list(d.keys()),0,f,d)
    if arr[i] not in d:
        d[arr[i]] = 1
    else:
        d[arr[i]] += 1
    return freq_d(arr,i+1,d,f)

arr=[2,2,3,3,4,5,4,5,4]
freq=3
print(freq_d(arr,0,{},freq))'''

#print all subsets [2,3,4] = [2],[3],[4],[2,3],[3,4],[2,4],[2,3,4]
'''def subset(x,s=[],i=0):
    if i==len(x):
        print(s)
        return
    subset(x,s+[x[i]],i+1) #include
    subset(x,s,i+1)        #exclude

a=[1,2,3]
subset(a)'''

#given arr [1,2,4,5] find if subset sum k exists k=6
#approach : do k-arr[i] for each element is k-arr[i]>0 else return if got 0 then sum there
'''def SubsetSum(arr,k,i,map):
    if map==0:
        return True
    if map<0:
        return 
    map = k-arr[i]
    return SubsetSum(arr,k,i+1,map)

arr = [1,4,5]
k=7
print(SubsetSum(arr,k,0,0))'''


'''sums=[]
def subset_sum(arr,i,c_sum,t):
    if c_sum==t:
        return True
    if i==len(arr):
        sums.append(c_sum)
        return False
    if subset_sum(arr,i+1,c_sum+arr[i],t):
        return True
    if subset_sum(arr,i+1,c_sum,t):
        return True
    return False
    
arr=[1,2,3]  
t=5
print(subset_sum(arr,0,0,t))
print(sums)'''

#coins = [2,4,6,8] &  amount = 13 , o/p: -1
#coins = [2,4,6,8] and amount = 14 , o/p:2
# find the minimum no of coins required to make the given amount else -1
'''def min_coins(coins,i,j,sum,target,min_len):
    if i>=len(coins) or j>=len(coins):
        return min_len
    if sum == target:
        min_len = min(j-i+1,min_len)
    sum += coins[j]
    if sum>target:
        return min_coins(coins,i+1,j,sum-coins[i],target,min_len)
    return min_coins(coins,i,j+1,sum,target,min_len)

target = 14
coins = [2,4,6,8]
print(min_coins(coins,0,0,0,target,-1))'''

#largest even no and smallest odd number
'''nums = list(map(int,input().split()))
even_max,odd_min = float('-inf'),float('inf')
for num in nums:
    if num%2==0:
        even_max = max(num,even_max)
    else:
        odd_min = min(num,odd_min)
print(even_max,odd_min)'''

#find the second largest number in array
'''nums = list(map(int,input().split()))
first_max,second_max = float('-inf'),float('inf')
for num in nums:
    if num>first_max:
        second_max=first_max
        first_max=num
    elif num<first_max and num>second_max:
        second_max = num
print(first_max,second_max)'''



