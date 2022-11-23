class Queue:
  def __init__(self):
    self.__max = 5
    self.__storage = []
    self.__length = 0
    self.__front = -1
    self.__rear = -1
  
  def checkForEnqueue(self):
    if self.__rear == self.__max: return False
    return True

  def checkForDequeue(self):
    if self.__front == - 1 : return False
    return True

  def enqueue(self,item):
    if self.checkForEnqueue():
      self.__storage.append(item)
      if self.__length == 0 :self.__front += 1
      self.__rear += 1
      self.__length += 1
      return True
    return False

  def dequeue(self):
    if self.checkForDequeue():
      if self.__front == self.__max : return self.reset()
      self.__storage.pop(0)
      self.__front += 1
      self.__length -= 1

      return True
    return False

  def reset(self):
    self.__front = -1
    self.__length = 0
    self.__rear = -1
    self.__storage.pop(0)


  def peek(self,index=-1):
    if index == -1:return self.__storage[len(self.__storage) - 1 ]
    if index >= len(self.__storage) or index < - 1 : return False
    return self.__storage[index]

  def getStorage(self):
    return self.__storage



x = Queue()

x.enqueue(1)
print(x.getStorage())
x.enqueue(2)
print(x.getStorage())
x.enqueue(3)
print(x.getStorage())
x.enqueue(4)
print(x.getStorage())
x.enqueue(5)
print(x.getStorage())
x.enqueue(6)
print(x.getStorage())
x.dequeue()
print(x.getStorage())

x.dequeue()
print(x.getStorage())

x.dequeue()
print(x.getStorage())
x.dequeue()
print(x.getStorage())
x.dequeue()
print(x.getStorage())

x.dequeue()
print(x.getStorage())


x.enqueue('new')
print(x.getStorage())
