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
  