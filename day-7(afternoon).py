#day_7
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


#moores algorithm
'''
a=[2,1,3,1,1,1,3]
c=1
res=a[0]
for i in range(1,len(a)):
    if(res==a[i]):
        c=c+1
    else:
        c=c-1
        if(c==0):
            res=a[i]
            c=1
print(res)
'''


#searching algorithm
'''
ip:[2,4,3,1,4,2,3,4,5]
x=4
linear search ,search the element with the last occurence of array''' 
'''
ip=[2,4,3,1,4,2,3,4,5]
x=4
last_index=1
for i in range(len(ip)):
    if ip[i]==x:
        last_index=i
if last_index!=-1:
    print(f"Last occurrence of {x} is at index {last_index}")
else:
    print(f"{x} not found in the list")
'''

#binary search
'''
[2,3,5,6,7,7,8,9,10,10,10,13,15]
find wheather element found or not
'''
'''
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return True  
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return False  

ip = [2, 3, 5, 6, 7, 7, 8, 9, 10, 10, 10, 13, 15]
x = 10

if binary_search(ip, x):
    print(f"{x} is found in the list.")
else:
    print(f"{x} is NOT found in the list.")
'''

#if there is duplicates values,print last occurence index
'''
def binary_search_last_occurrence(arr, x):
    low = 0
    high = len(arr) - 1
    result = -1  

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            result = mid      
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return result

ip = [2, 3, 5, 6, 7, 7, 8, 9, 10, 10, 10, 13, 15]
x = 10

index = binary_search_last_occurrence(ip, x)

if index != -1:
    print(index)
else:
    print("not found")
'''

'''
ip:[2,4,6,7,8,10,13,15]
x=3
if the element is found give the index of that eement ,if not found print where to be inserted.
'''








