class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.distance = None
        self.color = "white"
        self.predecessor = None
    
    def getDistance(self):
        return self.distance

    def setDistance(self, dist):
        self.distance = dist

    def setPredecessor(self, pred):
        self.predecessor = pred

    def getPredecessor(self):
        return self.predecessor

    def setColor(self, col):
        self.color = col

    def getColor(self):
        return self.color

    def addNeighbour(self, vertex, weight):
        self.connectedTo[vertex] = weight

    def __str__(self):
        return str(self.id)

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, vertex):
        return self.connectedTo[vertex]
