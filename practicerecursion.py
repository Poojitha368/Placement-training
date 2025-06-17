# def all_permutations_swap(idx,arr):
#     if idx == len(arr):
#         print(arr)
#         return
#     for i in range(idx,len(arr)):
#         arr[idx],arr[i] = arr[i],arr[idx]
#         all_permutations_swap(idx+1,arr)
# arr = [1,2,3]
# all_permutations_swap(0,arr)


def n_queens(j):
    if j>=n:
        ans.append(["".join(row) for row in board])
        return
    for i in range(n):
        if left_row[i] != True and lower_diagonal[i+j]!=True and upper_diagonal[n-1+i-j] != True:
            board[i][j] = 'Q'
            left_row[i] = True
            lower_diagonal[i+j] = True
            upper_diagonal[n-1+i-j] = True
        
            n_queens(j+1)
            board[i][j]='.'
            left_row[i]=False
            lower_diagonal[i+j] = False
            upper_diagonal[n-1+i-j]=False

ans = []
n=4
left_row = [False]*n
lower_diagonal = [False]*(2*n-1)
upper_diagonal = [False]*(2*n-1)
board = [['.' for _ in range(n)] for _ in range(n)]
n_queens(0)
print(ans)