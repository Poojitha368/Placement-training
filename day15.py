'''def find_value_expression(a):
    s = a.split(',')
    print(s)
    stack = []
    for c in s:
        if c.isdigit():
            stack.append(c)
        else:
            op1 = int(stack.pop())
            op2 = int(stack.pop())
            if c == '+':
                res = op1 + op2
            elif c == '-':
                res = op2 - op1
            elif c == '*':
                res = op1 * op2
            else:
                res = op2/op1
            stack.append(res)
    return stack[-1]

a = '15,3,+,6,2,-,*'
print(find_value_expression(a))'''


# 🟢 Beginner Level (Get comfortable with stack basics):
# Valid Parentheses
# 📍 LeetCode #20 – Link
# ✔️ Use stack to check for matching brackets.

# Implement Stack using Queues / Queue using Stacks
# 📍 LeetCode #225 / #232 – Link

# Min Stack
# 📍 LeetCode #155 – Link
# ✔️ Track min value at every state.

# Reverse a Stack
# 💡 Use recursion to reverse elements in a stack.

# Next Greater Element I
# 📍 LeetCode #496 – Link

# 🟡 Intermediate Level (Pattern-based and sliding problems):
# Next Greater Element II
# 📍 LeetCode #503 – Use circular array logic.

# Daily Temperatures
# 📍 LeetCode #739 – Link

# Largest Rectangle in Histogram
# 📍 LeetCode #84 – Link
# ✔️ Classic stack problem on area optimization.

# Remove K Digits
# 📍 LeetCode #402 – Link
# ✔️ Greedy + stack.

# Decode String
# 📍 LeetCode #394 – Link

# 🔴 Advanced Level (Combines stacks with DP/graphs/trees):
# Maximal Rectangle
# 📍 LeetCode #85 – Based on histogram logic.

# Asteroid Collision
# 📍 LeetCode #735 – Link

# Basic Calculator I & II
# 📍 LeetCode #224, #227 – Parse string expressions using stacks.

# Expression Evaluation
# ✔️ Like the postfix one you did! Try supporting:

# Prefix

# Infix

# With variables

# Online Stock Span
# 📍 LeetCode #901 – Link


#ip: "(({}))" valid
'''def valid_parenthesis(s):
    stack = []
    for b in s:
        if stack and ((stack[-1]=='(' and b==')') or (stack[-1]=='{' and b=='}') or (stack[-1]=='[' and b==']')):
            stack.pop()
        else:
            stack.append(b)
        print(stack)
    return len(stack)==0
s = '((({})))]'
print(valid_parenthesis(s))'''

#find which index have error



#i/p: [4,1,2],[2,1,3,4]
#o/p:[-1,3,3]




class node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None
    # def inorder(self,root):
    #     if root == None:
    #         return 
    #     self.inorder(root.left)
    #     print(root.data,end=" ")
    #     self.inorder(root.right)
    # def preorder(self,root):
    #     if root==None:
    #         return
    #     print(root.data,end=" ")
    #     self.preorder(root.left)
    #     self.preorder(root.right)
    def sum_all_nodes(self,root):
        if root == None:
            return 0
        return root.data+self.sum_all_nodes(root.left)+self.sum_all_nodes(root.right)
    def sum_all_even_nodes(self,root):
        if root == None:
            return 0
        if root.data % 2 == 0:
            return root.data + self.sum_all_even_nodes(root.left)+self.sum_all_even_nodes(root.right)
        else:
            return self.sum_all_even_nodes(root.left)+self.sum_all_even_nodes(root.right)
    def height(self,root):
        if root == None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    def search_in_tree(self,root,t):
        if root == None:
            return
        if root.data == t:
            return root.data
        elif root.data > t:
            return self.search_in_tree(root.left,t)
        else:
            return self.search_in_tree(root.right,t)
        
    

root = node(10)
root.left = node(5)
root.right = node(20)
root.left.right = node(8)
root.left.left = node(2)
# root.inorder(root)
# root.preorder(root)
print(root.sum_all_nodes(root))
print(root.sum_all_even_nodes(root))
print(root.height(root))
print(root.search_in_tree(root,2))