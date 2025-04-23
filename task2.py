import networkx as nx
from collections import deque

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ') 
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    
    if not queue:
        return
    
    vertex = queue.popleft()
    
    if vertex not in visited:
        
        print(vertex, end=" ")
        
        visited.add(vertex)
        
        queue.extend(set(graph[vertex]) - visited)
    
    bfs_recursive(graph, queue, visited)




G = nx.Graph()

G.add_nodes_from(["Kyiv","Zhitomyr","Kmelnitskyi","Rivne","Ternopil","Lviv"])

G.add_edges_from([("Kyiv","Zhitomyr"),("Zhitomyr","Rivne"),("Zhitomyr","Kmelnitskyi"),("Rivne","Lviv"),("Rivne","Ternopil"),
                  ("Kmelnitskyi","Ternopil"),("Ternopil","Lviv")])


print("DFS")
dfs_recursive(G, "Kyiv")
print("")
print("BFS")
bfs_recursive(G, deque(["Kyiv"]))