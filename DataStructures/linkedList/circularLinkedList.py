class Node :
  def __init__(self,prevNode, data):
    self.prevNode = prevNode
    self.data = data
    self.next = None


class CircularLinkedList :
  
  def __init__(self):
    self.__head = None
    self.length = 0

  def insertAtEnd(self, data):
    newNode = Node(self.__head, data)
    if self.__head == None :
      self.__head = newNode
      self.length += 1
      return

    if self.__head.next == None :
      self.__head.prevNode = newNode
      self.__head.next = newNode
      self.length += 1
      return

    self.__head.prevNode.next = newNode
    self.__head.prevNode = newNode
    self.length += 1
    
  def insertAtBegin(self,data):
    newNode = Node(None,data)

    if self.__head == None :
      self.__head = newNode
      self.length += 1
      return

    if self.__head.next == None:
      self.__head.next = newNode
      self.__head.prevNode = newNode
      newNode.next = self.__head
      newNode.prevNode = self.__head
      self.__head = newNode
      self.length += 1
      return
    
    newNode.next = self.__head
    newNode.prevNode = self.__head.prevNode
    self.__head.prevNode.next = newNode
    self.__head.prevNode = newNode
    self.__head = newNode
    self.length += 1

  def insertAfter(self):
    pass

  def delete(self):
    pass

  def search(self):
    pass

  def printAll(self):
    tmp = self.__head
    for item in range(0,self.length ):
      print(tmp.data)
      tmp = tmp.next
      
      



# x = CircularLinkedList()

# x.insertAtBegin(0)
# x.insertAtBegin(1)
# x.insertAtBegin(2)
# x.insertAtBegin(3)
# x.printAll()