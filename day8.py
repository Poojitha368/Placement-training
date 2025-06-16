#find square root of a number for n=38 and its floor value without sqrt and floor
'''def square_root(n):   #o(n)
    for i in range(n//2):
        if i*i==n:
            return i
        if i*i>n:
            return i-1
n=38
print(square_root(n))'''

#o(logn)
'''def square_root(n):
    l=0
    r=n//2
    while l<=r:
        m=(l+r)//2
        if m*m == n:
            return m
        elif m*m>n:
            r=m-1
        else:
            l=m+1
    return r
n=38
print(square_root(n))'''

#find the index where the array is rotated
#[15,18,20,22,2,5,8,10,12,13] , o/p: (3,4)
#             l            r
'''def rotated_binary_serach(a):
    l=0
    r=len(a)-1
    while l<=r:
        m=(l+r)//2
        if a[r]>a[m]: #m in sorted part
            r=m
        else:
            l=m+1
    return r
        
arr=[15,18,20,22,2,5,8,10,12,13]
print(rotated_binary_serach(arr))'''

### 🔹 **Basic Binary Search**

# 1. **Search Element in Sorted Array**
#    Given a sorted array and a target value, return the index if the target is found. Otherwise, return -1.

# 2. **Find First and Last Position of Element in Sorted Array**
#    Leetcode 34: `Input: nums = [5,7,7,8,8,10], target = 8 → Output: [3,4]`

# 3. **Insert Position**
#    Leetcode 35: Given a sorted array, find the index where a target should be inserted to maintain order.

# ---

# ### 🔹 **Binary Search Variants**

# 4. **Find the Peak Element**
#    A peak element is greater than its neighbors. Find any peak element. (Leetcode 162)

# 5. **Find Minimum in Rotated Sorted Array**
#    Leetcode 153: `Input: [4,5,6,7,0,1,2] → Output: 0`

# 6. **Search in Rotated Sorted Array**
#    Leetcode 33: Search for a target in a rotated sorted array.

# 7. **Count Occurrences of a Number**
#    Find how many times a number appears in a sorted array.

# ---

# ### 🔹 **Binary Search on Answer (Search Space)**

# 8. **Koko Eating Bananas**
#    Leetcode 875: Min eating speed `K` so Koko can finish all bananas in `H` hours.

# 9. **Minimum Number in Sorted Array After Rotation**
#    Like Leetcode 153, find the min element in a rotated sorted array.

# 10. **Capacity to Ship Packages Within D Days**
#     Leetcode 1011: Given weights and D days, return the minimum ship capacity.

# 11. **Aggressive Cows** (Popular in coding interviews)
#     Place cows in stalls so the minimum distance between them is maximized.

# 12. **Allocate Minimum Number of Pages**
#     Given books and students, minimize the max pages a student has to read.

# ---

# ### 🔹 **Matrix-Based**

# 13. **Search a 2D Matrix**
#     Leetcode 74: Binary search in a 2D matrix where rows and columns are sorted.

# 14. **Search in a Row and Column-wise Sorted Matrix**
#     Leetcode 240: Each row and column is sorted. Search for a target.


#find any of the peak element(which is greater than its neighbours)
# i/p : [2,3,4,6,3,2,1,5,8,10,1,4,2]
# o/p : 6 or 10 or 4

'''def peak_element(a):
    l=0
    r=len(a)-1
    n=len(a)
    while l<=r:
        m=(l+r)//2
        if (m==0 and a[m]>a[m+1]) or (m==n-1 and a[m]>a[m-1]) or (a[m]>a[m-1] and a[m]>a[m+1]):
            return m
        if a[m+1]>a[m-1]:
            l=m+1
        else:
            r=m-1
    return -1
arr=[2,3,4,6,3,2,1,5,8,10,1,4,2]
print(peak_element(arr))'''

#input => h=8,k=3 (eating 3 banaas/hr in 8hrs) , output = True/false
'''import math
def koko_bananas(h,k,a):
    tot_time = 0
    for i in range(len(a)):
        b_hr = math.ceil(a[i]/k)
        tot_time += b_hr
        if tot_time == h:
            return True
    return False
h=8
k=5
arr=[3,6,7,11]
print(koko_bananas(h,k,arr))'''

'''import math    #o(n**2)
def koko_bananas(h,a):
    tot_time = 0
    k=0
    while(1):
        k+=1
        tot_time=0
        for i in range(len(a)):
            b_hr = math.ceil(a[i]/k)
            tot_time += b_hr
            if tot_time>h:
                break
            if tot_time == h:
                return k
h=8
arr=[3,6,7,11]
print(koko_bananas(h,arr))'''

'''import math  #o(n*logn)
def koko_bananas(h,a,k):
    tot_time = 0
    for i in range(len(a)):
        b_hr = math.ceil(a[i]/k)
        tot_time += b_hr
        if tot_time>h:
            break
        if tot_time == h:
            return True
    return False
def binary_serach(h,a):
    l=0
    r=max(a)
    while l<=r:
        m=(l+r)//2
        if koko_bananas(h,a,m):
            r=m-1
        else:
            l=m+1
    return l

h=8
arr=[3,6,7,11]
print(binary_serach(h,arr))'''

#i/p = [1,2,5,7,10]
# k = 4 , possible (1,5,10)
# k = 5, not possible (1,5,10)x
a=[1,2,5,7,10,12]
k=3
mini = 5
prev=a[0]
k=k-1
for i in range(len(a)):
    if i-prev >= mini:
        prev=i
        k=k-1
    if k==0:
        print("possible")
        break
    else:
        print("not possible")
        break
#to reduce the time complexity perform binary search same as koko but reverse the condition l,r conditions,