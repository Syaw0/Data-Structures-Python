import random
  
  # ** binary search is structure of sorted numbers...
  # ** in this DS each left side of root node has less than root 
  # ** and each right side of root node has more than root !

  # TODO refactor method on line 67(deletion)
  # ? can you write a better algorithm for create ? line(138) and
  # ? i think this is huge duplication -_-

class Node:
  def __init__(self, value):
    self.value = value
    self.parent = None
    self.right = None
    self.left = None



class BinarySearch:
  def __init__(self, arr):
    self.tree = []
    self.tmp = list(arr)
    self.mainRoot = None
    self.create()

  def search(self, key ,root=0 ):
    # * look we are recursively look to the tree and because tree is 
    # * BSD easily we found that if its exist its return node else return None
    if root == 0 :
      root = self.mainRoot
    if root == None:
      return 
    
    if root.value == key:
      print(root.value,'founded')
      return root
    if root.value >  key:
      return self.search(key, root.left)
    else:
      return self.search(key, root.right)    
    
    
  def insert(self ,key , root=0):
    if root == 0:
      root = self.mainRoot
    if root == None:
      print("we reach the element")
      return Node(key)
    if root.value == key:
      return root
    if root.value > key:
      root.left = self.insert(key, root.left)
      if root.left != None:
        root.left.parent = root
    else:
      root.right = self.insert(key, root.right)
      if root.right != None:
        root.right.parent = root
    return root


  def getMin(self,node):
    current = node
    while current.left != None:
      current = current.left
    return current #* we sure this is leaf element

  def deletion(self, key):
    node = self.search(key)
    if node == None :
      return 'no such node exist'

    if node.left == None and node.right == None:
      if node.parent.value > node.value:
        node.parent.left = None
      else:
        node.parent.right = None
    elif node.left != None and node.right != None:
      minNode = self.getMin(node.right)
      if minNode.right == None:
        # here is must easy because min node is leaf
        minNode.parent.left = None
        if node.parent.value > node.value:
          node.parent.left = minNode
        else:
          node.parent.right = minNode
        minNode.left = node.left
        minNode.right = node.right
        minNode.left.parent = minNode
        minNode.right.parent = minNode

      else:
        # in here we have 2 case :
        if minNode.parent.value > minNode.value:
          # case 1: node is smaller than parent
          minNode.parent.left = minNode.right
          minNode.parent = node.parent
          if node.parent.value > node.value:
            node.parent.left = minNode
          else:
            node.parent.right = minNode
          minNode.left = node.left
          minNode.right = node.right
          minNode.left.parent = minNode
          minNode.right.parent = minNode
        else:
          # case 2: node is bigger than parent and its mean 
          # min node connect to that node we want to remove
          if node.parent.value > node.value:
            node.parent.left = minNode
          else:
            node.parent.right = minNode
          minNode.parent = node.parent
          minNode.left = node.left
          node.left.parent = minNode.parent      
    else:          
      # ! this must refactor!!
      if node.left != None:
        if node.parent.value > node.value:
          node.parent.left = node.left
          node.left.parent = node.parent.left
        else:
          node.parent.right = node.left
          node.left.parent = node.parent.right
      else:
        if node.parent.value > node.value:
          node.parent.left = node.right
          node.right.parent = node.parent.left
        else:
          node.parent.right = node.right
          node.right.parent = node.parent.right


    self.tree.remove(node)


  def create(self, root=0):
    if root == 0:
      root = Node(self.tmp[0])
      self.mainRoot = root
      self.tmp.remove(self.tmp[0])
    if root == None:
      return
    lMin = self.getMinThan(root.value , self.tmp)
    lMax = self.getMaxThan(root.value , self.tmp)
    if len(lMax) != 0:
      randomNumRight = random.randint(0,len(lMax) - 1)
      r = lMax[randomNumRight]
      root.right = Node(r)      
      root.right.parent = root
      lMax.remove(r)
    if len(lMin) != 0:
      randomNumLeft = random.randint(0,len(lMin) - 1)
      l = lMin[randomNumLeft]
      root.left = Node(l)
      root.left.parent = root
      lMin.remove(l)
    self.tree.append(root)
    self.createLeft(root.left , lMin)
    self.createRight(root.right , lMax)

  def createLeft(self,root,arr):
    if root == None :
      return
    lMin = self.getMinThan(root.value ,arr)
    lMax = self.getMaxThan(root.value , arr)
    if len(lMax) != 0:
      randomNumRight = random.randint(0,len(lMax) - 1)
      r = lMax[randomNumRight]
      root.right = Node(r)      
      root.right.parent = root
      lMax.remove(r)
    if len(lMin) != 0:
      randomNumLeft = random.randint(0,len(lMin) - 1)
      l = lMin[randomNumLeft]
      root.left = Node(l)
      root.left.parent = root
      lMin.remove(l)
    self.tree.append(root)
    self.createLeft(root.left , lMin )
    self.createLeft(root.right , lMax)


  def createRight(self , root , arr):
    if root == None :
      return
    lMin = self.getMinThan(root.value ,arr)
    lMax = self.getMaxThan(root.value , arr)
    if len(lMax) != 0:
      randomNumRight = random.randint(0,len(lMax) - 1)
      r = lMax[randomNumRight]
      root.right = Node(r)      
      root.right.parent = root
      lMax.remove(r)
    if len(lMin) != 0:
      randomNumLeft = random.randint(0,len(lMin) - 1)
      l = lMin[randomNumLeft]
      root.left = Node(l)
      root.left.parent = root
      lMin.remove(l)
    self.tree.append(root)
    self.createLeft(root.left , lMin )
    self.createLeft(root.right , lMax)


  def getMaxThan(self,value ,arr):
    tmpList = []
    target = arr
    if arr == None:
      target = self.tmp

    for item in target:
      if item > value:
        tmpList.append(item)
    return tmpList


  def getMinThan(self ,value , arr):
    tmpList = []
    target = arr
    if arr == None:
      target = self.tmp

    for item in target:
      if item < value:
        tmpList.append(item)
    return tmpList

  def show(self , root=0):
    if root == 0:
      root = self.mainRoot
    if root == None :
      return

    print('this is root value',root.value)
    if root.left == None:
      print("left of root is none")
    else:
      print("left of root is : ", root.left.value)

    if root.right == None:
      print("right of root is none")
    else:
      print("right of root is : ", root.right.value)

    self.show(root.left)
    self.show(root.right)

  

x = BinarySearch([10, 11 , 43 , 13 , 32 , 19 , 20 , 9 , 5, 1])
x.insert(21)
x.show()
print("deletion start")
# print(len(x.tree))
x.deletion(19)
# print(len(x.tree))
x.show()