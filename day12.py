# i/p: "abcedacefaebg", m='c',n='d', o/p:5
#find the length of longest non repeating substring having m and n in it
'''def longest_nonrepeating_substring_mn(s):
    v = {}
    l = 0
    m, n = 'c', 'd'
    max_len = 0
    start = 0

    for r in range(len(s)):
        if s[r] in v and v[s[r]] >= l:
            l = v[s[r]] + 1

        v[s[r]] = r

        if (m in v and n in v) and (v[m] >= l and v[n] >= l):
            if r - l + 1 > max_len:
                max_len = r - l + 1
                start = l

    return s[start:start + max_len], max_len

s="abcedacefaebghd"
print(longest_nonrepeating_substring_mn(s))'''

#i/p: [4,2,7,20,8,6,4,1], remove k=3 cards from first or last such that get max score
'''cards = [4,2,7,20,8,6,4,1]
l=0
k=3
r=len(cards)-1
total_sum=0
while l<r:
    if k==0:
        break
    if cards[r]>cards[l]:
        total_sum += cards[r]
        r-=1
        k-=1
    elif cards[r]<cards[l]:
        total_sum += cards[l]
        l+=1
        k-=1
    else:
        if cards[l+1]>cards[r-1]:
            total_sum += cards[l]
            k-=1
            l+=1
        else:
            total_sum += cards[r]
            k-=1
            r-=1
print(total_sum)'''

'''cards = [4,3,2,5,6,1,12,3]
k=3
l,r=0,0 
max_sum=0
sl = 0
n=len(cards)
for i in range(k):
    sl += cards[i]
sr=0
max_sum=sl
for i in range(k-1,-1,-1):
    sl -= cards[i]
    sr += cards[n-1]
    max_sum = max(max_sum,sl+sr)
    n-=1
print(max_sum)'''

#leetcode 904 
#fruits = [1,2,1] , o/p:3
'''a=[4,4,2,1,2,2,1,4,4,3]
l,max_len=0,0
d={}
for r in range(len(a)):
    if a[r] not in d:
        d[a[r]]=1
    else:
        d[a[r]]+=1
    if len(d)>2:
        d[a[l]]-=1
        if d[a[l]] == 0:
            del d[a[l]]
        l+=1
    else:
        max_len = max(max_len,r-l+1)
print(max_len)'''


#i/p 
# start = [900,945,1110,1230,1235,1245,1340,1700]
# end   = [930,1130,1120,1250,1250,1415,1400,1730]
# find the min no of doctors required to treat all patient in times above
