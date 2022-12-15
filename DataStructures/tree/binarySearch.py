import random
  
  # ** binary search is structure of sorted numbers...
  # ** in this DS each left side of root node has less than root 
  # ** and each right side of root node has more than root !
  # TODO we want 3 operation : 1.search  2.insert 3.deletion



  # ! in this case that we are using array 
  # ! we have an problem to create an bsd 

  ## ? possible algorithm i think must work is this that we know R is a mainRoot
  ## ? then we split list to the min of R and max of R
  ## ? then catch random item in list and append to the R.left
  ## ? then for R.left we split list to the max of R.left and min of R.left
  ## ? then catch random number and add it to the r.left.left 
  ## ? JUST like this recursively do this until tree make appeared!

  
class Node:
  def __init__(self, value):
    self.value = value
    self.parent = None
    self.right = None
    self.left = None



class BinarySearch:
  def __init__(self, arr):
    # self.tree = self.makeTree(arr)
    self.tree = []
    self.tmp = list(arr)
    self.mainRoot = None
    self.lTmp = None
    self.rTmp = None
    self.create()

  def create(self, root=0):
    if root == 0:
      root = Node(self.tmp[0])
      self.mainRoot = root
      self.tmp.remove(self.tmp[0])
    
    if root == None:
      return
    
    lMin = self.getMinThan(root.value , self.lTmp)
    lMax = self.getMaxThan(root.value , self.rTmp)
    self.lTmp = lMin
    self.rTmp = lMax
    print(lMax)
    print(lMin)
    if len(lMax) != 0:
      randomNumRight = random.randint(0,len(lMax) - 1)
      r = lMax[randomNumRight]
      print('this is right' , r)
      root.right = Node(r)      
      self.rTmp.remove(r)
    if len(lMin) != 0:
      randomNumLeft = random.randint(0,len(lMin) - 1)
      l = lMin[randomNumLeft]
      root.left = Node(l)
      self.lTmp.remove(l)
    self.tree.append(root)
    self.create(root.left)
    self.create(root.right)

    
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

    print(root.value)
    print("its left side node")
    self.show(root.left)
    print("its right side node")
    self.show(root.right)

  def makeTree(self,arr):
    tmpList = []
    for item in arr:
      tmpList.append(Node(item)) 
    return tmpList


x = BinarySearch([10, 11 , 43 , 13 , 32 , 19 , 20 , 9 , 5, 1])

# x.show()
print(x.mainRoot.left.left.value)
# print(random.randint(0,10))      
