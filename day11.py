#find the max no of jobs scheduled 
# start_time = [0,3,8,1,5,7,9]
# end_time =   [5,7,10,2,6,9,11], o/p: 3
'''def sort_endtime(j):
    return j[1]
start = [0,3,8,1,5,7,9]
end =   [5,7,10,2,6,9,11]
jobs=[5,7,10,2,6,9,11]
jobs=list(zip(start,end))
jobs.sort(key=sort_endtime)
start_time = 0
meetings=0
for s,e in jobs:
    if s>=start_time:
        start_time = e+1
        meetings+=1
print(meetings)'''

# i/p:"hippopotamus",o/p:"simtopopapuh"
'''def reverse_string_without_changind_vowels(s):
    idx = []
    for i in range(len(s)):
        if s[i].lower() not in ['a','e','i','o','u']:
            idx.append(i) 
    l=0
    r=len(idx)-1
    string=list(s)
    while l<=r:
        string[idx[l]],string[idx[r]]=string[idx[r]],string[idx[l]]
        l+=1
        r-=1
    return "".join(string)

s='hippopotamus'
print(reverse_string_without_changind_vowels(s))'''

'''def is_consonant(char):
    if char not in ['a','e','i','o','u']:
        return True
    return False
def reverse_string_without_changind_vowels(string):
    l=0
    r=len(string)-1
    s=list(string)
    while l<r:
        if is_consonant(s[l]) and is_consonant(s[r]):
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        elif not is_consonant(s[l]):
            l+=1
        elif not is_consonant(s[r]):
            r-=1
        else:
            l+=1
            r-=1
    return "".join(s)

s='hippopotamus'
print(reverse_string_without_changind_vowels(s))'''

#ip:[2,1,6,4,2,3,1,1,4,2,6,7,3], contigous k no of books should be picked , return max_discount

'''books = [2,1,6,4,2,3,1,1,4,2,6,7,3]
sums=0
max_sum=0
for i in range(len(books)-4):
    sums=0
    for j in range(i,i+5):
        sums+=books[j]
    max_sum = max(max_sum,sums)
print(max_sum)'''

'''books = [2,1,6,4,2,3,1,1,4,2,6,7,3]
l=0
k=5
curr_sum,max_sum = 0,0
for i in range(len(books)):
    if i<k:
        curr_sum+=books[i]
    elif i>=k:
        curr_sum = curr_sum-books[l]+books[i]
        max_sum = max(curr_sum,max_sum)
        l+=1
print(max_sum)'''

#find the length of longest subarray with sum<=k
# i/p:[2,1,4,6,2,3,1,1,4,2,6,7,3], k=6
def longest_subarray_ksum(arr):
    curr_sum = 0
    k=7
    i=0
    length,max_len=0,0
    for j in range(len(arr)):
        curr_sum += arr[j]
        if curr_sum <= k:
            length = j-i+1
            max_len = max(length,max_len)
        if curr_sum>k:
            curr_sum -= arr[i]
            i+=1
    return max_len

arr=[2,1,4,6,2,3,1,1,4,2,6,7,3]
print(longest_subarray_ksum(arr))

#i/p: "ababba",o/p:4
#find the length of longest palindromic substring
'''def longest_palindrome_substring(s):
    l,r=0,0
    max_len=0
    for i in range(len(s)):
        #odd length palindrome
        l,r=i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            max_len = max(max_len,r-l+1)
            l-=1
            r+=1
        l,r=i,i+1
        #even length palindrome
        while l>=0 and r<len(s) and s[l]==s[r]:
            max_len = max(max_len,r-l+1)
            l-=1
            r+=1
    return max_len

s="ababba"
print(longest_palindrome_substring(s))'''

'''def longest_palindrome_substring(s):
    l,r=0,0
    max_len=0
    start=0
    for i in range(len(s)):
        #odd length palindrome
        l,r=i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            # max_len = max(max_len,r-l+1)
            if r-l+1 > max_len:
                max_len = r-l+1
                start = l
                end=r
            l-=1
            r+=1
        l,r=i,i+1
        #even length palindrome
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1 > max_len:
                max_len = r-l+1
                start = l
            l-=1
            r+=1
    return s[start:start+max_len]

s="ababba"
print(longest_palindrome_substring(s))'''


'''def longest_palindrome_substring(s):
    l,r=0,0
    max_len=0
    c=0
    for i in range(len(s)):
        #odd length palindrome
        l,r=i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            max_len = max(max_len,r-l+1)
            l-=1
            r+=1
            c+=1
        l,r=i,i+1
        #even length palindrome
        while l>=0 and r<len(s) and s[l]==s[r]:
            max_len = max(max_len,r-l+1)
            l-=1
            r+=1
            c+=1
    return c

s="ababba"
print(longest_palindrome_substring(s))'''

#i/p: "abcdaecdb" , o/p:4
'''def longest_nonrepeating_substring(s):
    v={}
    l=0
    max_len=0
    for r in range(len(s)):
        if s[r] in v and l < v[s[r]]:
            l = v[s[r]] + 1
        v[s[r]]=r
        max_len = max(max_len,r-l+1)
        
    return max_len

s="abcdcecdb"
print(longest_nonrepeating_substring(s))'''



