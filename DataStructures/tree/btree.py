class BTreeNode :
    def __init__(self,leaf=False):
        self.leaf = False
        self.keys = []
        self.children =[]
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