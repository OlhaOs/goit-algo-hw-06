import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["Kyiv","Zhitomyr","Kmelnitskyi","Rivne","Ternopil","Lviv"])

G.add_edges_from([("Kyiv","Zhitomyr"),("Zhitomyr","Rivne"),("Zhitomyr","Kmelnitskyi"),("Rivne","Lviv"),("Rivne","Ternopil"),
                  ("Kmelnitskyi","Ternopil"),("Ternopil","Lviv")])

nx.draw(G, with_labels=True)
plt.show()

print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")