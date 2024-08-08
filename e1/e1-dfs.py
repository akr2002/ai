from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def insertEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFS_helper(self, u, visited):
        visited.add(u)
        print(u, end=" ")
        for v in self.adj[u]:
            if v not in visited:
                self.DFS_helper(v, visited)

    def DFS(self, u):
        visited = set()
        self.DFS_helper(u, visited)


g = Graph()
g.insertEdge(0, 1)
g.insertEdge(0, 3)
g.insertEdge(1, 4)
g.insertEdge(1, 2)
g.insertEdge(2, 3)
g.insertEdge(4, 5)
g.insertEdge(4, 6)
g.insertEdge(5, 6)
print("The DFS traversal of the given graph starting from node 0 is -")
g.DFS(0)
