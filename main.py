from ip_table import IP_table, Row
from mytrie import Trie
import networkx as nx
import matplotlib.pyplot as plt


def print_title(title):
    print("\n", 10*"=", str(title), 10*"=", "\n")
# Assume normalized prefix tree in prefix table
print_title("Show IP table")
table = IP_table()
table.add_row(Row("000","B"))
table.add_row(Row("001","A"))
table.add_row(Row("01","B"))
# table.add_row(Row("010","B"))
# table.add_row(Row("011","A"))
table.add_row(Row("10","A"))
table.add_row(Row("11","B"))
table.print()

# Convert ip table to tree and plot it
print_title("Show Prefix tree")
tree = table.create_tree()
# G = nx.Graph()
# nodelabel = {}
# tree.plot(G, nodelabel)
# pos = nx.spring_layout(G)
# nx.draw(G, pos, labels=nodelabel, font_size=10, with_labels=True)
# edge_labels = nx.get_edge_attributes(G, 'prefix')
# nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)
# plt.show()

print_title("Show Few Log")
print(tree.height())
print(tree.child_array(1))
print(tree.child_array(2))
print(tree.child_array(3))
print(tree.child_array(4))

print(tree.stride())
#print(tree.children['1'].stride())

print_title("Compress tree")
k = tree.stride()["k"]
root = table.create_tree(k)

G = nx.Graph()
nodelabel = {}
root.plot(G, nodelabel)
pos = nx.spring_layout(G)
nx.draw(G, pos, labels=nodelabel, font_size=10, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'prefix')
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)
plt.show()

