class Node:
    def __init__(self):
        self.prefix = None
        self.label = None
        self.left = None
        self.right = None
    
    def insert(self, prefix, label):
        if self.prefix == prefix:
            self.label = label
        else:
            if self.prefix + "0" == prefix:


            elif self.prefix + "1" == prefix:

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

        

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()

