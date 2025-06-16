# 🔰 Beginner Level
# Find the Number of Connected Components

# Given an undirected graph, count the number of connected components.

# Detect Cycle in Undirected Graph

# Use DFS or Union-Find to check if there's a cycle.

# Detect Cycle in Directed Graph

# Use DFS with recursion stack or Kahn's Algorithm.

# Bipartite Graph Check

# Can you color the graph using 2 colors without two same-colored neighbors?

# Shortest Path in Unweighted Graph

# Use BFS to find the shortest path from source to all nodes.

# ⚙️ Intermediate Level
# Dijkstra’s Algorithm

# Given a weighted graph with non-negative edges, find the shortest path from source to all nodes.

# Prim’s Algorithm (Minimum Spanning Tree)

# Find the minimum cost to connect all nodes in an undirected weighted graph.

# Topological Sort

# For a DAG (Directed Acyclic Graph), return a valid topological ordering.

# Course Schedule

# Given course prerequisites, can all courses be finished? (Cycle detection in DAG)

# Clone a Graph

# Given a graph as a node with neighbors, return a deep copy.

# 🔥 Advanced Level
# Bellman-Ford Algorithm

# Find shortest paths with the possibility of negative edges and detect negative cycles.

# Floyd-Warshall Algorithm

# All-pairs shortest paths in a dense graph.

# Kosaraju’s Algorithm (SCCs)

# Find all strongly connected components in a directed graph.

# Critical Connections (Bridges) in a Network

# Find all bridges whose removal disconnects the graph (Tarjan's Algorithm).

# Network Delay Time

# Similar to Dijkstra — given a starting node and edge weights, find time to reach all nodes.

# 💡 Real-Life Inspired
# Cheapest Flights Within K Stops (Leetcode 787)

# Modify Dijkstra to track number of stops.

# Word Ladder (Leetcode 127)

# Transform one word to another using BFS on implicit graph.

# Rotting Oranges (Leetcode 994)

# 2D grid graph, BFS from multiple sources.

# Alien Dictionary

# Build a graph of character precedence and do topological sort.

# Reconstruct Itinerary (Hierholzer’s Algorithm)

# Eulerian path with lexical order.


'''def no_provinces(i):
    L[i] = True
    for j in range(n):
        if g[i][j] == 1 and i != j and L[j] != True:
            no_provinces(j)

n = 5
L = [False] * n
c = 0
g = [[1, 1, 0, 0, 0],
     [1, 1, 1, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 1, 1],
     [0, 0, 0, 1, 1]]

for i in range(n):
    if not L[i]:
        c += 1
        no_provinces(i)

print(c)'''

d = {10:[[5,2],[7,4]],5:[[10,2],[7,1],[8,3],[3,2]],7:[[10,4],[5,1],[8,1]],8:[[7,1],[5,3],[3,1]],3:[[5,2],[8,1]]}
def dijikstra_alogithm(u,v):
    cost = {}
    for i in d:
        cost[i] = float('inf')
    cost[10]=0
    visited=set()
    l = []
    l.append(10)
    while l:
        curr = l.pop(0)
        visited.add(curr)
        for i,w in d[curr]:
            if i not in l and i not in visited:
                l.append(i)
            if cost[curr]+w < cost[i]:
                cost[i]=cost[curr]+w
            
        print(cost)
        #print the shortest path from u to v
import heapq
d = {10:[[5,2],[7,4]],5:[[10,2],[7,1],[8,3],[3,2]],7:[[10,4],[5,1],[8,1]],8:[[7,1],[5,3],[3,1]],3:[[5,2],[8,1]]}
def prims_algorithm(u):
    vi = set()
    mh = [(0,u)]
    mc = 0
    while mh:
        w,n = heapq.heappop(mh)
        if n in vi:
            continue
        vi.add(n)
        mc = mc+w
        for i,we in d[n]:
            if i not in vi:
                heapq.heappush(mh,(we,i))
    print(mc,end=" ")
      

dijikstra_alogithm(10,3)
prims_algorithm(10)