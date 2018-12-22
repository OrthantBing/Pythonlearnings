def drawTicks(tickLength):
    if (tickLength > 0):
        drawTicks(tickLength - 1)
        drawOneTick(tickLength)
        drawTicks(tickLength - 1)

def drawOneTick(tickLength):
   print "-"*tickLength

if __name__ == '__main__':
    drawTicks(5)