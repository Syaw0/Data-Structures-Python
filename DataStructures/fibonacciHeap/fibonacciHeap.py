
## ! this structure still have an issue !!
## TODO fix tree child issue 
## TODO work on delete and decrease key methods!


import math

class FibonacciTree:
  def __init__(self,value,children):
    self.value = value 
    if children is not None:
      self.child = children
    else:
      self.child = []
    self.order = 0
    self.degree = 0
    self.setDegree()

  def insertAtEnd(self, tree):
    self.child.append(tree)
    self.order += 1
    self.setDegree()


  def setDegree(self):
    if len(self.child) == 0 :return
    self.degree = 0
    for child in self.child :
      self.degree += len(child) # we must only use array for children


class FibonacciHeap:
  def __init__(self):
    self.trees = []
    self.least = None
    self.count = 0

  def insertNode(self, value , children):
    newTree = FibonacciTree(value, children)
    self.trees.append(newTree)
    if self.least is None or value < self.least.value :
      self.least = newTree
    self.count += 1

  def getMin(self):
    if self.least is None:
      return None
    return self.least.value

  def extractMin(self):
    smallest = self.least
    if smallest is not None:
      for child in smallest.child:
        self.trees.append(child)
      self.trees.remove(smallest)
      if self.trees == []:
        self.least = None
      else:
        self.least = self.trees[0]
        self.consolidate()
      self.count -= 1
      return smallest.value

  def findMax(self):
    max = 0
    for tree in self.trees:
      if hasattr(tree,'degree') == True:
        if max < tree.degree:
          max = tree.degree
        continue
      if max < len(tree):
        max = len(tree)
    return max



  def show(self):
    print(self.trees)
    s = {}
    x = 0
    for i in self.trees:
      tmp = {}
      if self.isItObject(i) == True:
        tmp['root'] = i.value
        tmp['child'] = i.child
      else:
        tmp['root'] = i[0]
        tmp['child'] = i[1:len(i)]
      s[x] = tmp
      x += 1

    for i in s :
      print(s[i])

  def isItObject(self,obj):
    if hasattr(obj, "degree") == True:
      return True
    else:
      return False

  def getKey(self,obj):
    if self.isItObject(obj) == True:
      return obj.value
    else:
      return obj[0]

  def union(self,min,max):
    # maxIndex = self.trees.index(max)
    # minIndex =self.trees.index(min)
    if self.isItObject(min) == True:
      min.insertAtEnd(max)
    else:
      min.append(max)
    self.trees.remove(max)
    
    


  def consolidate(self): 

    aux = (self.findMax() + 1) * [None]
    for tree in self.trees:
      x = tree
      d = None
      if self.isItObject(x) == True:
        d = x.degree
      else:
        d = len(x)
      while aux[d] != None:
        y = aux[d]
        yKey = self.getKey(y)
        xKey = self.getKey(x)
        print('hello',x,y)
        if xKey > yKey:
          self.union(y,x)
          print("union together and y is root",x,y)
        elif xKey < yKey:
          self.union(x,y)
          print("union together and x is root" , x,y)
        aux[d] = None
      aux[d] = x

x = FibonacciHeap()

x.insertNode(1,[[2,3],[4,5,6]])
x.insertNode(32,[[34,59],[42,45,90,100]])
x.insertNode(3,[[34,59],[42]])
x.insertNode(5,[[34,59]])
x.show()
x.extractMin()
x.show()
# x.show()

