import tkinter as tk
from methodes import *
import pandas as pd
import numpy as np




                                           #On inverse la liste pour obtenir le chemin dans le bon ordre (départ vers arrivée)


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
        

# GRAPHIQUE


            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FIN DJIKSTRA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEBUT FORD~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def ford_graphique(depart,arrive):
    """Cette fonction prend en paramètres deux arrêts et renvoie le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en utilisant la 
    méthode de Bellman Ford-Kalaba."""
    distance=[(np.Inf,None) for _ in range(len(nom_arrets))]    #Tous les arrets ont une distances infinie et pas de predécesseur
    distance[indice_som(depart)]=(0,indice_som(depart))         #On ajoute la distance de l'arret de départ soit 0, son pred est lui même
    a_traiter=[indice_som(depart)]                              #Une liste de tous les arrets que l'ont doit traiter
    while a_traiter!=[]:                                        #Tant que cette liste n'est pas vide on continue la recherche, on assume donc qu'il n'y a pas de chemins absorbants
        distancepred=distance[:]                                #Copie de la liste de distance afin de la comparer après l'étape

        for arret_actuel in a_traiter:                                                                          #L'arrets en cours de traitement                                                                      
            for proche in voisin(nom(arret_actuel)):                                                            #Pour tous les arrets voisins de l'arret observé
                if distance[indice_som(proche)][0]>distance[arret_actuel][0]+distarc(nom(arret_actuel),proche):         #Si ce nouveau chemin est plus avantageux que l'ancien      
                    distance[indice_som(proche)]=(distance[arret_actuel][0]+distarc(nom(arret_actuel),proche),arret_actuel)     #On met a jour sa distance et son prédécesseur 
        a_traiter=difference(distance,distancepred)             #on récupere tous les arrets qui ont était mis a jour dans l'étape
                                                                #Opération faite après l'étape pour ne pas interferer avec les données de l'étape
    
    # Reconstruction
    chemin=[arrive]                                             #On crée une liste de allant de l'arrivée vers le depart
    arret_actuel=indice_som(arrive)                             #On parcours les arrets en commançant par l'arrivée
    while arret_actuel!=indice_som(depart):                     #Tant que l'arret actuel n'est pas le départ on continue le chemin                   
        pred=distance[arret_actuel][1]                          #Prédécesseur de l'arret actuel   
        chemin.append(nom(pred))                                #On ajoute le Prédécesseur au chemin 
        arret_actuel=pred                                       #L'arret actuel devient le prédécesseur
    chemin.reverse()                                           #On inverse la liste pour obtenir le chemin depart->arrivée
    return (chemin,round(distance[indice_som(arrive)][0]))            #On retourne le chemin et la distance entre ces deux arrets
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FIN FORD~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        
        
def floyd_graphique(depart,arrive):
    """Cette fonction prend en paramètres deux arrêts et renvoient le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en utilisant la 
    méthode de floyd wharshall."""
    M0=[x[:] for x in poids_bus]                               #Creation de M0
    #------------Creation de P0---------
    P0=[x[:] for x in poids_bus]                                           
    for i in range (len(P0)):
        for j in range(len(P0)):
            if P0[i][j]==np.Inf or P0[i][j]==0:
                P0[i][j]=None
            else:
                P0[i][j]=i
    #-------------------------------------

    n=len(nom_arrets)
    k=0
    while k < n :
        MN=[x[:] for x in M0]
        PN=[x[:] for x in P0]  
        for i in range (n):
            for j in range (n):
                if i!=j and M0[k][j]+M0[i][k]<M0[i][j]:
                    MN[i][j]=M0[k][j]+M0[i][k]
                    PN[i][j]=P0[k][j]
                else:
                    MN[i][j]=M0[i][j]
                    PN[i][j]=P0[i][j]
        M0=[x[:] for x in MN]
        P0=[x[:] for x in PN]
        k+=1
    arret_actuel=indice_som(arrive)
    chemin=[nom(arret_actuel)]
    while arret_actuel!=indice_som(depart):

        pred=P0[indice_som(depart)][arret_actuel]
        chemin.append(nom(pred))
        arret_actuel=pred
    chemin.reverse()
    return (chemin,round(M0[indice_som(depart)][indice_som(arrive)]))

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

