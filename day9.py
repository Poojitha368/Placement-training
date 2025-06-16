#search a given element in marix
'''def search_matrix(matrix):
    target = 8
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return i,j
    return False
matrix = [[1,2,3],[6,8,9],[7,10,11]]
print(search_matrix(matrix))'''

# 2  3  7  8
# 9 15 20 22
# 23 26 35 37
# 38 39 42 43
# search element=29 in above matrix
#o(n+logn)
'''def matrix_bs(matrix,t):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        if matrix[i][0]< t and matrix[i][cols-1]>=t:
            return binary_serach(matrix[i],i,t)
def binary_serach(row,rows,t):
    l=0
    r=len(row)-1
    while l<=r:
        m=(l+r)//2
        if row[m]<t:
            l=m+1
        elif row[m]>t:
            r=m-1
        else:
            return m,rows
    return -1
matrix=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
t=35
print(matrix_bs(matrix,t))'''

#o(logn+logm)
'''def matrix_bs(matrix,t):
    u,d = 0,len(matrix)-1
    if u<=d:
        if matrix[]

    
def binary_serach(row,rows,t):
    l=0
    r=len(row)-1
    while l<=r:
        m=(l+r)//2
        if row[m]<t:
            l=m+1
        elif row[m]>t:
            r=m-1
        else:
            return m,rows
    return -1
matrix=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
t=35
print(matrix_bs(matrix,t))'''

#o(logn)
'''def binary_search(matrix,t):
    row,col = len(matrix),len(matrix[0])
    l=0
    r=row*col-1
    while l<=r:
        m=(l+r)//2
        if matrix[m//col][m%col] < t:
            l=m+1
        elif matrix[m//col][m%col] == t:
            return m//col,m%col
        else:
            r=m-1
    return "not found"
t=8
matrix=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
print(binary_search(matrix,t))'''

#capacity = 12 , i/p : [1,2,3,4,5,6,7,8,9,10]
'''def ship_capacity_possible(weights,c):
    d=1
    weightSum=0
    for w in weights:
        if weightSum+w>c:
            weightSum=0
            d+=1
        weightSum += w
    return d
c=5
w = [1,2,3,4,5,6,7,8,9,10]
print(ship_capacity_possible(w,c))'''

#find the capacity for given days
# i/p : [1,2,3,4,5,6,7,8,9,10],days=5
'''def ship_capacity_possible(weights,days,c):
    d=1
    weightSum=0
    for w in weights:
        if weightSum+w>c:
            weightSum=0
            d+=1
        weightSum += w
    if d<=days:
        return True
    return False

def binary_search(w,d):
    l=0
    r=sum(w)
    while l<=r:
        m=(l+r)//2
        if ship_capacity_possible(w,d,m):
            r=m-1
        else:
            l=m+1
    return m


d=5
w = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(w,d))'''

# 3  4  6  8
# 5  7  9  10
# 8  12 13 15
# 20 23 26 28
# 30 36 40 45 , target: 23, o/p : (3,1)

'''def search_sorted(mat,t,i,j):
    if i>= len(mat) or j<0:
        return 
    if mat[i][j] < t:
        return search_sorted(mat,t,i+1,j)
    elif mat[i][j] > t:
        return search_sorted(mat,t,i,j-1)
    else:
        return i,j
    
mat = [[3,4,6,8],[5,7,9,10],[8,12,13,15],[20,23,26,28],[30,36,40,45]]
t=23
row=len(mat)
col = len(mat[0])
print(search_sorted(mat,t,0,col-1))'''

#i/p : [2,7,11,15] , t=9 , find the two sum equal to target
'''a=[2,7,11,15]
l=0
r=len(a)-1
t=10
while l<=r:
    if a[l]+a[r] > t:
        r-=1
    elif a[l]+a[r] < t:
        l+=1
    else:
        print("Found")
        break
else:
    print("Not found")'''

#3 sum , i/p:[-1,0,1,2,-1,-4], o/p:[[-1,0,1],[1,2,-1]]











        



