from graphics import *
from methodes import *
from random import *
from time import sleep
import time as t
import random

<<<<<<< HEAD
windowWidth = 1023
windowHeight = 950
win = GraphWin("Reseau Chronoplus", windowWidth, windowHeight)

minLong=np.Inf
minLat=np.Inf
maxLong=np.NINF
maxLat=np.NINF
=======
from time import sleep
import time as t
import random

windowWidth = 1070
windowHeight = 981
win = GraphWin("Reseau Chronoplus", windowWidth, windowHeight)
>>>>>>> main

for i in arrets:
    if arrets[i][0] <= minLat:
        minLat=arrets[i][0]
    if arrets[i][0] >= maxLat:
        maxLat=arrets[i][0]
    if arrets[i][1] <= minLong:
        minLong=arrets[i][1]
    if arrets[i][1] >= maxLong:
        maxLong=arrets[i][1]

<<<<<<< HEAD
minLong-=0.002
minLat-=0.002
maxLong+=0.002
maxLat+=0.002

A=distanceGPS(43,44,0,0)
B=distanceGPS(43,43,-1,0)
=======

minLong=np.Inf
minLat=np.Inf
maxLong=np.NINF
maxLat=np.NINF


for i in arrets:
    if arrets[i][0] <= minLat:
        minLat=arrets[i][0]
    if arrets[i][0] >= maxLat:
        maxLat=arrets[i][0]
    if arrets[i][1] <= minLong:
        minLong=arrets[i][1]
    if arrets[i][1] >= maxLong:
        maxLong=arrets[i][1]

minLong-=0.002
minLat-=0.002
maxLong+=0.002
maxLat+=0.002
>>>>>>> main

if maxLat-minLat > maxLong-minLong:
    ratio=windowHeight/(maxLat-minLat)
else:
    ratio=windowWidth/(maxLong-minLong)

<<<<<<< HEAD
def afficherArret(arret,couleur,fill=True,taille=4):
    affichage = Circle(Point((arrets[arret][1]-minLong)*ratio,
                             windowHeight-(arrets[arret][0]-minLat)*ratio*(A/B)),taille)
    if fill:
        affichage.setFill(couleur)
    affichage.draw(win)
    return affichage
=======



def afficherArret(arret,couleur,fill=True):
    affichage = Circle(Point((arrets[arret][1]-minLong)*ratio,
                             windowHeight-(arrets[arret][0]-minLat)*ratio*1.37),4)
    if fill:
        affichage.setFill(couleur)
    affichage.draw(win)
>>>>>>> main


def tracerArc(arret1,arret2,couleur="black",largeur=1):
    affichage = Line(Point((arrets[arret1][1]-minLong)*ratio,
<<<<<<< HEAD
                           windowHeight-(arrets[arret1][0]-minLat)*ratio*(A/B)),
                     Point((arrets[arret2][1]-minLong)*ratio,
                            windowHeight-(arrets[arret2][0]-minLat)*ratio*(A/B)))
    affichage.setFill(couleur)
    affichage.setWidth(largeur)
    affichage.draw(win)
    return affichage

appuyez_text="init"
=======
                           windowHeight-(arrets[arret1][0]-minLat)*ratio*1.37),
                     Point((arrets[arret2][1]-minLong)*ratio,
                            windowHeight-(arrets[arret2][0]-minLat)*ratio*1.37))
    affichage.setFill(couleur)
    affichage.setWidth(largeur)
    affichage.draw(win)

appuyez_text="allala"
>>>>>>> main
def afficherDuree(tmpDepart):
    global appuyez_text
    try:
        appuyez_text.undraw()
    except:
        pass
    duree = t.time() - tmpDepart
<<<<<<< HEAD
    appuyez_text=Text(Point(45,138), str(round(duree,2))+"s")
=======
    appuyez_text=Text(Point(27,138), str(round(duree,2))+"s")
>>>>>>> main
    appuyez_text.draw(win)

    
