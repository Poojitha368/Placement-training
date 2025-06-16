#optimized code
'''def bubble_sort(arr):
    for j in range(len(arr)-1):
        swapped = False
        for i in range(len(arr)-1-j):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped = True
        if swapped == False:
            break
        else:
            print(arr)
    return arr
arr=[3,5,6,1,7]
print(bubble_sort(arr)) '''

# ip = [5,2,3,8,1,6,7], k=2 
# op = [5,2,1,3,8,6,7] , need to leave first  and last k elements and sort rest
'''def sort_k(arr,k):
    start = k
    end= len(arr)-k
    for i in range(start,end):
        for j in range(i+1,end):
            if arr[j]<arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr
arr=[5,2,3,8,1,6,7]
k=2
print(sort_k(arr,k))'''

# input = [2,5,8,6,3,1,9,4,7],k=4 find the kth largest element.
#o/p : 6
'''def k_largest(arr,k):
    org_k = k
    for j in range(len(arr)-1): #run upto k times as in each step the array sorts the largest to last
        swapped=False
        k-=1
        for i in range(len(arr)-1-j):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped=True
        if swapped==False or k==0:
            break
        print(arr)
    return arr[-org_k]
    
arr=[2,5,8,6,3,1,9,4,7]
k=4
print(k_largest(arr,k))'''

#find ip=['c','e','a','b','f'] o/p:['a','b','c','e','f']
'''def alpha_sort(chars):
    n=len(chars)
    for j in range(n-1):
        swapped = False
        for i in range(n-1-j):
            if chars[i] > chars[i+1]:
                chars[i],chars[i+1]=chars[i+1],chars[i]
                swapped=True
        if swapped==False:
            break
        print(chars)

    return chars
chars=['c','e','a','b','f']
print(alpha_sort(chars))'''

#find i/p = [[2,8],[5,1],[1,3],[7,3]] o/p:[[5,1],[1,3],[7,3],[2,8]]
'''def matrix_sort(matrix):
    n = len(matrix)
    for _ in range(n - 1):
        for i in range(n - 1):
            if matrix[i][1] > matrix[i + 1][1]:
                matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
    return matrix

matrix = [[2, 8], [5, 1], [7, 3], [1, 3]]
print("Sorted matrix:", matrix_sort(matrix)) '''

#i/p=["zebra","cet","apple","cat"] o/p:['apple','cat','cet','zebra']
'''def lexographic_sort(strings):
    n=len(strings)
    for _ in range(n-1):
        for i in range(n-1):
            if strings[i][0]>strings[i+1][0]: #if both first letter different
                strings[i],strings[i+1]=strings[i+1],strings[i]
            elif strings[i][0]==strings[i+1][0]: #if first same 
                if strings[i][1]>strings[i+1][1]: #if second letter greater
                    strings[i],strings[i+1]=strings[i+1],strings[i]
    return strings
strings=["zebra","car","apple","cat"]
print(lexographic_sort(strings))'''

#i/p : [[4,13,12],[8,10,5],[7,9,20],[14,8,3]], sort the matrix wrt prime no
#o/p:  [[14,8,3],[8,10,5],[7,9,20],[4,13,12]].
'''primes = []
matrix = [[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
def isprime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def matrix_prime_sort(primes):
    n = len(matrix)
    for _ in range(n - 1):
        for i in range(n - 1):
            if primes[i] > primes[i + 1]:
                primes[i], primes[i + 1] = primes[i + 1], primes[i]
                matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
    return matrix


r = len(matrix)
c = len(matrix[0])
for i in range(r):
    for j in range(c):
        if isprime(matrix[i][j]):
            primes.append(matrix[i][j])
print(primes)

print("Sorted matrix:", matrix_prime_sort(primes))'''

#i/p: "An apple a day keeps doctor away" , sort the words based on the its lenght
# o/p: "a an day away apple keeps doctor"
'''sentence = "an apple a day keeps doctor away"
words=sentence.split()
lenghts = [len(word) for word in words]
def length_sort(lengths):
    n=len(lenghts)
    for _ in range(n-1):
        for i in range(n-1):
            if lengths[i]>lenghts[i+1]:
                lengths[i],lengths[i+1]=lengths[i+1],lengths[i]
                words[i],words[i+1]=words[i+1],words[i]
    return words
print(" ".join(length_sort(lenghts)))'''


#i/p : [7,2,6,3,6,7,7,2,2,2]
#o/p : [3,6,6,7,7,7,2,2,2,2]
'''nums = [7,10,10,2,6,3,6,7,7,2,2,2]
d ={}
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
def frequency_sort(nums):
    n=len(nums)
    for _ in range(n-1):
        for i in range(n-1):
            if d[nums[i]]>d[nums[i+1]]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
    return nums

print(frequency_sort(nums))'''

#above question using bucket sort
'''nums = [7,10,10,2,6,3,6,7,7,2,2,2]
d ={}
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
max_freq = max(d.values())
bucket = [[] for _ in range(max_freq+1)]
print(bucket)
# for item in d.items():
#     print(item)
for num,freq in d.items():
    bucket[freq].append(num)
# print(bucket)
res=[]
for i in range(len(bucket)):
    for j in bucket[i]:
        res.extend([j]*i)
print(res)
        '''
#key

'''a=[(7, 3, 4), (2, 4), (6,), (3,2,6)]
a.sort(key=len) #sorts based on length 
print(a) #[(6,), (2, 4), (7, 3, 4), (3, 2, 6)]'''

'''def qwer(x):
    return len(x)
a=[(7, 3, 4), (2, 4), (6,), (3,2,6)]
a.sort(key=len) #sorts based on length
print(a) #[(6,), (2, 4), (7, 3, 4), (3, 2, 6)]'''

'''def qwer(x):
    return x[0]
a=[(7, 3, 4), (2, 4), (6,), (3,2,6)]
a.sort(key=qwer) #sorts based on value of first index value
print(a) #[(2, 4), (3, 2, 6), (6,), (7, 3, 4)]'''

'''def isprime(x):
    for num in x:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            return num
    return 0
a=[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
a.sort(key=isprime) #sorts based on value of prime numbers
print(a) #[(2, 4), (3, 2, 6), (6,), (7, 3, 4)]'''








    
    






