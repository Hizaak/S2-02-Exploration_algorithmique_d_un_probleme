from donnees import *

# Dijkstra

def min_exclude(distance,marque):
    """Retourne l'indice du tableau de la valeur minimale en ignorant les valeurs des indices inscrit dans la liste marque"""
    min=-1                              #valeur par default marqueur d'erreur si aucun arret est trouvé
    for i in range (len(distance)):     #On parcours tout les arrets
        if i not in marque:                     #S'il n'est pas déjà marqué 
            if min==-1:                                                         
                min=i                               #La première valeur devient le minimum
            elif distance[i][0]<distance[min][0]:   #Si l'arret i à une distance inferieur a l'arret min
                min=i                               #L'arret i devient le nouveau min
    return min          #Retourne l'arret avec la distance minimale

def dijkstra(depart,arrive):
    '''Cette fonction prend en paramètres deux arrêts et renvoie le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en
    utilisant la méthode de Djiksrta.'''
    # Initialisation
    distance=[(np.Inf,None) for _ in range(len(nom_arrets))]
    distance[indice_som(depart)]=(0,indice_som(depart))                 # On ajoute la distance de l'arret de départ soit 0, son pred est lui même
    marque=[indice_som(depart)]                                         # Liste de tous les arrets dont la distance minimum a déjà été trouvée
    arret_actuel=indice_som(depart)                                     # arret_actuel est l'arret a partir du quel on va effectuer l'étape
    
    while arret_actuel!=indice_som(arrive):                             # On peut raccourcir djikstra en s'arretant dès que l'on doit traiter le sommet d'arrivée
        for proche in voisin(nom(arret_actuel)):                                                                              #Pour tous les arrets voisins de l'arret observé                           
            if indice_som(proche) not in marque:                                                                              #Si l'arret n'est pas déjà marqué (on pourra pas l'ameliorer de toute facon)
                if distance[indice_som(proche)][0]>distance[arret_actuel][0]+distarc(nom(arret_actuel),proche):               #Si ce nouveau chemin est plus avantageux que l'ancien 
                    distance[indice_som(proche)]=(distance[arret_actuel][0]+distarc(nom(arret_actuel),proche),arret_actuel)   #On met a jour sa distance et son prédécesseu
        arret_actuel=min_exclude(distance,marque)                      #On récupere l'arret avec la distance minimale parmis les arrets non marqués
        marque.append(arret_actuel)                                    #On ajoute l'arret actuel dans les arrets marqués                                  


    # Reconstruction
    arret_actuel=indice_som(arrive)                             #On parcours les arrets en commançant par l'arrivée
    chemin=[nom(arret_actuel)]                                       #On crée une liste de allant de l'arrivée vers le depart
    while arret_actuel!=indice_som(depart):                     #Tant que l'arret actuel n'est pas le départ on continue le chemin                   
        pred=distance[arret_actuel][1]                          #Prédécesseur de l'arret actuel   
        arret_actuel=pred                                       #L'arret actuel devient le Prédécesseur
        chemin.append(nom(arret_actuel))                        #On ajoute le Prédécesseur au chemin 

    chemin.reverse()                                            #On inverse la liste pour obtenir le chemin dans le bon ordre (départ vers arrivée)
    return (chemin,round(distance[indice_som(arrive)][0]))      # Renvoie : chemin (liste), distance (entier)


# Bellman-Ford Kalaba

def difference(nouvelle,ancienne):
    """Renvoie les indices des valeurs differentes dans une liste
        - len(liste1)==len(liste2)""" 
    diff=[]
    for y in range(len(nouvelle)):
        if nouvelle[y]!=ancienne[y]: #Si les deux valeurs (ici des distances) sont différentes
            diff.append(y)            #On ajoute l'indice i (representant un arret) à la liste de retours
    return diff                       #On retourne la liste de tout les indices(arrets) ayant une valeur(distance) changée


def ford(depart,arrive):
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

# Floyd-Warshall

def floyd(depart,arrive):
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