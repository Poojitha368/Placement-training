'''def even_sum(a, i):
    if i > len(a) - 1:
        return 0
    if a[i] % 2 == 0:
        return a[i]+even_sum(a, i + 1) #handling even nos
    else:
        return even_sum(a,i+1)

a = [2, 5, 6, 7, 2, 1, 4, 3, 6]
print(even_sum(a, 0))     '''


# ### 🟢 Beginner-Level Recursion Questions

# 1. **Factorial of a number**
#    📌 Input: `n`, Output: `n!`

# 2. **Sum of first N natural numbers**
#    📌 Input: `n`, Output: `1 + 2 + ... + n`

# 3. **Print numbers from 1 to N and N to 1 using recursion**

# 4. **Check if a string is a palindrome**

# 5. **Find the nth Fibonacci number**
#    (Use memoization later to optimize)

# 6. **Sum of digits of a number**
#    📌 Input: `123`, Output: `6`

# 7. **Count the number of digits in a number**

# ---

# ### 🟡 Intermediate-Level Recursion Questions

# 8. **Reverse a string using recursion**

# 9. **Binary Search using recursion**

# 10. **Check if an array is sorted recursively**


# 11. **Generate all subsets (power set) of a string or array**

# 12. **Tower of Hanoi problem**

# 13. **Find the first and last occurrence of an element in an array**

# 14. **Find all indices of a number in an array**

# ---

# ### 🔴 Advanced-Level Recursion Questions

# 15. **Permutations of a string/array**
#     📌 e.g., `"abc"` → `["abc", "acb", "bac", "bca", "cab", "cba"]`

# 16. **N-Queens Problem**

# 17. **Sudoku Solver**

# 18. **Rat in a Maze (Backtracking)**

# 19. **Word Break Problem using recursion**

# 20. **Generate all balanced parentheses for given n pairs**

# 21. **Count number of ways to reach the nth stair (Climbing stairs problem)**
#     (like Fibonacci but with multiple options: 1 or 2 steps)

# ---

# ### Bonus: Recursion + DP Combo

# * **Edit Distance problem**
# * **Minimum path sum in a grid**
# * **Knapsack Problem (0/1)**

# 5! = 5x4x3x2x1
'''def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))'''


'''def sum_n(n):
    if n==1:
        return 1
    return n+sum_n(n-1)
print(sum_n(10))'''

# input=153
# output = 351

'''def reverse(rev, n):
    if n == 0:
        return rev
    return reverse(rev * 10 + (n % 10), n // 10)

print(reverse(0, 153))  # Output: 351'''

#count of prime nos in [13,17,21,23,22,7,29] using recursion
'''def isprime(n,i):
    if i==n:
        return True
    if n%i==0:
        return False
    return isprime(n,i+1)

def count_primes(arr,i,count):
    if i==len(arr):
        return count
    if isprime(arr[i],i=2):
        return count_primes(arr,i+1,count+1)
    else:
        return count_primes(arr,i+1,count)

arr = [13,17,21,23,22,7,29]
print("no of primes:", count_primes(arr,i=0,count=0))'''  # Output: 4

#input = 20, wehave to subtract 3 and 5 from it so is it possible to reach 1 or not
# [20,17,15,14,12,12,10]etc 

'''def is_one(n):
    if n<1:
        return False
    if n==1:
        return True
    left = 1+is_one(n-3)
    right= 1+is_one(n-5)
    return min(left,right) #min no of operations
          #path: 20 → 17 → 14 → 11 → 6 → 1 ✅

print(is_one(20))'''

#using bfs to 
# def bfs(n):
#     queue =[n]
#     visited=[]
#     while(1):
#         queue.pop()

#palindrome string or not using recursion
'''def palindrome(s,i,j):
    if s[i]!=s[j]:
        return False
    if i>=j:
        return True
    return palindrome(s,i+1,j-1)

s = "hello"
print(palindrome(s,0,len(s)-1))'''



#check if array is sorted
'''def is_sorted(arr,i,j):
    if j>=len(arr):
        return True
    if arr[i]>arr[j]:
        return False
    return is_sorted(arr,i+1,j+1)

arr=[1,2,3,6,5]
print(is_sorted(arr,0,1))'''

#sum of digits in a number
'''def sum_digits(n):
    if n<=0:
        return 0
    return n%10 + sum_digits(n//10)
print(sum_digits(555))'''

# rev a string using recursion
'''def reverse(s,i,j):
    if i>=j:
        return "".join(s)
    s[i],s[j] = s[j],s[i]
    return reverse(s,i+1,j-1) 
s="pooja"
print(reverse(list(s),0,len(s)-1))'''

#binary search using recursion
'''def binary_search(arr,l,r,target):
    if l>r:
        return -1
    m=(l+r)//2
    if arr[m]==target:
        return f"found at {m} index"
    elif arr[m]>target:
        r=m-1
    else:
        l=m+1
    return binary_search(arr,l,r,target)

arr=[1,3,5,6,7,8]
target = 6
print(binary_search(arr,0,len(arr)-1,target))'''