class Stack:
  def __init__(self):
    self.__storage = []
    self.__top = -1
    self.__max = 30
    print('successfully created a stack')

  def permissionForPop(self):
    if self.__top == -1 :
      return False
    return True

  def permissionForPush(self):
    if self.__top == self.__max :
      print("stack is overflowed :D")
      return False
    return True

  def push(self,item):
    if self.permissionForPush() :
      self.__storage.append(item)
      self.__top += 1
      print('add this item: %s ' % item)

  def pop(self):
    if self.permissionForPop() :
      print('delete this item:%s'% self.__storage.pop())
      self.__top -= 1

  def stackSize(self):
    return self.__top + 1

  def getStack(self):
    return self.__storage

  def peek(self):
    return self.__storage[self.__top]

