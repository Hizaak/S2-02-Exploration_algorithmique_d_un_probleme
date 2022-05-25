from graphics import *
from methodes import *
from time import sleep
import random

windowWidth = 1070
windowHeight = 981
win = GraphWin("Reseau Chronoplus", windowWidth, windowHeight)



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

if maxLat-minLat > maxLong-minLong:
    ratio=windowHeight/(maxLat-minLat)
else:
    ratio=windowWidth/(maxLong-minLong)
print(ratio)



def afficherArret(arret,couleur,fill=True):
    affichage = Circle(Point((arrets[arret][1]-minLong)*ratio,
                             windowHeight-(arrets[arret][0]-minLat)*ratio),4)
    if fill:
        affichage.setFill(couleur)
    affichage.draw(win)


def tracerArc(arret1,arret2,couleur="black",largeur=1):
    affichage = Line(Point((arrets[arret1][1]-minLong)*ratio,
                           windowHeight-(arrets[arret1][0]-minLat)*ratio),
                     Point((arrets[arret2][1]-minLong)*ratio,
                            windowHeight-(arrets[arret2][0]-minLat)*ratio))
    affichage.setFill(couleur)
    affichage.setWidth(largeur)
    affichage.draw(win)


def dijkstra_graphique(depart,arrivee,win):
    '''Cette fonction prend en paramètres deux arrêts et renvoie le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en
    utilisant la méthode de Djiksrta.'''
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
            if indice_som(proche) not in marque:      #Si l'arret n'est pas déjà marqué (on pourra pas l'ameliorer de toute facon)
                afficherArret(proche, "purple")
                sleep(0.01)
                if distance[indice_som(proche)][0]>distance[arret_actuel][0]+distarc(nom(arret_actuel),proche):               #Si ce nouveau chemin est plus avantageux que l'ancien 
                    distance[indice_som(proche)]=(distance[arret_actuel][0]+distarc(nom(arret_actuel),proche),arret_actuel)   #On met a jour sa distance et son prédécesseur
                    
        arret_actuel=min_exclude(distance,marque)                      #On récupere l'arret avec la distance minimale parmis les arrets non marqués
        
        marque.append(arret_actuel)                                    #On ajoute l'arret actuel dans les arrets marqués                                  

    afficherArret(arrivee, "blue")
    
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

dijkstra("NOVE","TROICR")

