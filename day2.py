# ### ✅ **Beginner Level**

# 1. **Check if a number is even or odd**
#    👉 Use: `num & 1`

# 2. **Check if a number is a power of 2**
#    👉 Use: `n > 0 and (n & (n - 1)) == 0`

# 3. **Count the number of set bits (1s) in a number**
#    👉 Use: `n & (n - 1)` in a loop

# 4. **Find the only non-repeating element in an array where every other element appears twice**
#    👉 Use: XOR (`^`) or sliding window

# 5. **Swap two numbers without using a temporary variable**
#    👉 Use: XOR swap

# ---

# ### 🧠 **Intermediate Level**

# 6. **Find the missing number in an array of size `n` containing numbers from `0` to `n`**
#    👉 Use XOR from `0 to n` and XOR with array elements

# 7. **Find the two non-repeating elements in an array where every other element appears twice**
#    👉 Use XOR with bitmasking

# 8. **Determine if two numbers have opposite signs**
#    👉 Use: `(a ^ b) < 0`

# 9. **Turn off the rightmost set bit**
#    👉 Use: `n & (n - 1)`

# 10. **Isolate the rightmost set bit**
#     👉 Use: `n & -n`

# ---

# ### 🚀 **Advanced Level**

# 11. **Count the total set bits from 1 to n**
#     👉 Recursively or using Brian Kernighan's algorithm

# 12. **Generate all subsets of a set using bitmasks**

# 13. **Find the XOR of all subsets of an array**

# 14. **Find the maximum XOR of any two numbers in an array**

# 15. **Implement a Trie of binary bits to optimize XOR-based problems**

# ---

# ### Bonus Bitwise Practice Platforms:

# * **LeetCode**: Try problems with tags like `bit manipulation`
# * **HackerRank**: Bit Manipulation section
# * **Codeforces/AtCoder**: Search for tags like "bitmasks"
# 1^2^3^4^5 value in o(1) than o(n)
'''def func(n):
    if n%4==1:
        return 1
    elif n%4==2:
        return n+1
    elif n%4==0:
        return n
    else:
        return 0

# print(func(n))'''
#find input =5 and 10 
# find 5^6^7^8^9^10
# (1to10 - 1to5)
'''
n=5
m=10
print(func(m)^func(n-1)) #(1^2^3^4^5^6^7^8^9^10)^(1^2^3^4) = (5^6^7^8^9^10)   '''

#find the element which occurs one time and others occuring twice [2,2,4,4,6,6,7,8,8,9,9] (sliding window)
'''arr = [2,2,4,4,6,6,7,8,8,9,9] o(n/2)
i,j=0,1
while j<len(arr):
    if arr[i]!=arr[j]:
        print(arr[i])
        break
    i+=2
    j=i+1'''

#find the element which occurs one time and others occuring twice [2,2,4,4,6,6,7,8,8,9,9](o(logn))
'''arr = [2, 2, 4, 4, 6, 6, 7, 8, 8, 9, 9]
l, r = 0, len(arr) - 1

while l <= r:
    m = (l + r) // 2

    # Edge cases to prevent index errors
    if m == 0 or m == len(arr) - 1:
        print(arr[m])
        break

    if arr[m] != arr[m - 1] and arr[m] != arr[m + 1]:
        print(arr[m])
        break
    elif arr[m] == arr[m - 1]:
        if (m - l + 1) % 2 == 0:
            l = m + 1
        else:
            r = m - 2
    else:
        if (r - m + 1) % 2 == 0:
            r = m - 1
        else:
            l = m + 2'''

#find the length of longest subsequence [2,3,4,6,7,8,9,1,2,3,4,5,6,7,3,4,5,10,9]
'''arr = [2,3,4,6,7,8,9,1,2,3,4,5,6,7,3,4,5,10,9]
print(arr)
count=1
max_count=0
for i in range(len(arr)-1):
    if arr[i+1]-arr[i] == 1:
        count+=1
        max_count = max(count,max_count)
    else:
        count=1
print(max_count)'''

#find if input = "aaabbaaaacccddeff" output="a3b2a4c3d2e1f2"
'''s = "aaabbaaaacccddeff"
res_string = ""
i = 0
count=1
while i < len(s)-1:
    if s[i]==s[i+1]:
        count+=1
    else:
        res_string += s[i] + str(count)
        count=1
    i += 1
res_string += s[-1]+str(count)
print(res_string)'''