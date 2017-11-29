from graph import Graph
from vertex import Vertex
from collections import deque

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    for line in wfile:
        word = line[:-1]
        for i in xrange(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    
    return g

def bfs(g, start):
start.setDistance(0)
start.setPredecessor(None)
VertexQueue = deque()
VertexQueue.append(start)
    while len(VertexQueue) > 0:
        v = VertexQueue.popleft()
        for i in v.getConnections():
            if (i.color == 'white'):
                i.setColor('grey')
                i.setDistance(v.getDistance() + 1)
                i.setPredecessor(v)
                VertexQueue.appnd(i)
        v.setColor('black')

def traverse(y):
    x = y
    while(x.pred is not None):
        print (x.getId())
        x = x.pred
    print(x.getId())        
    

               