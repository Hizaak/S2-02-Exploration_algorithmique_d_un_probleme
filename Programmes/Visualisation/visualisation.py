from graphics import *
from methodes import *

win = GraphWin("Réseau Chronoplus", 910, 910)

minX=np.Inf
minY=np.Inf
maxX=np.NINF
maxY=np.NINF

for i in arrets:
    if arrets[i][1] <= minX:
        minX=arrets[i][1]
    if arrets[i][0] <= minY:
        minY=arrets[i][0]
    if arrets[i][1] >= maxX:
        maxX=arrets[i][1]
    if arrets[i][0] >= maxY:
        maxY=arrets[i][0]

zone = 900

def dessinerGraphe():
    ratio = zone/(maxX-minX)
    for i in arrets:    
        for j in arrets[i][2]:
            Line(Point((arrets[i][1]-minX)*ratio+5,
                        700-(arrets[i][0]-minY)*ratio+5),
                 Point((arrets[j][1]-minX)*ratio+5,
                        700-(arrets[j][0]-minY)*ratio+5)).draw(win)
    for i in arrets:
        Circle(Point((arrets[i][1]-minX)*ratio+5,
                      700-(arrets[i][0]-minY)*ratio+5),4).draw(win)


def main():
    dessinerGraphe()
    win.getMouse()
    win.close()
    
main()



