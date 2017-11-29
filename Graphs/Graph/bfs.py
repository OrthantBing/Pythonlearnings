from collections import deque

def bfs(g, start):
    start.setDistance(0)
    start.setPredecessor(None)
    vertQueue = deque()
    vertQueue.append(start)
    while len(vertQueue) > 0:
        currentVert = vertQueue.pop()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == "white"):
                nbr.setColor("gray")
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPredecessor(currentVert)
                vertQueue.append(nbr)
            currentVert.setColor("black")


