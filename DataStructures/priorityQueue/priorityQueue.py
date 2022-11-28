
class PriorityQueue :
  def __init__(self):
    self.__storage = []
    pass

  def heapify(self, arr, length, index):
    largest = index
    l = 2 * index + 1
    r = 2 * index + 2

    if l < length and arr[index] < arr[l]:
      largest = l
    if r < length and arr[largest] < arr[r]:
      largest = r
    
    if largest != index :
      arr[index], arr[largest] = arr[largest] , arr[index]


  def insert(self,element):
    length = len(self.__storage)
    if length == 0 :
      self.__storage.append(element)
      return
    self.__storage.append(element)
    for index in range((len(self.__storage) // 2 ) - 1 , -1 , -1):
      self.heapify(self.__storage, len(self.__storage), index)
  

  def delete(self, element):
    size = len(self.__storage)
    for elm in range (0,size):
      if self.__storage[elm] == element:
        break
    
    self.__storage[elm] , self.__storage[size - 1] =  self.__storage[size - 1] , self.__storage[elm] 
    self.__storage.pop(size - 1)

    for index in range((len(self.__storage)//2)-1 ,-1 ,-1):
      self.heapify(self.__storage, len(self.__storage) , index)
  
    

  def getStorage(self):
    return self.__storage
