class Heap:
  def __init__(self):
    self.storage = []

  def heapify(self, arr, length, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < length and arr[left] > arr[index]:
      largest = left
    if right < length and arr[right] > arr[largest]:
      largest = right

    if largest != index:
      arr[largest] ,arr[index ] = arr[index ], arr[largest]
    

    

  def insert(self,data):
    self.storage.append(data)
    if len(self.storage )== 0:
      return
    for index in range((len(self.storage)//2) - 1 , -1 , -1) :
      print(index)
      self.heapify(self.storage,len(self.storage), index)  

  def show(self):
    print(self.storage)


  def delete(self, key):
    result = self.checkForKey(key)
    arr = self.storage
    print("this is result",result)
    if not result:
      return
    arr[result] , arr[len(arr) - 1] =  arr[len(arr) - 1] , arr[result] 
    arr.pop()
    for index in range((len(arr)//2) - 1 , -1 , -1) :
      self.heapify(self.storage , len(self.storage) , index)
      

  def checkForKey(self,key):
    if self.storage.count(key) == 0 :
      return False
    return self.storage.index(key)

  def peek(self,key):
    result = self.checkForKey(key)
    if not result:
      return
    return self.storage[result]
    