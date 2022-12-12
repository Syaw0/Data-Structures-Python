class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self, tree):
        self.tmpTree = tree
        self.tree = []
        self.tmp = []
        self.makeTree()

    def makeTree(self):
        for item in self.tmpTree:
            tmpNode = Node(item)
            self.tree.append(tmpNode)

        for index in range(0, len(self.tree) - 1):
            left = index * 2 + 1
            right = index * 2 + 2
            if left < len(self.tmpTree):
                self.tree[index].left = self.tree[left]
            if right < len(self.tmpTree):
                self.tree[index].right = self.tree[right]

    def inOrderTraverse(self, root=0):
        if root == 0:
            root = self.tree[0]

        if root.left != None:
            self.inOrderTraverse(root.left)

        self.tmp.append(root.value)

        if root.right != None:
            self.inOrderTraverse(root.right)

    def preOrderTraverse(self, root=0):
        if root == 0:
            root = self.tree[0]

        self.tmp.append(root.value)

        if root.left != None:
            self.preOrderTraverse(root.left)

        if root.right != None:
            self.preOrderTraverse(root.right)

    def postOrderTraverse(self, root=0):
        if root == 0:
            root = self.tree[0]
        if root.left != None:
            self.postOrderTraverse(root.left)

        if root.right != None:
            self.postOrderTraverse(root.right)
        self.tmp.append(root.value)


