from binarySearch import BinarySearch

class AVL(BinarySearch):
    def __init__(self, arr):
        super().__init__(arr)

    def isBalancedBinary(self, node = 0, height= 0):
        # * If the difference between the two sides of a node in a tree is equal to one
        # * we call this binary tree a balanced binary...

        if node == 0 :
            node = self.tree[0]
            height = NodeHeight()
        
        rightNodeHeight = NodeHeight()
        leftNodeHeight =NodeHeight()

        if node == None:
            return True
        
        # recursively call to check all the elements...
        l = self.isBalancedBinary(node.left , leftNodeHeight)
        r = self.isBalancedBinary(node.right , rightNodeHeight)

        height.height = max(leftNodeHeight.height, rightNodeHeight.height) + 1
        if abs(leftNodeHeight.height - rightNodeHeight.height <= 1):
            return l and r
        return False
        

class NodeHeight:
    def __init__(self):
        self.height = 0


x = AVL([23,34,10,4,11,44,55,19])
x.show()
print(x.isBalancedBinary())