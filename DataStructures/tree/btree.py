class BTreeNode :
    def __init__(self,leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children =[]
        self.tree = None
        self.parent = None

    def getLen(self):
        return len(self.keys)
    
    def addKey(self,value):
        if value == None:
            return False
        pos = 0
        while self.keys[pos]<value :
            pos += 1
        self.keys.insert(pos,value)
    
    def rmKey(self,pos):
        if pos >= self.getLen():return False
        self.keys.pop(pos)

    def addChild(self,node,pos):
        self.children.insert(pos,node)
        node.parent = self

    def rmChild(self,pos):
        self.children.pop(pos)




class BTree :
    def __init__(self,order):
        self.order = order
        self.root = None
    
    def search(self,node,value):
        if node.keys.count(value) != 0:
            return node
        if node.leaf:
            return False
        child = 0
        while node.getLen() and node.keys[child] < abs(value) :
            child += 1
        return self.search(node.children[child])
    
    def insert(self,value):
        actual= self.root
        if len(actual.keys) == (2*self.order) - 1:
            tmpNode = BTreeNode(False)
            tmpNode.tree = self
            self.root = tmpNode
            tmpNode.addChild(actual,0)
            self.split(actual,tmpNode,1)
            self.insertNonFull(tmpNode,value)
        else:
            self.insertNonFull(tmpNode,value)