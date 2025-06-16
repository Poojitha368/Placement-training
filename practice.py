'''def subsequence(i,s=[]):
    if i==len(arr):
        if len(s) != 0:
            print(s)
        return 
    s.append(arr[i])
    subsequence(i+1,s)
    s.pop()
    subsequence(i+1,s)
    
arr=[1,2,3]
subsequence(0)'''

#print all subsequences with sum k
def subsequence_sum_k(i,s=[],sum=0,k=2):
    if i==len(arr):
        if sum == k:
            print(s)
        return 
    s.append(arr[i])
    sum += arr[i]
    subsequence_sum_k(i+1,s,sum,k)
    s.pop()
    sum -= arr[i]
    subsequence_sum_k(i+1,s,sum,k)
    
arr=[1,2,1]
subsequence_sum_k(0)

#print only one subsequence with sum k
def subsequence_sum_k(i=0,s=[],csum=0,k=2):
    if i==len(arr):
        if csum == k:
            print(s)
            return True
        return 
    s.append(arr[i])
    csum += arr[i]
    if subsequence_sum_k(i+1,s,csum,k) == True:
        return True
    s.pop()
    csum -= arr[i]
    if subsequence_sum_k(i+1,s,csum,k) == True:
        return True
    
arr=[1,2,1]
subsequence_sum_k()


#count no of subsequences with sum k
def subsequence_sum_k(i,s=[],sum=0,k=2):
    if i==len(arr):
        if sum == k:
            return 1
        else:
            return 0
        return 
    s.append(arr[i])
    sum += arr[i]
    l=subsequence_sum_k(i+1,s,sum,k)
    s.pop()
    sum -= arr[i]
    r=subsequence_sum_k(i+1,s,sum,k)
    return l+r
    
arr=[1,2,1]
print(subsequence_sum_k(0))


# QuickSort implementation
def partition(arr, low, high):
    pivot = arr[low]
    left = low
    right = high
    while left < right:
        while arr[left] <= pivot and left <= right:
            left += 1
        while arr[right] > pivot and left <= right:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right
        
        
def quicksort(arr, low, high):
    if low<high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)

arr = [4,6,2,5,7,9,1,3]
quicksort(arr,0,7)
print(arr)