def dijkstra_graphique(depart,arrivee,win):
    '''Cette fonction prend en paramètres deux arrêts et renvoie le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en
    utilisant la méthode de Djiksrta.'''
<<<<<<< HEAD
    tps_exec=Text(Point(73,117), "Temps d'execution :")
=======
    tps_exec=Text(Point(73,117), "Temps d'exécution :")
>>>>>>> main
    tps_exec.draw(win)
    tmp=t.time()
    afficherDuree(tmp)
    # Initialisation
    distance=[(np.Inf,None) for _ in range(len(nom_arrets))]
    distance[indice_som(depart)]=(0,indice_som(depart))                 # On ajoute la distance de l'arret de départ soit 0, son pred est lui même
    marque=[indice_som(depart)]                                         # Liste de tous les arrets dont la distance minimum a déjà été trouvée
    arret_actuel=indice_som(depart)                                     # arret_actuel est l'arret a partir du quel on va effectuer l'
    
    afficherArret(depart, "blue")
    afficherArret(arrivee, "blue")

    while arret_actuel!=indice_som(arrivee):                             # On peut raccourcir djikstra en s'arretant dès que l'on doit traiter le sommet d'arrivée
        for proche in voisin(nom(arret_actuel)):                                                                              #Pour tous les arrets voisins de l'arret observé                           
            if proche != depart and proche != arrivee:
                afficherArret(proche, "orange")
                afficherDuree(tmp)
            if indice_som(proche) not in marque:      #Si l'arret n'est pas déjà marqué (on pourra pas l'ameliorer de toute facon)
                afficherArret(proche, "purple")
                afficherDuree(tmp)
                sleep(0.01)
                if distance[indice_som(proche)][0]>distance[arret_actuel][0]+distarc(nom(arret_actuel),proche):               #Si ce nouveau chemin est plus avantageux que l'ancien 
                    distance[indice_som(proche)]=(distance[arret_actuel][0]+distarc(nom(arret_actuel),proche),arret_actuel)   #On met a jour sa distance et son prédécesseur
                    
        arret_actuel=min_exclude(distance,marque)                      #On récupere l'arret avec la distance minimale parmis les arrets non marqués
        
        marque.append(arret_actuel)                                    #On ajoute l'arret actuel dans les arrets marqués                                  

    afficherArret(arrivee, "blue")
    afficherDuree(tmp)
    
    # Reconstruction
    arret_actuel=indice_som(arrivee)                             #On parcours les arrets en commançant par l'arrivée
    chemin=[nom(arret_actuel)]                                       #On crée une liste de allant de l'arrivée vers le depart
    while arret_actuel!=indice_som(depart):                     #Tant que l'arret actuel n'est pas le départ on continue le chemin                   
        pred=distance[arret_actuel][1]                          #Prédécesseur de l'arret actuel   
        arret_actuel=pred                                       #L'arret actuel devient le Prédécesseur
        chemin.append(nom(arret_actuel))                        #On ajoute le Prédécesseur au chemin 
    

    tracerArc(arrivee,chemin[1],"green",3)
    for i in range(len(chemin)):
        if chemin[i]!=arrivee and chemin[i]!=depart:
            
            tracerArc(chemin[i],chemin[i+1],"green",3)
            afficherArret(chemin[i],"green")
            sleep(0.1)
            
    afficherArret(depart, "blue")
    afficherArret(arrivee, "blue")
    chemin.reverse()                                            #On inverse la liste pour obtenir le chemin dans le bon ordre (départ vers arrivée)
    return (chemin,round(distance[indice_som(arrivee)][0]))      # Renvoie : chemin (liste), distance (entier)

<<<<<<< HEAD
def bellman_graphique(depart,arrivee,win):
    """Cette fonction prend en paramètres deux arrêts et renvoie le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en utilisant la 
    méthode de Bellman Ford-Kalaba."""
    tps_exec=Text(Point(73,117), "Temps d'execution :")
