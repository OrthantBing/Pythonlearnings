from vertex import Vertex
class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        self.vertexList[key] = Vertex(key)
        return self.vertexList[key] 
    
    def getVertex(self, n):
        if n in self.vertexList:
            return self.vertexList[n]
        else: 
            return None
    
    def __contains__(self, n):
        return n in self.vertexList

    def addEdge(self, f, t, cost = 0):
        if f not in self.vertexList:
            self.addVertex(f)
        if t not in self.vertexList:
            self.addVertex(t)
        self.vertexList[f].addNeighbour(self.vertexList[t], cost)

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())