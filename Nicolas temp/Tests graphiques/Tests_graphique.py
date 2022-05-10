import tkinter as tk
import methodes
import pandas as pd
import numpy as np

# JEU DE DONNÉES
donneesbus=pd.read_csv(r'./donneesbus.csv',sep=';')
arrets={}
for c in range (len( donneesbus)):
    arrets[donneesbus['arret'][c]]=[float(donneesbus['lattitude'][c].replace(",",".")),float(donneesbus['longitude'][c].replace(",",".")),list(donneesbus['listesucc'][c].replace('[','').replace(']','').replace("'","").replace(" ","").split(","))]
nom=list(arrets.keys())
nom_arrets=[]

minX=np.inf
minY=np.inf
maxX=-100
maxY=-100

for i in arrets:
    if arrets[i][1]<= minX:
        minX=arrets[i][1]
    if arrets[i][0]<= minY:
        minY=arrets[i][0]
    if arrets[i][1]>= maxX:
        maxX=arrets[i][1]
    if arrets[i][0]>= maxY:
        maxY=arrets[i][0]
        
def traceCroix(x,y,canvas,longueur=6,forme="penche",couleur="black",padding=0):
    if forme=="penche":
        canvas.create_line(x-longueur,
                           y-longueur,
                           x+longueur,
                           y+longueur,
                           fill=couleur)
        canvas.create_line(x+longueur,
                           y-longueur,
                           x-longueur,
                           y+longueur,
                           fill=couleur)
    else:
        canvas.create_line(x,y-longueur,
                           x,y+longueur,
                           fill=couleur)
        canvas.create_line(x+longueur,y,
                           x-longueur,y,
                           fill=couleur)
    
def tracerLigne(a,b,canvas,couleur="black"):
    global screen_width
    global screen_height
    canvas.create_line((a[1]-minX)*screen_width/(maxX-minX),
                       (a[0]-minY)*screen_height/(maxX-minX),
                       (b[1]-minX)*screen_width/(maxX-minX),
                       (b[0]-minY)*screen_height/(maxX-minX),
                       fill=couleur)
"""
for i in arrets:    
    pecX = (arrets[i][0]-minX)*zone_width/(maxX-minX)
    pecY = (arrets[i][1]-minY)*zone_height/(maxY-minY)
    canvas.create_oval(pecX-len(i),
                       pecY,
                       pecX+oval_width+len(i),
                       pecY+oval_height,
                       fill=oval_color)
    canvas.create_text(pecX+oval_width/2,pecY+oval_height/2,text=i)
"""

def dessinerOvale(x,y,canvas,width=16,height=6,couleur="black"):
    X = (x-minX)*screen_width/(maxX-minX)
    Y = (y-minY)*screen_height/(maxY-minY)
    canvas.create_oval(X-width/2,Y-width/2,X+width/2,Y+width/2,fill=couleur)

def ecrireTexte(texte,x,y,canvas,couleur="black"):
    X = (x-minX)*screen_width/(maxX-minX)
    Y = (y-minY)*screen_height/(maxY-minY)
    canvas.create_text(X,Y,fill=couleur,text=texte)
        
if __name__ == '__main__':
    
    # FENETRE
    fenetre=tk.Tk()
    fenetre=fenetre
    fenetre.title="Visionneuse de graphes"
    fenetre.geometry("1920x1080+0+0") # Dimensions : 1920x1080 ; Apparait en : (0,0)
    fenetre.resizable(False,False) # Fenêtre non-redimensionnable - À CHANGER ?
    fenetre.configure(bg="lightgrey")
    
    # DONNÉES
    screen_width = fenetre.winfo_screenwidth()
    screen_height = fenetre.winfo_screenheight()
    
    # CANEVAS
    screen_width = fenetre.winfo_screenwidth()
    screen_height = fenetre.winfo_screenheight()
    bg_canvas="lightblue"
    canevas = tk.Canvas(fenetre,width=screen_width,height=screen_height,bg=bg_canvas)
    
    # FOOTER
    Footer = tk.Frame(fenetre)
    Footer.pack(side=tk.BOTTOM)

    # ENTRÉES
    tk.Label(Footer, text="Départ :").grid(row=0)
    tk.Label(Footer, text="Arrivée :").grid(row=1)
    DepartReponse = tk.Entry(Footer).grid(row=0, column=1)
    DepartReponse = tk.Entry(Footer).grid(row=1, column=1)

    # BOUTTONS
    Dijkstra = tk.Button(Footer,activebackground="grey",bg="lightgrey",text="Exécuter Dijkstra",command=lambda : methodes.djiksrta("ZADI","NOVE")).grid(row=1, column=2)
    Ford = tk.Button(Footer,activebackground="grey",bg="lightgrey",text="Exécuter Bellman-Ford Kalaba",command=lambda : methodes.ford("ZADI","NOVE")).grid(row=1, column=3)
    Floyd = tk.Button(Footer,activebackground="grey",bg="lightgrey",text="Exécuter Floyd Warshall",command=lambda : methodes.floyd("ZADI","NOVE")).grid(row=1, column=4)

    # TRAÇAGE
    for i in arrets:
        for j in arrets[i][2]:
            tracerLigne(arrets[i],arrets[j],canvas=canevas)

    for i in arrets:
        dessinerOvale(arrets[i][1], arrets[i][0],canvas=canevas)
        ecrireTexte(i, arrets[i][1], arrets[i][0],canvas=canevas)
    

    
    canevas.place(x=0,y=0)
    canevas.mainloop()