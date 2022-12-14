  # ** binary search is structure of sorted numbers...
  # ** in this DS each left side of root node has less than root 
  # ** and each right side of root node has more than root !
  # TODO we want 2 operation : 1.search  2.insert 3.deletion



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
    self.tree = self.makeTree(arr)
    self.tmp = list(arr)
    
  def makeTree(self,arr):
    tmpList = []
    for item in arr:
      tmpList.append(Node(item)) 
    return tmpList


x = BinarySearch([10, 11 , 43 , 13 , 32 , 19 , 20 , 9 , 5, 1])
# x.printTree()

      
