class Vertex:
    def __init__(self, id):
        self.id = id
        self.connectedTo = {}
        self.pred = None
        self.distance = None
        self.color = 'white'

    def addNeighbour(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo: ' + str([i for i in self.connectedTo.keys()])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def setDistance(self, val):
        self.distance = val

    def setPredecessor(self, vertex):
        self.pred = vertex
    
    def setColor(self, color):
        self.color = color