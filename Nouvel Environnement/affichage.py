from algorithmes import *
import tkinter as tk
import numpy as np

# Données

  

minX=np.inf
minY=np.inf
maxX=-100
maxY=-100

for i in arrets:
    if arrets[i][0]<= minX:
        minX=arrets[i][0]
    if arrets[i][1]<= minY:
        minY=arrets[i][1]
    if arrets[i][0]>= maxX:
        maxX=arrets[i][0]
    if arrets[i][1]>= maxY:
        maxY=arrets[i][1]
        
def traceArc(x1,y1,x2,y2):
    canevas.create_line(x1,y1,x2,y2)

def dessinerGraphe():
    for i in arrets:
        for j in arrets[i][2]:
            # Tracer les arcs
            traceArc((arrets[i][0]-minX)*screen_width/(maxX-minX),
                     (arrets[i][1]-minY)*screen_height/(maxX-minX),
                     (arrets[j][0]-minX)*screen_width/(maxX-minX),
                     (arrets[j][1]-minY)*screen_height/(maxX-minX))
            


# FENETRE
fenetre=tk.Tk()

fenetre.title="Visionneuse de graphes"
fenetre.geometry("1920x1080+0+0")
fenetre.attributes('-fullscreen', True)
fenetre.resizable(False,False)
fenetre.configure(bg="lightgrey")

screen_width = fenetre.winfo_screenwidth()
screen_height = fenetre.winfo_screenheight()  

# CANEVAS

canevas = tk.Canvas(fenetre,width=screen_width,height=screen_height,bg="lightblue",highlightthickness=0)

dessinerGraphe()


canevas.place()
canevas.pack(padx = 20,pady =20)


fenetre.mainloop()
    
    
    
    
