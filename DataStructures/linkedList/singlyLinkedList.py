class Node:
  def __init__(self,data):
    self.__data = data
    self.__next = None
  
  def getData(self):
    return self.__data

  def getNext(self):
    return self.__next

  def setNext(self,nextNode):
    self.__next = nextNode

  def setData(self,newData):
    self.__data = newData
  
class LinkedList:
  
  def __init__(self):
    self.__head = None
  
  def insertAtBefore(self,data):
    newNode = Node(data)
    if self.__head == None:
      self.__head = newNode
      return  
    newNode.setNext(self.__head)
    self.__head = newNode

  def insertAtEnd(self,data):
    newNode = Node(data)
    if self.__head == None:
      self.__head = newNode
      return  
    if self.__head.getNext() == None :
      self.__head.setNext(newNode)
      return

    last = self.__head
    while last:
      if last.getNext() == None: break
      last = last.getNext()
    last.setNext(newNode)
  
  def insertAfter(self,key,data):
    searchResult = self.search(key)
    if searchResult["state"] != True : return False
    newNode = Node(data)
    newNode.setNext(searchResult["data"].getNext())
    searchResult["data"].setNext(newNode)



  def delete(self,key):
    head = self.__head
    if head == None :return
    if self.search(key)["state"] != True :return False
    if head.getNext() == None :
      self.__head = None
      return True
    if head.getData() == key:
      self.__head = head.getNext()
      return True

    while head:
      if head.getNext() == None :break
      else :
        nextElement = head.getNext()
        if nextElement.getData() == key:
          if nextElement.getNext() != None:
            head.setNext(nextElement.getNext())
            return True
          else:
            break
      head = head.getNext()


    

  def search(self,key):
    tmp = self.__head

    while tmp:
      if tmp.getData() == key :
        return {"state":True, "data":tmp}
      if tmp.getNext() == None : break
      tmp = tmp.getNext()
    return {"state":False, "data":None}

  def sort(self):
    head = self.__head

    if head == None or head.getNext() == None : return
    while head:
      index = head.getNext()
      if index.getNext() == None : break
      while index :
        if index.getData() > head.getData() :
          indexValue = head.getData()
          headValue = index.getData()
          index.setData(indexValue)
          head.setData(headValue)
        if index.getNext() == None : break
        index = index.getNext()  
      if head.getNext() == None: break
      head = head.getNext()

  def printList(self):
    tmp = self.__head
    while(tmp):
      print('printing',str(tmp.getData()))
      tmp = tmp.getNext()