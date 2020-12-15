class Node:
    def __init__(self, name, prefix=None, label=None):
        self.childs = []
        self.name = name
        self.prefix = prefix
        self.label = label
    
    def add_child(self, node, label):
        self.childs.append({"label": label, "node": node})
        #print(self.childs)

    def print(self, deep):
        print("\t" * deep + "Node: {} #childs: {}".format(self.name, len(self.childs)))
        for child in self.childs:
            print("\t" * deep + "\t{} --> {}".format(child["label"], child["node"].name))
            child["node"].print(deep+1)
        #print(self.childs[0].name)
        

# a = Node("A")

# b = Node("B", "00")
# c = Node("C", "01")
# d = Node("D", "001")
# a.add_child(b, '00')
# a.add_child(c, '01')
# b.add_child(d, "0")

# a.print(0)