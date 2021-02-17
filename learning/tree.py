'''
Tree
- Tree Data Structure
- Tree Traversal
- Application of Tree
- Binary Tree in Python
- Inorder Traversal in Python
- Preorder Traversal in Python
- Postorder Traversal in Python
- Size of Binary Tree in Python
- Maximum in Binary Tree
- Search Binary Tree
- Height of Binary Tree
- Iterative Inorder Traversal
- Iterative Preorder Traversal
- Level Order Traversal
'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.root = key
        

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)

    print(root)