import random
  
  # ** binary search is structure of sorted numbers...
  # ** in this DS each left side of root node has less than root 
  # ** and each right side of root node has more than root !
  # TODO we want 1 operation :  1.deletion
  # TODO refactor creation method !

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
      print(root.value ,'l')
      root.left = self.insert(key, root.left)
    else:
      print(root.value , 'r')
      root.right = self.insert(key, root.right)
    return root



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
      lMax.remove(r)
    if len(lMin) != 0:
      randomNumLeft = random.randint(0,len(lMin) - 1)
      l = lMin[randomNumLeft]
      root.left = Node(l)
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
      lMax.remove(r)
    if len(lMin) != 0:
      randomNumLeft = random.randint(0,len(lMin) - 1)
      l = lMin[randomNumLeft]
      root.left = Node(l)
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
      lMax.remove(r)
    if len(lMin) != 0:
      randomNumLeft = random.randint(0,len(lMin) - 1)
      l = lMin[randomNumLeft]
      root.left = Node(l)
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