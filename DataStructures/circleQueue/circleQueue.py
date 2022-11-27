class CircleQueue:
  def __init__(self):
    self.__max = 5
    self.__front = -1
    self.__rear = -1
    self.__storage = []

  
  def enqueue(self,data):
    if self.checkForEnqueue() : return
    if(len(self.__storage) == 0): self.__front = 0
    if(self.__max - 1 == self.__rear):
      self.__rear = 0
      self.__storage.append(data)
      return
    self.__rear+=1
    self.__storage.append(data)
  
  def dequeue(self):
    if self.checkForDequeue() : return
    if len(self.__storage) == 1 :
      self.__front = -1
      self.__rear = -1
      self.__storage.pop(0)
      return
    self.__storage.pop(0)
    if self.__front == self.__max - 1 :
      self.__front = 0
    else:
      self.__front += 1

  def checkForEnqueue(self):
    if len(self.__storage) == self.__max:
      return True
    return False

  def checkForDequeue(self):
    if(len(self.__storage) == 0) :
      return True
    return False

  def showQueue(self):
    return self.__storage,self.__rear,self.__front

  def peek(self,index):
    if index >=0 and index <= self.__max - 1 :
      if index <= len(self.__storage) - 1 :
        return self.__storage[index]
    return False

