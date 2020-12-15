import networkx as nx

class Trie:
    def __init__(self, label = "", stripe = 1):
        self.label = label
        self.full_prefix = ""
        self.children = {}
    
    def __str__(self):
        return "{}\n{} --> {}".format(id(self), self.full_prefix, self.label)
    
    def insert(self, prefix, label, full_prefix):
        if prefix == "":
            self.label = label
            self.full_prefix = full_prefix
            return

        remain_prefix = prefix
        # if len(prefix) == 1:
        children = self.children.get(remain_prefix[0], None)
        if children == None:
            self.children[remain_prefix[0]] = Trie("" )
            children = self.children[remain_prefix[0]]
        children.insert(remain_prefix[1:], label, full_prefix)
            
    
    def print(self, deep):
        print("\t" * deep + str(self.label))

        for i in self.children.keys():
            if self.children[i].print(deep+1):
                print("\t" * deep + str(i) + " --> " + self.children[i].label)


    
    def plot(self, graph, nodelabel):
        for i in self.children.keys():
            nodelabel[id(self.children[i])] = self.children[i].label
            print("Label:" + str(self.label) )
            graph.add_edge(id(self), id(self.children[i]), prefix=i)
            self.children[i].plot(graph, nodelabel)

    def height(self):
        if len(self.children) == 0:
            return 0
        else:
            return max([self.children[i].height() for i in self.children.keys() ]) + 1

    def child_array(self, deep):
        if deep > self.height() or deep == 0:
            return []
        if deep == 1:
            return list([self.children[i] for i in self.children.keys()])
        else:
            array = []
            for i in self.children.keys():
                array += self.children[i].child_array(deep-1)

            return array
            # return list([self.children[i].child_array(deep-1) for i in self.children.keys()]
    
    def stride(self):
        if len(self.children) == 0:
            # No children --> leaf node
            return {"k": 0, "value": 0}
        else:
            minimum = {"k": None, "value": 100}

            for k in range(1,self.height()+1):
                childs = self.child_array(k)
                summ = pow(2,k)
                for node in childs:
                    summ += node.stride()["value"]

                if summ < minimum["value"]:
                    minimum["k"] = k
                    minimum["value"] = summ
            
            return minimum
        



# root = Trie("-")
# root.insert("000", "B")
# root.insert("001", "A")
# root.insert("01", "B")
# root.insert("10", "A")
# root.insert("11", "B")

# root.insert("1", "B")
# root.insert("11", "A")
# root.insert("0", "K")
# root.insert("01", "L")
# root.insert("001", "Y")
# root.insert("00", "x")
# root.insert("000", "z")
# root.insert("10", "C")
# root.print(0)
