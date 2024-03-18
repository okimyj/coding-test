import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    nodeDict = {}
    def __init__(self, node):
        self.root = node
        self.nodeDict[node.value] = node
    def pushNodes(self, head, left, right):
        if left != '.' :
            node = Node(left)
            self.nodeDict[head].left = node
            self.nodeDict[left] = node
        if right != '.':
            node = Node(right)
            self.nodeDict[head].right = node
            self.nodeDict[right] = node

def preorder(node):
    if node == None:
        return ''
    result = node.value
    result += preorder(node.left)
    result += preorder(node.right)
    return result


def inorder(node):
    if node == None:
        return ''
    result = inorder(node.left)
    result += node.value
    result += inorder(node.right)
    return result


def postorder(node):
    if node == None:
        return ''
    result = postorder(node.left)
    result += postorder(node.right)
    result += node.value
    return result

tree = BinaryTree(Node('A'))
curHead = None
nodeNum = int(sys.stdin.readline())
for i in range(nodeNum) :
    head, left, right = sys.stdin.readline().replace('\n','').split(' ')
    tree.pushNodes(head, left, right)

print(preorder(tree.root))
print(inorder(tree.root))
print(postorder(tree.root))