def ford_graphique(depart,arrivee,win):
    """Cette fonction prend en paramètres deux arrêts et renvoie le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en utilisant la 
    méthode de Bellman Ford-Kalaba."""
    distance=[(np.Inf,None) for _ in range(len(nom_arrets))]    #Tous les arrets ont une distances infinie et pas de predécesseur
    distance[indice_som(depart)]=(0,indice_som(depart))         #On ajoute la distance de l'arret de départ soit 0, son pred est lui même
    a_traiter=[indice_som(depart)]                              #Une liste de tous les arrets que l'ont doit traiter
    affichage = Circle(Point((arrets[depart][1]-minLong)*ratio+5,
              delta-(arrets[depart][0]-minLat)*facteur_Y+5),4)
    affichage.setFill("blue")
    affichage.draw(win)
    affichage = Circle(Point((arrets[arrivee][1]-minLong)*ratio+5,
              delta-(arrets[arrivee][0]-minLat)*facteur_Y+5),4)
    affichage.setFill("blue")
    affichage.draw(win)
    while a_traiter!=[]:                                        #Tant que cette liste n'est pas vide on continue la recherche, on assume donc qu'il n'y a pas de chemins absorbants
        distancepred=distance[:]                                #Copie de la liste de distance afin de la comparer après l'étape
        for atraiter in a_traiter:
            if nom(atraiter) != depart and nom(atraiter) != arrivee:
                affichage = Circle(Point((arrets[nom(atraiter)][1]-minLong)*ratio+5,
                          delta-(arrets[nom(atraiter)][0]-minLat)*facteur_Y+5),4)
                affichage.setFill("purple")
                affichage.draw(win)
        for arret_actuel in a_traiter:                                                                          #L'arrets en cours de traitement                                                                      
            for proche in voisin(nom(arret_actuel)):                                                            #Pour tous les arrets voisins de l'arret observé
                if proche != depart and proche != arrivee:
                    affichage = Circle(Point((arrets[proche][1]-minLong)*ratio+5,
                              delta-(arrets[proche][0]-minLat)*facteur_Y+5),4)
                    affichage.setFill("coral1")
                    affichage.draw(win)
                if distance[indice_som(proche)][0]>distance[arret_actuel][0]+distarc(nom(arret_actuel),proche):         #Si ce nouveau chemin est plus avantageux que l'ancien      
                    distance[indice_som(proche)]=(distance[arret_actuel][0]+distarc(nom(arret_actuel),proche),arret_actuel)     #On met a jour sa distance et son prédécesseur 
                    sleep(0.001)
                    
        a_traiter=difference(distance,distancepred)             #on récupere tous les arrets qui ont était mis a jour dans l'étape
                                                                #Opération faite après l'étape pour ne pas interferer avec les données de l'étape
    
    # Reconstruction
    chemin=[arrivee]                                             #On crée une liste de allant de l'arrivée vers le depart
    arret_actuel=indice_som(arrivee)                             #On parcours les arrets en commançant par l'arrivée
    while arret_actuel!=indice_som(depart):                     #Tant que l'arret actuel n'est pas le départ on continue le chemin                   
        pred=distance[arret_actuel][1]                          #Prédécesseur de l'arret actuel   
        chemin.append(nom(pred))                                #On ajoute le Prédécesseur au chemin 
        arret_actuel=pred                                       #L'arret actuel devient le prédécesseur
    
    affichage = Circle(Point((arrets[depart][1]-minLong)*ratio+5,
              delta-(arrets[depart][0]-minLat)*facteur_Y+5),4)
    affichage.setFill("blue")
    affichage.draw(win)
    affichage = Line(Point((arrets[arrivee][1]-minLong)*ratio+5,
                delta-(arrets[arrivee][0]-minLat)*facteur_Y+5),
         Point((arrets[chemin[1]][1]-minLong)*ratio+5,
                delta-(arrets[chemin[1]][0]-minLat)*facteur_Y+5))
    affichage.setWidth(3)
    affichage.setFill("green")
    affichage.draw(win)
    for i in range(len(chemin)):
        if chemin[i]!=arrivee and chemin[i]!=depart:
            affichage = Line(Point((arrets[chemin[i]][1]-minLong)*ratio+5,
                        delta-(arrets[chemin[i]][0]-minLat)*facteur_Y+5),
                 Point((arrets[chemin[i+1]][1]-minLong)*ratio+5,
                        delta-(arrets[chemin[i+1]][0]-minLat)*facteur_Y+5))
            affichage.setWidth(3)
            affichage.setFill("green")
            affichage.draw(win)
            affichage = Circle(Point((arrets[chemin[i]][1]-minLong)*ratio+5,
                      delta-(arrets[chemin[i]][0]-minLat)*facteur_Y+5),4)
            affichage.setFill("green")
            affichage.draw(win)
            sleep(0.1)
    affichage = Circle(Point((arrets[arrivee][1]-minLong)*ratio+5,
              delta-(arrets[arrivee][0]-minLat)*facteur_Y+5),4)
    affichage.setFill("blue")
    affichage.draw(win)
    chemin.reverse()                                           #On inverse la liste pour obtenir le chemin depart->arrivée
    return (chemin,round(distance[indice_som(arrivee)][0]))            #On retourne le chemin et la distance entre ces deux arrets


