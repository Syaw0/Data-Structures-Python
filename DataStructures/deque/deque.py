class Deque:
  def __init__(self):
    self.__storage = []
    self.__max = 10

  def insertBefore(self, data):
    if self.__checkForInsert():return
    self.__storage.insert(0, data)
  
  def insertAfter(self, data):
    if self.__checkForInsert():return
    self.__storage.append(data)

  def rmFirst(self):
    if self.__checkForRm():return
    self.__storage.pop(0)

  def rmLast(self):
    if self.__checkForRm():return
    self.__storage.pop(len(self.__storage) - 1 )
  
  def __checkForInsert(self):
    if len(self.__storage) == self.__max :
      return True
    return False

  def __checkForRm(self):
    if len(self.__storage) == 0:
      return True
    return False

  def getStorage(self):
    return self.__storage
  

x = Deque()

x.insertAfter(19)
x.insertAfter(20)
x.insertAfter(21)
x.insertAfter(22)

x.insertBefore(1)
x.insertBefore(2)
x.insertBefore(4)
  
print(x.getStorage())

x.rmFirst()
print(x.getStorage())

x.rmLast()
print(x.getStorage())