def dessinerOvale(x,y,canvas,width=16,height=6,couleur="black"):
    global screen_width
    global screen_height
    X = -(x-minY)*screen_height/(maxX-minX)
    Y = -(y-minX)*screen_width/(maxX-minX)
    canvas.create_oval(X-width/2,Y-width/2,X+width/2,Y+width/2,fill=couleur)
        
    
        
def dessiner(a,b,text,canvas,couleur="black"):
    global screen_width
    global screen_height
    deltaX=b[0]+a[0]+800
    deltaY=b[1]+a[1]+1080
    canvas.create_line(-(a[0]-minY)*screen_height/(maxX-minX)+deltaX,
                       -(a[1]-minX)*screen_width/(maxX-minX)+deltaY,
                       -(b[0]-minY)*screen_height/(maxX-minX)+deltaX,
                       -(b[1]-minX)*screen_width/(maxX-minX)+deltaY,
                       fill=couleur)
    width=6
    canvas.create_oval(-(a[0]-minY)*screen_height/(maxX-minX)+deltaX-width/2,
                       -(a[1]-minX)*screen_width/(maxX-minX)+deltaY-width/2,
                       -(a[0]-minY)*screen_height/(maxX-minX)+deltaX+width/2,
                       -(a[1]-minX)*screen_width/(maxX-minX)+deltaY+width/2,
                       fill=couleur)
        
if __name__ == '__main__':
    
    # FENETRE
    fenetre=tk.Tk()
    fenetre=fenetre
    fenetre.title="Visionneuse de graphes"
    fenetre.geometry("1920x1080+0+0") # Dimensions : 1920x1080 ; Apparait en : (0,0)
    fenetre.attributes('-fullscreen', True)
    fenetre.resizable(False,False) # Fenêtre non-redimensionnable - À CHANGER ?
    fenetre.configure(bg="lightgrey")
    
    # DONNÉES
    screen_width = fenetre.winfo_screenwidth()
    screen_height = fenetre.winfo_screenheight()
    
    # CANEVAS
    screen_width = 1080
    screen_height = 1080
    bg_canvas="lightblue"
    canevas = tk.Canvas(fenetre,width=screen_width,height=screen_height,bg=bg_canvas)
    
    # FOOTER
    Footer = tk.Frame(fenetre)
    Footer.place(x=1084,y=0)

    # ENTRÉES
    tk.Label(Footer, text="Départ :").grid(row=0)
    tk.Label(Footer, text="Arrivée :").grid(row=1)
    depart = tk.StringVar()
    arrivee = tk.StringVar()
    DepartReponse = tk.Entry(Footer,textvariable=depart, width=30).grid(row=0, column=1)
    ArriveeReponse = tk.Entry(Footer,textvariable=arrivee, width=30).grid(row=1, column=1)

    # BOUTTONS
    Dijkstra = tk.Button(Footer,activebackground="grey",bg="lightgrey",text="Exécuter Dijkstra",command=lambda : djiksrta_graphique(depart.get(),arrivee.get())).grid(row=1, column=2)
    Ford = tk.Button(Footer,activebackground="grey",bg="lightgrey",text="Exécuter Bellman-Ford Kalaba",command=lambda : ford_graphique(depart.get(),arrivee.get())).grid(row=1, column=3)
    Floyd = tk.Button(Footer,activebackground="grey",bg="lightgrey",text="Exécuter Floyd Warshall",command=lambda : floyd_graphique(depart.get(),arrivee.get())).grid(row=1, column=4)

    # TRAÇAGE
    for i in arrets:
        for j in arrets[i][2]:
            dessiner(arrets[i],arrets[j],i,canvas=canevas)

    canevas.place(x=0,y=0)
    canevas.mainloop()