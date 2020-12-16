class Row:
    def __init__(self, prefix=None, label=None, stride=1):
        self.prefix = prefix
        self.label = label
        if stride == 0:
            stride = 1
        self.stride = stride
        self.id = None


class Trie:
    def __init__(self, label="", stride=1, full_prefix=""):
        self.label = label
        self.full_prefix = full_prefix
        self.children = {}
        self.stridev = stride

    def __str__(self):
        return "{}\n{} --> {}".format(id(self), self.full_prefix, self.label)

    def insert(self, prefix, label, full_prefix):
        if prefix == "":
            self.label = label
            self.full_prefix = full_prefix
            return

        remain_prefix = prefix
        # if len(prefix) == 1:
        children = self.children.get(remain_prefix[0:int(self.stridev)], None)
        if children is None:
            dict_prefix = remain_prefix[0:int(self.stridev)]
            self.children[dict_prefix] = Trie("", full_prefix=self.full_prefix + dict_prefix)
            children = self.children[remain_prefix[0:self.stridev]]
        children.insert(remain_prefix[self.stridev:], label, full_prefix)

    def print(self, deep):
        print("\t" * deep + str(self.label))

        for i in self.children.keys():
            if self.children[i].print(deep + 1):
                print("\t" * deep + str(i) + " --> " + self.children[i].label)

    def info(self):
        print("|{:>4}|{:>10}|{:>5}|{:>5}|".format("ID", "Prefix", "Label", "Stride"))
        self.export_print()
        print("Edge (pointer) number: {}".format(self.get_edges()))
        print("Node number: {}".format(self.get_nodes()))
        print("Label number: {}".format(self.get_labels()))

    def get_edges(self):
        if len(self.children) == 0:
            return 0
        else:
            edge = len(self.children)

            for i in self.children.keys():
                edge += self.children[i].get_edges()
            return edge

    def get_nodes(self):
        if len(self.children) == 0:
            return 1
        else:
            nodes = 1
            for i in self.children.keys():
                nodes += self.children[i].get_nodes()
            return nodes

    def get_labels(self):
        if len(self.children) == 0:
            if self.label == "":
                return 0
            else:
                return 1
        else:
            labels = 0
            if self.label != "":
                labels = 1

            for i in self.children.keys():
                labels += self.children[i].get_labels()
            return labels

    def plot(self, graph, nodelabel):
        for i in self.children.keys():
            nodelabel[id(self.children[i])] = self.children[i].label
            # print("Label:" + str(self.label) )
            graph.add_edge(id(self), id(self.children[i]), prefix=i)
            self.children[i].plot(graph, nodelabel)

    def height(self):
        if len(self.children) == 0:
            return 0
        else:
            return max([self.children[i].height() for i in self.children.keys()]) + 1

    def child_array(self, deep):
        if deep > self.height() or deep == 0:
            return []
        if deep == 1:
            return list([self.children[i] for i in self.children.keys()])
        else:
            array = []
            for i in self.children.keys():
                array += self.children[i].child_array(deep - 1)

            return array
            # return list([self.children[i].child_array(deep-1) for i in self.children.keys()]

    def stride(self):
        if len(self.children) == 0:
            # No children --> leaf node
            return {"k": 0, "value": 0}
        else:
            minimum = {"k": None, "value": 100}

            for k in range(1, self.height() + 1):
                childs = self.child_array(k)
                summ = pow(2, k)
                for node in childs:
                    summ += node.stride()["value"]

                if summ < minimum["value"]:
                    minimum["k"] = k
                    # print("Can compress levels: " + str(k))
                    minimum["value"] = summ

            return minimum

    def set_stride(self):
        self.stridev = self.stride()["k"]
        for i in self.children.keys():
            self.children[i].set_stride()

    def export(self):
        array = []
        # if self.label != "":
        array.append(Row(self.full_prefix, self.label, self.stridev))

        for i in self.children.keys():
            array += self.children[i].export()
        return array

    def export_print(self):
        rows = self.export()
        for r in rows:
            print("|{:>2}|{:>10}|{:>5}|{:>5}|".format(str(r.id), str(r.prefix), str(r.label), str(r.stride)))

    def compress(self):
        self.set_stride()
        rows = self.export()

        for node in rows:
            print(
                "|{:>2}|{:>10}|{:>5}|{:>5}|".format(str(node.id), str(node.prefix), str(node.label), str(node.stride)))

        sum_stride = rows[0].stride
        root = Trie(full_prefix=rows[0].prefix, label=rows[0].label, stride=rows[0].stride)

        print("#1len: " + str(len(rows)))
        while True:
            add_stide = 1
            for row in rows:
                if row.label == "":
                    rows.remove(row)
                elif len(row.prefix) <= sum_stride:
                    root.insert(row.prefix, row.label, row.prefix)

                    if row.stride != 1:
                        add_stide = row.stride

                    rows.remove(row)

            print("#len: " + str(len(rows)))
            sum_stride += add_stide
            if len(rows) == 0:
                break

        root.export_print()

        return root

    # def level_compress(self):
    #     k = self.stride()["k"]
    #     root = Trie("",k)

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
