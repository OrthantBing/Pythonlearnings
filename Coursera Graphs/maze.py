from collections import deque
class Vertex: 
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.visited = False

    def addNeighbour(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()
    

    def __str__(self):
        return str(self.id) + ' connectedTo ' + str([i.id for i in self.connectedTo.keys()]) 

class Graph(object):
    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        self.vertexList[key] = Vertex(key)
        self.numVertices += 1
        return self.vertexList[key]

    def addEdge(self, f, t, cost = 0):
        if f not in self.vertexList:
            self.addVertex(f)
        if t not in self.vertexList:
            self.addVertex(t)
        self.vertexList[f].addNeighbour(self.vertexList[t], cost)

    def __contains__(self, vertex):
        return vertex in self.vertexList

    def getVertices(self):
        return self.vertexList.keys()

    def __itr__(self):
        return iter(self.vertexList.values())
    
    def __str__(self):
        return "\n".join([str(i) for i in self.vertexList.values()])

    def pathExists(self, vertex1, vertex2):
        if vertex1 not in self.vertexList:
            return False
        if vertex2 not in self.vertexList:
            return False

        return self.explore(vertex1, vertex2)
        
    def explore(vertex1, vertex2):
        queue = deque()
        queue.append(vertex1)
        while len(queue) > 0:
            currentvertex = queue.pop()
            currentvertex.visited = True
            for nbr in currentvertex.getConnections():
                if nbr.visited == True:
                    




    
if __name__ == "__main__":
    n, m = map(int, raw_input().split())
    graph = Graph()
    for i in xrange(m):
        vertex1, vertex2 = map(int, raw_input().split())
        graph.addEdge(vertex1, vertex2)
    
    print str(graph)
        

        