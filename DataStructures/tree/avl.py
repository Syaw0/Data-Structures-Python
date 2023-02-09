import sys
from binarySearch import BinarySearch
from binarySearch import Node
class AVL(BinarySearch):
    def __init__(self, arr):
        super().__init__(arr)
        self.tmpList =[]

    def balance(self):
        result = self.isBalancedBinary()
        print(result,'result')
        if result==True:
            return True
        print(self.tmpList)
        for i in self.tmpList:
            print('\n',i['node'].value,' IS NOT BALANCED\n')
        node = self.tmpList[0]['node']
        nodeNum = self.tmpList[0]['num']
        print('im using this node ',node.value)
        parent = node.parent
        if parent ==None:
            # TODO Refactor...
            if nodeNum > 0:
                self.rightRotation(node.left)
            else:
                self.leftRotation(node.right)
        else:
            if nodeNum > 0:
                if node.left.right !=None:

                    self.leftRotation(node.left.right)

                    self.rightRotation(node.left)
                else:
                    self.rightRotation(node.left)
            else:
                if node.right.left !=None:
                    self.rightRotation(node.right.left)
                    self.leftRotation(node.right)
                else:
                    self.leftRotation(node.right)
        print(self.tmpList)
        self.tmpList = []
        print(self.tmpList)
        self.balance()

    def rightRotation(self,node):
        parent = node.parent
        parent.left = node.right
        if node.right != None:
            node.right.parent=parent
        node.parent = parent.parent
        if parent.parent !=None:
            if parent.parent.left == parent:
                parent.parent.left = node
            else:
                parent.parent.right = node
        parent.parent = node
        node.right = parent

    def leftRotation(self,node):

        parent = node.parent
        parent.right = node.left
        if node.left != None:
            node.left.parent=parent
        node.parent = parent.parent
        if parent.parent != None:
            if parent.parent.left == parent:
                parent.parent.left = node
            else:
                parent.parent.right = node
        parent.parent = node
        node.left = parent

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
        # print(node.value,height.height,leftNodeHeight.height , rightNodeHeight.height,'abs:',abs(leftNodeHeight.height - rightNodeHeight.height <= 1))
        height.height = max(leftNodeHeight.height, rightNodeHeight.height) + 1
        if abs(leftNodeHeight.height - rightNodeHeight.height )<= 1:
            return l and r
        
        print(node.value,'its not balanced')
        self.tmpList.append({"node":node,"num":leftNodeHeight.height - rightNodeHeight.height})
        return False

    def search(self,value,node=0):
        if node==0:
            node= self.tree[0]
        if node == None:
            return False
        if node.value == value:
            print('found ',node.value)
            return node
        
        if   value > node.value:
            return self.search(value,node.right)
        else:
            return self.search(value,node.left)
    def delete(self,value):
        node = self.search(value)
        if node == False:
            return 'can not found element to delete it'
        print(node)
        if node.left ==None and node.right == None:
            if node.parent.left ==node:
                node.parent.left = None
            else:
                node.parent.right = None
            
            self.tree=self.removeNodeFromList(node)
        elif node.left!=None and node.right != None:
            if node.right.left == None:
                node.left.parent = node.right
                node.right.left = node.left
                node.right.parent = node.parent #*
                if node.parent.left ==node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                
            else:

                targetNode = node.right
                while True:
                    if targetNode.left == None:
                        break
                
                    targetNode = targetNode.left

                if  targetNode.left.right !=None:
                    targetNode.parent.left = targetNode.right
                    targetNode.right.parent = targetNode.parent
                targetNode.parent = node.parent 
                if node.parent.left ==node :
                    node.parent.left =targetNode
                else:
                    node.parent.right =targetNode
                targetNode.left = node.left
                targetNode.right = node.right
                node.right.parent = targetNode
                node.left.parent = targetNode
            self.tree=self.removeNodeFromList(node)
        else:
            if node.left == None :
                if node.parent.left ==node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.right.parent = node.parent
                self.tree=self.removeNodeFromList(node)
                
            else:
                if node.parent.left ==node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                node.left.parent = node.parent
                self.tree= self.removeNodeFromList(node)
        self.balance()

    def removeNodeFromList(self,node):
        newList = []
        for i in  self.tree :
            if i.value != node.value:
                newList.append(i)
        return newList

        
    def insert(self,value,node=0):
        if node==0:
            searchResult = self.search(value)
            if searchResult!=False :
                
                return 'the value exist'
            else:
                node = self.tree[0]
        
            
        
        if value>node.value:
            if node.right != None:
                self.insert(value,node.right)
            else:
                node.right = Node(value)
                node.right.parent = node
                self.tree.append(node)
                self.balance()
        else:
            if node.left != None:
                self.insert(value,node.left)
            else:
                node.left = Node(value)
                node.left.parent = node
                self.tree.append(node)
                self.balance()
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.value)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)
        
        

class NodeHeight:
    def __init__(self):
        self.height = 0


x = AVL([23,34,10,4,11,44,55,19])
x.printHelper(x.tree[0],'',True)
if x.balance() != True:
    x.printHelper(x.tree[0],'',True)



x.insert(123)
x.printHelper(x.tree[0],'',True)
x.insert(5)
x.printHelper(x.tree[0],'',True)
x.insert(1)
x.printHelper(x.tree[0],'',True)
x.insert(32)
x.printHelper(x.tree[0],'',True)
x.insert(30)
x.printHelper(x.tree[0],'',True)
print('\n\n')
print('start DELETING \n\n',123)
x.delete(123)
x.printHelper(x.tree[0],'',True)
print('start DELETING \n\n',19)
x.delete(19)
x.printHelper(x.tree[0],'',True)
print('start DELETING \n\n',10)
x.delete(10)
x.printHelper(x.tree[0],'',True)