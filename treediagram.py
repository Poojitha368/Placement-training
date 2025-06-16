from collections import deque

class node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def insert(root, x):
    if root is None:
        return node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root

def get_height(root):
    if root is None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))

def print_tree(root):
    if root is None:
        return

    height = get_height(root)
    max_width = 2 ** height - 1
    queue = deque([(root, 1, max_width // 2)])

    levels = [[] for _ in range(height)]

    while queue:
        node, level, pos = queue.popleft()
        levels[level - 1].append((pos, node.data if node else None))
        if level < height:
            if node:
                queue.append((node.left, level + 1, pos - 2 ** (height - level - 1)))
                queue.append((node.right, level + 1, pos + 2 ** (height - level - 1)))
            else:
                queue.append((None, level + 1, pos - 2 ** (height - level - 1)))
                queue.append((None, level + 1, pos + 2 ** (height - level - 1)))

    for i in range(height):
        line = ""
        curr_level = levels[i]
        last_pos = 0
        for pos, val in curr_level:
            spaces = pos - last_pos
            line += " " * spaces
            line += str(val) if val is not None else " "
            last_pos = pos + 1
        print(line)

        # draw branches
        if i < height - 1:
            branch_line = ""
            last_pos = 0
            for pos, val in curr_level:
                left = pos - 1
                right = pos + 1
                branch_line += " " * (left - last_pos)
                branch_line += "/" if val is not None else " "
                branch_line += " "
                branch_line += "\\" if val is not None else " "
                last_pos = right + 1
            print(branch_line)


root=None
root = insert(root,10)
root = insert(root,5)
root = insert(root,20)
root = insert(root,2)
root = insert(root,8)
root = insert(root,7)
root = insert(root,9)
print_tree(root)