=======
dijkstra("NOVE","TROICR")

def bellman_graphique(depart,arrivee,win):
    """Cette fonction prend en paramètres deux arrêts et renvoie le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en utilisant la 
    méthode de Bellman Ford-Kalaba."""
    tps_exec=Text(Point(73,117), "Temps d'exécution :")
>>>>>>> main
    tps_exec.draw(win)
    tmp=t.time()
    afficherDuree(tmp)
    
    distance=[(np.Inf,None) for _ in range(len(nom_arrets))]    #Tous les arrets ont une distances infinie et pas de predécesseur
    distance[indice_som(depart)]=(0,indice_som(depart))         #On ajoute la distance de l'arret de départ soit 0, son pred est lui même
    a_traiter=[indice_som(depart)]                              #Une liste de tous les arrets que l'ont doit traiter
    afficherArret(depart, "blue")
    afficherArret(arrivee, "blue")
    while a_traiter!=[]:                                        #Tant que cette liste n'est pas vide on continue la recherche, on assume donc qu'il n'y a pas de chemins absorbants
        distancepred=distance[:]                                #Copie de la liste de distance afin de la comparer après l'étape
        for arret_actuel in a_traiter:
            if nom(arret_actuel) != depart and nom(arret_actuel) != arrivee:
                afficherArret(nom(arret_actuel),"purple")                                                                        #L'arrets en cours de traitement                                                                      
            for proche in voisin(nom(arret_actuel)):                                                            #Pour tous les arrets voisins de l'arret observé
                afficherDuree(tmp)
                if proche != depart and proche != arrivee:
                    afficherArret(proche,"orange")
                if distance[indice_som(proche)][0]>distance[arret_actuel][0]+distarc(nom(arret_actuel),proche):         #Si ce nouveau chemin est plus avantageux que l'ancien      
                    distance[indice_som(proche)]=(distance[arret_actuel][0]+distarc(nom(arret_actuel),proche),arret_actuel)     #On met a jour sa distance et son prédécesseur 
                    sleep(0.001)
                    
        a_traiter=difference(distance,distancepred)             #on récupere tous les arrets qui ont était mis a jour dans l'étape
                                                                #Opération faite après l'étape pour ne pas interferer avec les données de l'étape
    afficherDuree(tmp)
    # Reconstruction
    chemin=[arrivee]                                             #On crée une liste de allant de l'arrivée vers le depart
    arret_actuel=indice_som(arrivee)                             #On parcours les arrets en commançant par l'arrivée
    while arret_actuel!=indice_som(depart):                     #Tant que l'arret actuel n'est pas le départ on continue le chemin                   
        pred=distance[arret_actuel][1]                          #Prédécesseur de l'arret actuel   
        chemin.append(nom(pred))                                #On ajoute le Prédécesseur au chemin 
        arret_actuel=pred                                       #L'arret actuel devient le prédécesseur
    afficherArret(depart,"blue")
    tracerArc(arrivee,chemin[1],"green",3)
    for i in range(len(chemin)):
        if chemin[i]!=arrivee and chemin[i]!=depart:
            tracerArc(chemin[i],chemin[i+1],"green",3)
            afficherArret(chemin[i],"green")
            sleep(0.1)
    afficherArret(arrivee,"blue")
    chemin.reverse()                                           #On inverse la liste pour obtenir le chemin depart->arrivée
    return (chemin,round(distance[indice_som(arrivee)][0]))            #On retourne le chemin et la distance entre ces deux arrets
<<<<<<< HEAD


def floyd_graphique(depart,arrivee,win):
    """Cette fonction prend en paramètres deux arrêts et renvoient le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en utilisant la 
    méthode de floyd wharshall."""
    tps_exec=Text(Point(73,117), "Temps d'execution :")
=======


def floyd_graphique(depart,arrivee,win):
    """Cette fonction prend en paramètres deux arrêts et renvoient le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en utilisant la 
    méthode de floyd wharshall."""
    tps_exec=Text(Point(73,117), "Temps d'exécution :")