def floyd_graphique(depart,arrivee,win):
    """Cette fonction prend en paramètres deux arrêts et renvoient le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en utilisant la 
    méthode de floyd wharshall."""
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
    affichage = Circle(Point((arrets[depart][1]-minLong)*ratio+5,
              delta-(arrets[depart][0]-minLat)*facteur_Y+5),4)
    affichage.setFill("blue")
    affichage.draw(win)
    affichage = Circle(Point((arrets[arrivee][1]-minLong)*ratio+5,
              delta-(arrets[arrivee][0]-minLat)*facteur_Y+5),4)
    affichage.setFill("blue")
    affichage.draw(win)
    #-------------------------------------

    n=len(nom_arrets) # Taille de la matrice
    k=0 # Numéro de l'étape (= tous les chemins de longueur <= k)
    for k in range(n):
        if nom(k)!=depart and nom(k)!=arrivee:
            affichage = Circle(Point((arrets[nom(k)][1]-minLong)*ratio+5,
                      delta-(arrets[nom(k)][0]-minLat)*facteur_Y+5),4)
            affichage.setFill("orange")
            affichage.draw(win)
        for i in range (n):
            for j in range (n):

                # Application de la formule permettant de passer de PN à PN+1
                if M0[k][j]+M0[i][k]<M0[i][j]:
                    M0[i][j]=M0[k][j]+M0[i][k]
                    P0[i][j]=P0[k][j]
        # Remarque : On écrase les matrices car toutes les informations sont contenues dans les matrices finales
    # Reconstruction
    arret_actuel=indice_som(arrivee)
    chemin=[nom(arret_actuel)]
    while arret_actuel!=indice_som(depart):

        pred=P0[indice_som(depart)][arret_actuel]
        chemin.append(nom(pred))
        arret_actuel=pred

    affichage = Circle(Point((arrets[depart][1]-minLong)*ratio+5,
              delta-(arrets[depart][0]-minLat)*facteur_Y+5),4)
    affichage.setFill("blue")
    affichage.draw(win)
    affichage = Line(Point((arrets[arrivee][1]-minLong)*ratio+5,
                delta-(arrets[arrivee][0]-minLat)*facteur_Y+5),
         Point((arrets[chemin[1]][1]-minLong)*ratio+5,
                delta-(arrets[chemin[1]][0]-minLat)*facteur_Y+5))
    affichage.setWidth(3)
    affichage.setFill("green")
    affichage.draw(win)
    for i in range(len(chemin)):
        if chemin[i]!=arrivee and chemin[i]!=depart:
            affichage = Line(Point((arrets[chemin[i]][1]-minLong)*ratio+5,
                        delta-(arrets[chemin[i]][0]-minLat)*facteur_Y+5),
                 Point((arrets[chemin[i+1]][1]-minLong)*ratio+5,
                        delta-(arrets[chemin[i+1]][0]-minLat)*facteur_Y+5))
            affichage.setWidth(3)
            affichage.setFill("green")
            affichage.draw(win)
            affichage = Circle(Point((arrets[chemin[i]][1]-minLong)*ratio+5,
                      delta-(arrets[chemin[i]][0]-minLat)*facteur_Y+5),4)
            affichage.setFill("green")
            affichage.draw(win)
            sleep(0.1)
    affichage = Circle(Point((arrets[arrivee][1]-minLong)*ratio+5,
              delta-(arrets[arrivee][0]-minLat)*facteur_Y+5),4)
    affichage.setFill("blue")
    affichage.draw(win)
    
    chemin.reverse()                                            #On inverse la liste pour obtenir le chemin dans le bon ordre (départ vers arrivée)
    return (chemin,round(M0[indice_som(depart)][indice_som(arrivee)]))

def dessinerGraphe():
    win.delete('all')
    fond_carte = Image(Point(int(windowWidth/2),int(windowHeight/2)+1), "fond_carte.png")
    fond_carte.draw(win)

    for i in arrets:
        for j in arrets[i][2]:
            tracerArc(i,j)
    for i in arrets:
        afficherArret(i,"black",False)
        
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
            ford_graphique(arret1,arret2,win)
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
