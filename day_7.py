#day_7
#merge sort
'''
ip:[2,4,5,8,9]
[3,5,6,9,11,12,13]
merge two lists to single sorted list
op:[2,3,4,5,5,6,8,9,11,12,13]
'''
'''
list1=[2,4,5,8,9]
list2=[3,5,6,9,11,12,13]
i=j=0
merged=[]
while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        merged.append(list1[1])
        i+=1
    else:
        merged.append(list2[j])
        j+=1
while i < len(list1):
    merged.append(list1[i])
    i += 1

while j < len(list2):
    merged.append(list2[j])
    j += 1

print(merged)
'''

#second classmethod
'''
a=[2,4,5,6,7]
b=[2,4,5,8,9,10,13,14,15]
c=[]
i=0
j=0
while(i<len(a) and j<len(b)):
    if(a[i]<b[j]):
        c.append(a[i])
        i=i+1
    else:
        c.append(b[j])
        j=j+1
while(j<len(b)):
    c.append(b[j])
    j=j+1
while(i<len(a)):
    c.append(a[i])
    i=i+1
print(c)
'''


#recursion for merge sort
'''
def merge_sort(x):
    m=len(x)//2
    l=merge_sort(x[ :m])
    r=merge-sort(x[m: ])
     return merge(l,r)
def merge(l,r):
    c=[]
    i,j=0,0
    while(i<len(l) and j<len(r)):
         if(l[i]<r)
    
    return c
    
'''


#another question
'''
ip:[2,13,4,2,9,9,5,8,7,13,3]
k=3
find the kth largest number without using bubble sort,sort keyword also.do using frequency
if in case we consider duplicate values print the answer

'''
'''
a = [2, 13, 4, 2, 9, 5, 8, 7, 13, 3]
k = 3
for i in range(k):
    max_val = a[0]
    for num in a:
        if num > max_val:
            max_val = num
    a.remove(max_val)
print(max_val)
'''

#if in case we  does not consider  duplicate values print the answer
'''
a = [2, 13, 4, 2, 9, 5, 8, 7, 13, 3]
k = 3

unique_vals = list(set(a)) 

for i in range(k):
    max_val = unique_vals[0]
    for num in unique_vals:
        if num > max_val:
            max_val = num
    unique_vals.remove(max_val)

print(max_val)
'''

#second classmethod(with duplicates)
'''
a=[3,6,13,8,5,4,7,13,8,2,7]
k=3
b=[0 for i in range(max(a)+1)]
print(b)
for i in a:
    b[i]=1
print(b)
for i in range(len(b)-1,-1,-1):
    if(b[i]==1):
        k=k-1
    if(k==0):
        print(i)
        break
'''


# largest frequency
'''
a=[3,4,4,5,3,4,2,3,6,7,8,8,7,6,7,7,1,1,1]
d={}
for i in a:
    if(i not in a):
        d[i]=i
    else:
        d[i]+=1
m=0
for i in a:
    if(d[i]>m):
        m=d[i]
        res=1
    print(res)
'''


#kth largest frequency
'''
a=[7,7,7,3,3,2]
d={}
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1
print(d)
m=max(d.values())
b=[0 for i in range(m+1)]
for i in d:
    b[d[i]]=i
print(b[-i])
'''



'''ip:[2,1,1,2,3,1,1]
find the no ,of freq is >(n/2)
find number whose freq is half half the list
op:1'''
'''
a=[2,1,1,2,3,1,1]
n=len(a)
d={}
for i in a:
    d[i]=d.get(i,0)+1
for key in d:
    if d[key]>n//2:
        print(key)
        break
'''

#without using dictionary



