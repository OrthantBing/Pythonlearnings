from bfs import bfs
from graph import Graph

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    for line in wfile:
        word = line[:-1]
        for i in xrange(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    
    print d

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)

    return g

graph = buildGraph("./wordFile.txt")


bfs(graph,graph.getVertex("POLE"))

for i in graph.getVertices():
    print i, graph.getVertex(i).getDistance()

def traverse(y):
    x = y
    while (x.getPredecessor()):
        print x.getId()
        x = x.getPredecessor()
    print x.getId()

traverse(graph.getVertex('ROPE'))





