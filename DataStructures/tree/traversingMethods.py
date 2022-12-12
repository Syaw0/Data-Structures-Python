class Node:
  def __init__(self,value):
    self.left = None
    self.right = None
    self.value = value



class Tree:
  def __init__(self,tree):
    self.tmpTree = tree
    self.tree = []
    self.tmp = []
    self.makeTree()

  def makeTree(self):
    for item in self.tmpTree:
      tmpNode = Node(item)
      self.tree.append(tmpNode)
    
    for index in range(0,len(self.tree) - 1):
      left = index * 2 + 1
      right = index * 2 + 2
      if left < len(self.tmpTree): 
        self.tree[index].left = self.tree[left]
      if right < len(self.tmpTree):
        self.tree[index].right = self.tree[right]
    

  def inOrderTraverse(self,root=0):
    if root == 0:
      root = self.tree[0]
    
  
    if root.left != None:
      print('this is left',root.left.value)
      self.inOrderTraverse(root.left)

    self.tmp.append(root.value)
    
    if root.right != None:  
      print('this is right',root.right.value)
      self.inOrderTraverse(root.right)


  def preOrderTraverse(self, root=0):
    if root == 0:
      root = self.tree[0]
    
  

    self.tmp.append(root.value)

    if root.left != None:
      print('this is left',root.left.value)
      self.preOrderTraverse(root.left)
    
    if root.right != None:  
      print('this is right',root.right.value)
      self.preOrderTraverse(root.right)

  def postOrderTraverse(self , root=0):
    if root == 0:
      root = self.tree[0]
    if root.left != None:
      print('this is left',root.left.value)
      self.postOrderTraverse(root.left)
    
    if root.right != None:  
      print('this is right',root.right.value)
      self.postOrderTraverse(root.right)
    self.tmp.append(root.value)


x = Tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
x.postOrderTraverse()
print(x.tmp)
