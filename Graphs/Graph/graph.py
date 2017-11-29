from vertex import Vertex

class Graph:
    def __init__(self):
        self.numVertices = 0
        self.vertexList = {}

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def __contains__(self, key):
        return key in self.vertexList

    def getVertex(self, key):
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None

    def addEdge(self, v1key, v2key, cost = 0):
        if v1key not in self.vertexList:
            self.addVertex(v1key)
        if v2key not in self.vertexList:
            self.addVertex(v2key)
        self.vertexList[v1key].addNeighbour(self.vertexList[v2key],cost)

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())
        
