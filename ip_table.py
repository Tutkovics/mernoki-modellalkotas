from mytrie import Trie


class Row:
    def __init__(self, prefix=None, label=None, stride=1):
        self.prefix = prefix
        self.label = label
        self.stride = stride
        self.id = None


class IP_table:
    def __init__(self):
        self.rows = []
        self.current_id = 0

    def add_row(self, row):
        row.id = self.current_id
        self.rows.append(row)
        self.current_id += 1

    def print(self):
        print("|{:>2}|{:>10}|{:>5}|".format("-" * 2, "-" * 10, "-" * 5))
        print("|{:>2}|{:>10}|{:>5}|".format("ID", "Prefix", "Label"))
        print("|{:>2}|{:>10}|{:>5}|".format("-" * 2, "-" * 10, "-" * 5))
        for row in self.rows:
            print("|{:>2}|{:>10}|{:>5}|".format(str(row.id), str(row.prefix), str(row.label)))
        print("|{:>2}|{:>10}|{:>5}|".format("-" * 2, "-" * 10, "-" * 5))

    def create_tree(self, k=1):
        root = Trie("-", k)
        for row in self.rows:
            root.insert(row.prefix, row.label, row.prefix)
        return root
