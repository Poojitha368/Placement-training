#input = [2,4,1,5,8,4,1] and max_profit = 8-1 = 7
'''def max_profit(prices):
    min_price=float('inf')
    profit = -1
    for i in range(len(prices)):
        min_price = min(min_price,prices[i])
        profit = max(profit,prices[i]-min_price)
    return profit

# prices=[2,4,1,5,8,4,1]
prices = [13,140,2,5,18,1,4]
print(max_profit(prices))'''

#inputs
#     arr=   [7,6,5,2]
# matrix:    0 1 1 0 1
        #    1 1 0 0 1
        #    0 0 0 1 1
        #    0 1 0 0 0

'''arr=[7,6,5,2,3]
matrix = [[0 ,1 ,1 ,0 ,1],[1,1,0,0,1],[0,0,0,1,1],[0,1,0,0,0]]
row_sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            row_sum += arr[j]*1
    print(row_sum)
    row_sum=0'''

#rat in maze
def rat(a,i,j,n,count):
    if(a[i][j]==0 or i==n or j==n):
        return 0
    if j==n-1 and i==n-1 and a[i][j]==1:
        return 1
    right = rat(a,i,j+1,n,count) #move right
    down = rat(a,i+1,j,n,count) #move down
    return right+down

a = [[1,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1]]
print(rat(a,0,0,4,0))

#land and water
'''def land(a,i,j,n):
    if i==n or j==n or i<0 or j<0 or a[i][j]==0 or a[i][j]==2:
        return 0
    if a[i][j]==1:
        a[i][j]=2
    land(a,i-1,j,n) #top
    land(a,i,j-1,n) #left
    land(a,i+1,j,n) #down
    land(a,i,j+1,n) #right

a=[[1,0,0,1,1],[1,0,0,0,1],[0,0,0,1,0],[1,0,0,0,0],[1,0,0,0,1]]
c=0
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            land(a,i,j,5) #make all neighbours as 2 
            c+=1
print(c)'''


# the tree at (2,5) is burnt and then findout no of unburnt trees
#same as land and water make all connected 1's as 2s and count the 1s.
'''def tree(a,i,j,n):
    if i==n or j==n or i<0 or j<0 or a[i][j]==0 or a[i][j]==2:
        return 0
    if a[i][j]==1:
        a[i][j]=2
    tree(a,i-1,j,n) #top
    tree(a,i,j-1,n) #left
    tree(a,i+1,j,n) #down
    tree(a,i,j+1,n) #right

c=0
a=[[1,0,0,1,1,1],[1,1,1,0,0,0],[0,0,1,1,1,1],[1,1,1,0,0,0],[0,0,0,0,0,1],[1,0,0,1,0,0]]
tree(a,2,5,6)
for i in range(6):
    for j in range(6):
        if a[i][j]==1: 
            c+=1
print(c)'''


#find input = 5 (order of matrix)
# frog location = (2,3)
# danger locations = [(2,1),(4,1),(5,2),(3,5)]
'''def frog(a,i,j,n):
    if (i,j) in a or i>n or j>n:
        return 0
    if j==n and i==n:
        return 1
    return frog(a,i,j+1,n)+frog(a,i+1,j,n)
    
a = [(2,1),(4,1),(5,2),(3,5)]
print(frog(a,2,3,5))'''

#find input = 3  output = 00 01 10 11
# input = 12   output = 0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010
'''import math
res=[]
def allbinary(a,n,s=''):
    if(len(s)==n):
        print(s)
        return
    allbinary(a,n,s+'0')
    allbinary(a,n,s+'1')

a=5
n=math.log(a,1)+1  #to find the no
print(allbinary(a,3,''))
'''

#find all the combinations of of having equal no of opening and closing brackets for n=3
def brackets(n, s="",i=0):
    if i == 2*n:
        return s
    brackets(n,s+"(",i+1)
    brackets(n,s+")",i+1)

n = 2
print(brackets(n))