>>>>>>> main
    tps_exec.draw(win)
    tmp=t.time()
    afficherDuree(tmp)
    M0=[x[:] for x in poids_bus]                                #Initialisation de M0
    P0=[x[:] for x in poids_bus]                                #Initialisation de P0
    #Initialisation des prédécesseurs
    for i in range (len(P0)):
        for j in range(len(P0)):
            if P0[i][j]==np.Inf or P0[i][j]==0:
                # Si +infini ou diagonale : Pas de prédécesseur connu ou existant
                P0[i][j]=None
            else:
                # Sinon, le prédécesseur est l'indice de la colonne
                P0[i][j]=i
    afficherArret(depart, "blue")
    afficherArret(arrivee, "blue")
    #-------------------------------------
<<<<<<< HEAD
    n=len(nom_arrets) # Taille de la matrice
    k=0 # Numéro de l'étape (= tous les chemins de longueur <= k)
    for k in range(n):
        random_red=random.randrange(0,255)
        random_green=random.randrange(0,255)
        random_blue=random.randrange(0,255)
        afficherDuree(tmp)
            
        for i in range (n):
            afficherArret(nom(k),color_rgb(random_red,random_green,random_blue),True)
            if nom(i)!=depart and nom(i)!=arrivee:
                afficherDuree(tmp)
                affichage=tracerArc(nom(i), nom(k),color_rgb(random_red,random_green,random_blue),2)
                
                if nom(i)!=nom(k):
                    afficherArret(nom(i),color_rgb(random_red,random_green,random_blue),True)
                    #affichage.undraw()
=======

    n=len(nom_arrets) # Taille de la matrice
    k=0 # Numéro de l'étape (= tous les chemins de longueur <= k)
    for k in range(n):
        if nom(k)!=depart and nom(k)!=arrivee:
            afficherArret(nom(k),"orange",True)
            afficherDuree(tmp)
        for i in range (n):
>>>>>>> main
            for j in range (n):
                # Application de la formule permettant de passer de PN à PN+1
                if M0[k][j]+M0[i][k]<M0[i][j]:
                    M0[i][j]=M0[k][j]+M0[i][k]
                    P0[i][j]=P0[k][j]
        # Remarque : On écrase les matrices car toutes les informations sont contenues dans les matrices finales
    afficherDuree(tmp)
    # Reconstruction
    arret_actuel=indice_som(arrivee)
    chemin=[nom(arret_actuel)]
    while arret_actuel!=indice_som(depart):

        pred=P0[indice_som(depart)][arret_actuel]
        chemin.append(nom(pred))
        arret_actuel=pred

    afficherArret(depart, "blue")
    afficherArret(arrivee, "blue")
    
    tracerArc(arrivee,chemin[1],"green",3)

    for i in range(len(chemin)):
        if chemin[i]!=arrivee and chemin[i]!=depart:
            tracerArc(chemin[i],chemin[i+1],"green",3)
            afficherArret(chemin[i],"green")
            sleep(0.1)
    afficherArret(arrivee,"blue")
    
<<<<<<< HEAD
    chemin.reverse()         #On inverse la liste pour obtenir le chemin dans le bon ordre (départ vers arrivée)
=======
    chemin.reverse()                                            #On inverse la liste pour obtenir le chemin dans le bon ordre (départ vers arrivée)
>>>>>>> main
    return (chemin,round(M0[indice_som(depart)][indice_som(arrivee)]))


def aide_touches():
    appuyez_text=Text(Point(50,10), "Appuyez sur :")
    appuyez_text.draw(win)
    
    dijkstra_text=Text(Point(55,28), "D pour Dijkstra")
    dijkstra_text.draw(win)
    
    bellman_text=Text(Point(56,48), "B pour Bellman")
    bellman_text.draw(win)
    
    floyd_text=Text(Point(47,68), "F pour Floyd")
    floyd_text.draw(win)
    
    autre_text=Text(Point(161,88), "Une autre touche pour terminer le programme")
    autre_text.draw(win)
    
