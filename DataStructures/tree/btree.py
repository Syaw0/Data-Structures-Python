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
        if len(self.keys)!=0:
            while len(self.keys) -1 >= pos and self.keys[pos]<value :
                pos += 1
        self.keys.insert(pos,value)
    
    def rmKey(self,pos=0):
        if pos >= self.getLen():return False
        return self.keys.pop(pos)

    def addChild(self,node,pos=0):
        self.children.insert(pos,node)
        node.parent = self

    def rmChild(self,pos=0):
        self.children.pop(pos)




class BTree :
    def __init__(self,order):
        self.order = order
        self.root = BTreeNode(True)
    
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
        tmpNode = BTreeNode(False)
        if len(actual.keys) == (2*self.order) - 1:
            tmpNode.tree = self
            self.root = tmpNode
            tmpNode.addChild(actual,0)
            self.split(actual,tmpNode,1)
            self.insertNonFull(tmpNode,value)
        else:
            self.insertNonFull(actual,value)
    
    def insertNonFull(self,node,value):
        print(node.leaf)
        if node.leaf:
            node.addKey(value)
            return
        
        tmp = node.getLen()
        while tmp>=1 and value < node.keys[tmp - 1]:
            tmp -= 1
        print(tmp,node.children)
        if node.children[tmp].getLen() == (2*self.order) - 1 :
            self.split(node.children[tmp],node,tmp+1)
            if value > node.keys[tmp]:
                tmp += 1
        
        self.insertNonFull(node.children[tmp],value)

    def split(self,child,parent,pos):
        newChild = BTreeNode(child.leaf)
        newChild.tree = self.root.tree
        for key in range(0,self.order):
            if len(child.children) != 0 :
                newChild.addChild(child.rmChild(0))
        if child.leaf!=True and len(child.children)!=0:
            for key in range(0,self.order):
                newChild.addChild(child.rmChild(0),key - 1)
        parent.addChild(newChild,pos)
        parent.addKey(child.rmKey(self.order - 1))
        parent.leaf = False

    def print_tree(self, x, l=0):
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.children) > 0:
            for i in x.children:
                self.print_tree(i, l)

x = BTree(3)
x.insert(3)
x.insert(4)
x.insert(5)
x.insert(6)
x.insert(8)
x.insert(9)
x.insert(10)
x.insert(11)
x.insert(12)
x.print_tree(x.root)
