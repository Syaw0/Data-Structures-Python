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


  def delete(self):
    pass

  def peek(self):
    pass


x = Heap()
x.insert(1)
x.insert(2)
x.insert(3)
x.insert(4)
x.insert(5)

x.show()