def dessinerGraphe():
    win.delete('all')
<<<<<<< HEAD
    fond_carte = Image(Point(int(windowWidth/2)-1,int(windowHeight/2)+1), "fond_carte.png")
=======
    fond_carte = Image(Point(int(windowWidth/2),int(windowHeight/2)+1), "fond_carte.png")
>>>>>>> main
    fond_carte.draw(win)
    aide_touches()
    for i in arrets:
        for j in arrets[i][2]:
            tracerArc(i,j)
    for i in arrets:
        afficherArret(i,"black",False)

<<<<<<< HEAD
pressed_key=None
def random_arret():
    global pressed_key
    while True:
        if pressed_key == None :
            dessinerGraphe()
            pressed_key = win.getKey()
        if pressed_key=="d":
            dessinerGraphe()
            arret1 = random.choice(list(arrets.keys()))
            arret2 = random.choice(list(arrets.keys()))
            dijkstra_graphique(arret1,arret2,win)
            pressed_key = win.getKey()
            random_arret()
        if pressed_key=="b":
            dessinerGraphe()
            arret1 = random.choice(list(arrets.keys()))
            arret2 = random.choice(list(arrets.keys()))
            bellman_graphique(arret1,arret2,win)
            pressed_key = win.getKey()
            random_arret()
        if pressed_key=="f":
            dessinerGraphe()
            arret1 = random.choice(list(arrets.keys()))
            arret2 = random.choice(list(arrets.keys()))
            floyd_graphique(arret1,arret2,win)
            pressed_key = win.getKey()
            random_arret()
        else:
            win.close()
            return 0
    
def main(arret1,arret2,methode):
    dessinerGraphe()
    if methode == "dijkstra":
        dijkstra_graphique(arret1,arret2,win)
    elif methode == "bellman":
        bellman_graphique(arret1,arret2,win)
    elif methode == "floyd":
        floyd_graphique(arret1,arret2,win)
                
    win.getMouse()
    random_arret()
    
"""
Si vous souhaitez exécuter les algorithmes graphiquement entre deux arrêts précis :
    Appelez main() en précisant, dans l'odre, l'arrêt N°1, l'arrêt N°2, et la méthode (dijkstra,bellman ou floyd)
    Les trois paramètres sont des chaines de caractères
"""
main("NOVE","TROICR","floyd")

"""
Fonction montrant, avec deux arrêts pris au hasard, la démonstration des algorithmes
Les instructions sont affichées à l'écran. Veillez à bien attendre la fin de l'exécution d'une méthode avant d'agir sur le clavier.
"""
# random_arret()
=======

    
pressed_key=None
def random_arret():
    global pressed_key
    while True:
        if pressed_key == None :
            dessinerGraphe()
            
            
            pressed_key = win.getKey()
        if pressed_key=="d":
            dessinerGraphe()
            arret1 = random.choice(list(arrets.keys()))
            arret2 = random.choice(list(arrets.keys()))
            dijkstra_graphique(arret1,arret2,win)
            pressed_key = win.getKey()
            random_arret()
        if pressed_key=="b":
            dessinerGraphe()
            arret1 = random.choice(list(arrets.keys()))
            arret2 = random.choice(list(arrets.keys()))
            bellman_graphique(arret1,arret2,win)
            pressed_key = win.getKey()
            random_arret()
        if pressed_key=="f":
            dessinerGraphe()
            arret1 = random.choice(list(arrets.keys()))
            arret2 = random.choice(list(arrets.keys()))
            floyd_graphique(arret1,arret2,win)
            pressed_key = win.getKey()
            random_arret()
        else:
            win.close()
            return 0
    

def main(arret1,arret2):

    
    dessinerGraphe()
    dijkstra_graphique(arret1,arret2,win)
    win.getMouse()  
    win.close()
    
random_arret()
>>>>>>> main
