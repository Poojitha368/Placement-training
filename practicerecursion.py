# def all_permutations_swap(idx,arr):
#     if idx == len(arr):
#         print(arr)
#         return
#     for i in range(idx,len(arr)):
#         arr[idx],arr[i] = arr[i],arr[idx]
#         all_permutations_swap(idx+1,arr)
# arr = [1,2,3]
# all_permutations_swap(0,arr)


'''def n_queens(j):
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
print(ans)'''


'''class Solution(object):
    def partition(self, s):
        ds=[]
        ans=[]
        def partitionHelper(idx):
            if idx == len(s):
                ans.append(list(ds))
                return
            for i in range(idx,len(s)):
                if is_palindrome(idx,i):
                    ds.append(s[idx:i+1])
                    partitionHelper(i+1)
                    ds.pop()
        def is_palindrome(left,right):
            while left<=right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        partitionHelper(0)
        return ans'''

        
'''
class Solution:
    def solveSudoku(self, board):
        n = 9
        
        
        def isValid(row, col, ch):
            row, col = int(row), int(col)
            
            for i in range(9):
                
                if board[i][col] == ch:
                    return False
                if board[row][i] == ch:
                    return False
                
                if board[3*(row//3) + i//3][3*(col//3) + i%3] == ch:
                    return False
            
            return True
            
        def solve(row, col):
            if row == n:
                return True
            if col == n:
                return solve(row+1, 0)
            
            if board[row][col] == ".":
                for i in range(1, 10):
                    if isValid(row, col, str(i)):
                        board[row][col] = str(i)
                        
                        if solve(row, col + 1):
                            return True
                        else:
                            board[row][col] = "."
                return False
            else:
                return solve(row, col + 1)
            
            
        
        solve(0, 0)
		
		#do upvote if it helps.
'''