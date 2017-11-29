import sys
import os
import re

sys.path.append(re.match(r'(.*)/\w+$',os.getcwd()).groups()[0])

from Graph import Graph

def knightGraph(boardSize, tup):
    ktGraph = Graph()
    for row in xrange(boardSize):
        for col in xrange(boardSize):
            nodeId = posToNodeId(row, col, boardSize)
            newPositions = genLegalMoves(row, col, boardSize, tup)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], boardSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

def posToNodeId(row, column, boardsize):
    return (row * boardsize) + column

def genLegalMoves(x, y, boardsize, tup):
    newMoves = []
    moveoffsets = [(1,1),(-1,1),(1,-1),(-1,-1)]
    actualmoveoffset = []
    for i in moveoffsets:
        actualmoveoffset.append((i[0] * tup[0], i[1] * tup[1]))
        if tup[0] != tup[1]:
            actualmoveoffset.append((i[0] * tup[1], i[1] * tup[0]))

    for j in actualmoveoffset:
        newX = x + j[0]
        newY = y + j[1]
        if legalCoord(newX, boardSize) and legalCoord(newY, boardSize):
            newMoves.append((newX, newY))
    return newMoves

def legalCoord(a, boardsize):
    if a >= 0 and a < boardsize:
        return True
    else:
        return False