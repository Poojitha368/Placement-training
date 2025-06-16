# 🌱 Basic Binary Tree Problems
# Inorder, Preorder, Postorder Traversals (Recursive & Iterative)

# Height of a Binary Tree

# Count Total Nodes / Leaf Nodes / Internal Nodes

# Print Level Order Traversal (BFS)

# Mirror a Binary Tree

# Check if Two Trees are Identical

# Sum of All Nodes

# Print all Root-to-Leaf Paths

# Check if a Tree is Symmetric

# Diameter of a Binary Tree

# 🌳 Binary Search Tree (BST) Problems
# Insert / Delete a Node in BST

# Search for a Value in BST

# Find Minimum and Maximum in BST

# Find Inorder Successor / Predecessor

# Check if a Tree is a Valid BST

# Convert Sorted Array to BST

# Lowest Common Ancestor (LCA) in BST

# Kth Smallest / Largest Element in BST

# Find Floor and Ceil in BST

# Find Closest Value in BST

# 🌲 Intermediate Tree Problems
# Convert Binary Tree to Doubly Linked List

# Construct Binary Tree from Inorder and Preorder

# Boundary Traversal

# Zig-Zag (Spiral) Level Order Traversal

# Vertical Order Traversal

# Top View and Bottom View of Tree

# Right / Left View of Tree

# Maximum Path Sum in Binary Tree

# Check if Tree is Height Balanced

# Sum Tree: Check if each node equals sum of left and right subtree

# 🌴 Advanced / Interview-Level Problems
# Serialize and Deserialize a Binary Tree

# Flatten Binary Tree to Linked List (in-place)

# Tree Diameter in O(n)

# Burning Tree (Time to burn all nodes from a target node)

# Nodes at Distance K from Target

# Print Ancestors of a Node

# Count Number of Nodes in a Complete Binary Tree

# Find Duplicate Subtrees

# Construct Tree from Postorder and Inorder

# Maximum Width of a Binary Tree

# 🌿 Bonus Challenges
# Binary Tree to Sum Tree Conversion

# Binary Tree Camera Placement

# Check if a Tree is a Subtree of Another

# Morris Inorder Traversal (No Recursion, No Stack)

# Count Good Nodes in Binary Tree

class node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None

def insert(root,x):
    if root == None:
        return node(x)
    if root.data > x:
        root.left = insert(root.left,x)
    else:
        root.right = insert(root.right,x)
    return root
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)
def no_leaf_nodes(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    return no_leaf_nodes(root.left)+no_leaf_nodes(root.right)
def print_all_paths_from_root_to_leaf(root,paths=[]):
    if root == None:
        return 
    paths.append(root.data) 
    #[10,5,2]

    if root.left == None and root.right == None:
        print(paths)
        paths.pop()
        return 
    #p(10)
    print_all_paths_from_root_to_leaf(root.left,paths)
    # p(5)
    # p(2)
    print_all_paths_from_root_to_leaf(root.right,paths)
    paths.pop()

def level_order_traversal_bfs(root):
    if root == None:
        return "empty tree"
    l=[]
    l.append(root)
    while l:
        curr = l.pop(0)
        if curr.left != None:
            l.append(curr.left)
        if curr.right != None:
            l.append(curr.right)
        print(curr.data,end=" ")
    print()

def bfs_no_of_leaf_nodes(root):
    l = []
    l.append(root)
    cnt=0
    while l:
        curr = l.pop()
        if curr.left == None and curr.right == None:
            cnt+=1
        if curr.left != None:
            l.append(curr.left)
        if curr.right != None:
            l.append(curr.right)
    print("No of leaf nodes",cnt)

d={}
def left_view(root,level=0):
    if root == None:
        return
    if level not in d:
        d[level] = root.data
        print(root.data,end=" ")
    left_view(root.left,level+1)
    left_view(root.right,level+1)

d={}
def right_view(root,level=0):
    if root == None:
        return
    d[level] = root.data
    right_view(root.left,level+1)
    right_view(root.right,level+1)

d={}
#for top view use bfs it will be better
def top_view_dfs(root,left,right):
    if root == None:
        return
    if left not in d: #take the first occured value
        d[left]=root.data
    if right not in d:
        d[right] = root.data #take the first occured value
    top_view_dfs(root.left,left-1,right)
    top_view_dfs(root.right,left,right+1)

def top_view_bfs(root):
    d={}
    c = 0
    l = [(root,c)]
    while l:
        curr,c = l.pop(0)
        if c not in d:
            d[c]=curr.data
        if curr.left != None:
            l.append((curr.left,c-1))
        if curr.right != None:
            l.append((curr.right,c+1))
    return d
def bottom_view_bfs(root):
    d={}
    c = 0
    l = [(root,c)]
    while l:
        curr,c = l.pop(0)
        d[c]=curr.data #only this line change
        if curr.left != None:
            l.append((curr.left,c-1))
        if curr.right != None:
            l.append((curr.right,c+1))
    return d

def least_common_ansestor(root,p,q):
    if root == None:
        return
    if p < root.data and q < root.data:
        least_common_ansestor(root.left,p,q)
    elif p > root.data and q > root.data:
        least_common_ansestor(root.right,p,q)
    return root.data

def height(root):
    if root == None:
        return -1
    return 1 + max(height(root.left),height(root.right))

def check_all_nodes_balanced_or_not(root):
    if root == None:
        return True
    l = height(root.left)
    r = height(root.right)
    if abs(l-r)>1:
        return False
    return check_all_nodes_balanced_or_not(root.left) and check_all_nodes_balanced_or_not(root.right)
    




root=None
root = insert(root,10)
root = insert(root,5)
root = insert(root,20)
root = insert(root,2)
root = insert(root,8)
root = insert(root,7)
root = insert(root,9)
inorder(root)
print(no_leaf_nodes(root))
print(print_all_paths_from_root_to_leaf(root))
level_order_traversal_bfs(root)
bfs_no_of_leaf_nodes(root)
left_view(root,level=0)
print(d)
right_view(root,level=0)
print(d) #print the d keys to get right view , same for left,top,bottom
top_view_dfs(root,left=0,right=0)
print(d)
print(top_view_bfs(root))
print(bottom_view_bfs(root))
print(least_common_ansestor(root,7,9))
print(check_all_nodes_balanced_or_not(root))