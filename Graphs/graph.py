class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.distance = 0
        self.predecessor = None

    def addNeighbour(self, vertex, weight = 0):
        self.connectedTo[vertex] = weight

    def __str__(self):
        return str(self.id) + " connectedTo: " + " ".join(map(lambda x: str(x.id) ,self.connectedTo))
    
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, vertex):
        return self.connectedTo[vertex]

class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex
    
    def getVertex(self, key):
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertexList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertexList:
            self.addVertex(f)
        if t not in self.vertexList:
            self.addVertex(t)
        self.vertexList[f].addNeighbour(self.vertexList[t], cost)

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())

    