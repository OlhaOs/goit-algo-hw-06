import networkx as nx
import heapq

def dijkstra(graph, start):
    
    shortest_path = {vertex: float('infinity') for vertex in graph}
    shortest_path[start] = 0
    unvisited = [(0,start)]

    while unvisited:
        current_distance, current_vertex = heapq.heappop(unvisited)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight["weight"]

            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                heapq.heappush(unvisited, (distance, neighbor))

    return shortest_path

G = nx.Graph()

G.add_nodes_from(["Kyiv","Zhitomyr","Kmelnitskyi","Rivne","Ternopil","Lviv"])

G.add_edge("Kyiv","Zhitomyr",weight=140)
G.add_edge("Zhitomyr","Kmelnitskyi",weight=192)
G.add_edge("Zhitomyr","Rivne",weight=188)
G.add_edge("Rivne","Ternopil",weight=155)
G.add_edge("Rivne","Lviv",weight=211)
G.add_edge("Kmelnitskyi","Ternopil",weight=112)
G.add_edge("Ternopil","Lviv",weight=128)
                  
print(dijkstra(G, "Kyiv"))