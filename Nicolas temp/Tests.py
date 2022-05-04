from cmath import inf
import json as js
from time import sleep
from xml.dom.expatbuilder import theDOMImplementation
import pandas as pd
from math import sin, cos, acos, pi
import numpy as np
donneesbus=pd.read_csv(r'./donneesbus.csv',sep=';')

arrets={}
for c in range (len( donneesbus)):
    arrets[donneesbus['arret'][c]]=[float(donneesbus['lattitude'][c].replace(",",".")),float(donneesbus['longitude'][c].replace(",",".")),list(donneesbus['listesucc'][c].replace('[','').replace(']','').replace("'","").replace(" ","").split(","))]

nom=list(arrets.keys())










nom_arrets=[]
for i in arrets:
    nom_arrets.append(i)

def nom(ind):
    """Cette fonction retourne le nom d'un arrêt en fonction par son indice dans la liste de nom"""
    return nom_arrets[ind]

def indice_som(nom_som):
    """Cette fonction retourne l'indice d'un arrêt en fonction par son nom dans la liste de nom"""
    return nom_arrets.index(nom_som)

def latitude(nom_som):
    return arrets[nom_som][0]

def longitude(nom_som):
    return arrets[nom_som][1]

def coordonnes(nom_som):
    return latitude(nom_som),longitude(nom_som)

def voisin(nom_som):
    return arrets[nom_som][2]


#Question D

def dic_adjacence(donnees):
    dic={}                                                                              #Création d'un dictionnaire vide
    for i in donnees:                                                            #Récupération des clés du dictionnaires "donnees"
        dic[i]=donnees[i][2]                                                            #Récupération des arrêts succedant de l'arrêts i
    return dic                                                                          #Retour du dictionnaire d'adjacence crée


dic_bus=dic_adjacence(arrets)







def lst_adjacence(donnees):
    """Cette fonction renvoie une matrice d'ajacence à partir d'un dictionnaire d'adjacence
    """
    lst = [[0]*len(donnees) for _ in range(len(donnees))]                #Création d'un tableau à double entrées initialisé à 0 pour tous les arrêts

    for c in arrets:                                                                    #Pour tous les arrêts dans le dictionnaires des arrêts
        succ=voisin(c)                                                                  #On enregistre la liste des arrêts succedant de l'arrêt c
        for i in succ:                                                                  #Pour tous ses successeurs
            lst[indice_som(c)][indice_som(i)]=1                                         #On ajoute l'adjacence entre les deux arrêts
    
    return lst                                                                          #Retour de la matrice d'adjacence

mat_bus=lst_adjacence(arrets)






#Question E

def distanceGPS(latA,latB,longA,longB):
# Conversions des latitudes en radians
    ltA=latA/180*pi
    ltB=latB/180*pi
    loA=longA/180*pi
    loB=longB/180*pi
    # Rayon de la terre en mètres (sphère IAG-GRS80)
    RT = 6378137
    # angle en radians entre les 2 points
    S = acos(round(sin(ltA)*sin(ltB) + cos(ltA)*cos(ltB)*cos(abs(loB-loA)),14))
    # distance entre les 2 points, comptée sur un arc de grand cercle
    return S*RT



def distarrets(arret1,arret2):
    """Cette fonction retourne la distance en mètres entre deux arrets grâce a leurs coordonnées GPS"""
    lat1=latitude(arret1)       #Recuperation de la latitude de l'arret1
    lat2=latitude(arret2)       #Recuperation de la latitude de l'arret2

    long1=longitude(arret1)     #Recuperation de la longitude de l'arret1
    long2=longitude(arret2)     #Recuperation de la longitude de l'arret2

    return distanceGPS(lat1,lat2,long1,long2) #Appel et retour du résultat de la fonction de calcule à vol d'oiseau de deux points GPS


def distarc(arret1,arret2):
    """Cette fonction renvoie la distance en mètres entre deux arrêts donnés en paramètres:
                - Si l'arret2 est un successeur de l'arret1 le retour sera la distance a vol d'oiseau entre ces deux arrêts
                - Si l'arret2 n'est pas un successeur de l'arret1 le retour sera une distance infinie
    """
    
    if arret2 in voisin(arret1) or arret1==arret2 :               #Si l'arret2 est un successeur de l'arret1          
        res=distarrets(arret1,arret2)           #Appel de la fonction calculant la distance des deux arrêts
    else:                                       #Sinon
        res=np.Inf                              #La distance est dite Infinie
    return res





# Question F 
poids_bus=[x[:] for x in mat_bus]                     #Copie profonde de la matrice d'adjacence qui possède le même ordre


for i in range (len(poids_bus)):                      #On parcours la matrice poids_bus
    for y in range(len(poids_bus[i])):                
        poids_bus[i][y]=distarc(nom(i),nom(y))        #On y inscrit la distance entre les deux arrêts selectionnés [floatant ou Infini]





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





def djiksrta(depart,arrive):
    '''Cette fonction prend en paramètres deux deux arrêts et renvoient le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en
     utilisant la méthode de djiksrta.'''
    
    distance=[(np.Inf,None) for _ in range(len(nom_arrets))]            #Tous les arrets ont une distances infinie et pas de pred
    marque=[indice_som(depart)]                                         #Liste de tous les arrets dont la distance minimum a déjà était trouvé
    distance[indice_som(depart)]=(0,indice_som(depart))                 #On ajoute la distance de l'arret de départ soit 0, son pred est lui même
    arret_actuel=indice_som(depart)                                     #arret_actuel est l'arret a partir du quel on va effectuer l'étape
    while arret_actuel!=indice_som(arrive):                             #On peut raccourcir djikstra en s'arretant dès que l'arret actuel est celui d'arrivé

        for proche in voisin(nom(arret_actuel)):                                                                              #Pour tous les arrets voisins de l'arret observé                           
            if indice_som(proche) not in marque:                                                                              #Si l'arret n'est pas déjà marqué (on pourra pas l'ameliorer de toute facon)
                if distance[indice_som(proche)][0]>distance[arret_actuel][0]+distarc(nom(arret_actuel),proche):               #Si ce nouveau chemin est plus avantageux que l'ancien 
                    distance[indice_som(proche)]=(distance[arret_actuel][0]+distarc(nom(arret_actuel),proche),arret_actuel)   #On met a jour sa distance et son prédécesseu
        arret_actuel=min_exclude(distance,marque)                      #On récupere l'arret avec la distance minimale parmis les arrets non marqués
        marque.append(arret_actuel)                                    #On ajoute l'arret actuel dans les arrets marqués                                  

    #-------------------------------reconstruction---------------------------------------
    chemin=[arrive]                                             #On crée une liste de allant de l'arrivée vers le depart
    arret_actuel=indice_som(arrive)                             #On parcours les arrets en commançant par l'arrivée
    while arret_actuel!=indice_som(depart):                     #Tant que l'arret actuel n'est pas le départ on continue le chemin                   
        pred=distance[arret_actuel][1]                          #Prédécesseur de l'arret actuel   
        chemin.append(nom(pred))                                #On ajoute le Prédécesseur au chemin 
        arret_actuel=pred                                       #L'arret actuel devient le Prédécesseur
        

    chemin.reverse()                                           #On inverse la liste pour obtenir le chemin depart->arrivée
    return (chemin,distance[indice_som(arrive)][0])            #On retourne le chemin et la distance entre ces deux arrets

            

def difference(nouvelle,ancienne):
    """Renvois les indices des valeurs differentes dans une listes
        - len(liste1)==len(liste2)""" 
    res=[] 
    for y in range(len(nouvelle)):
        if nouvelle[y]!=ancienne[y]: #Si les deux valeurs (ici des distances) sont différentes
            res.append(y)            #On ajoute l'indice i (representant un arret) à la liste de retours
    return res                       #On retourne la liste de tout les indices(arrets) ayant une valeur(distance) changée


def ford(depart,arrive):
    """Cette fonction prend en paramètres deux deux arrêts et renvoient le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en utilisant la 
    méthode de bellman."""
    distance=[(np.Inf,None) for _ in range(len(nom_arrets))]    #Tous les arrets ont une distances infinie et pas de pred
    distance[indice_som(depart)]=(0,indice_som(depart))         #On ajoute la distance de l'arret de départ soit 0, son pred est lui même
    a_traiter=[indice_som(depart)]                              #Une liste de tous les arrets que l'ont doit traiter
    while a_traiter!=[]:                                        #Tant que cette liste n'est pas vide on continue la recherche, on assume donc qu'il n'y a pas de chemins absorbants
        distancepred=distance[:]                                #Copie de la liste de distance afin de la comparer après l'étape

        for node in a_traiter:                                                                          #L'arrets en cours de traitement                                                                      
            for proche in voisin(nom(node)):                                                            #Pour tous les arrets voisins de l'arret observé
                if distance[indice_som(proche)][0]>distance[node][0]+distarc(nom(node),proche):         #Si ce nouveau chemin est plus avantageux que l'ancien      
                    distance[indice_som(proche)]=(distance[node][0]+distarc(nom(node),proche),node)     #On met a jour sa distance et son prédécesseur 
        a_traiter=difference(distance,distancepred)             #on récupere tous les arrets qui ont était mis a jour dans l'étape
                                                                #Opération faite après l'étape pour ne pas interferer avec les données de l'étape
    
    #-------------------------------reconstruction---------------------------------------
    chemin=[arrive]                                             #On crée une liste de allant de l'arrivée vers le depart
    arret_actuel=indice_som(arrive)                             #On parcours les arrets en commançant par l'arrivée
    while arret_actuel!=indice_som(depart):                     #Tant que l'arret actuel n'est pas le départ on continue le chemin                   
        pred=distance[arret_actuel][1]                          #Prédécesseur de l'arret actuel   
        chemin.append(nom(pred))                                #On ajoute le Prédécesseur au chemin 
        arret_actuel=pred                                       #L'arret actuel devient le Prédécesseur
        

    chemin.reverse()                                           #On inverse la liste pour obtenir le chemin depart->arrivée
    return (chemin,distance[indice_som(arrive)][0])            #On retourne le chemin et la distance entre ces deux arrets
    





def floyd(depart,arrive):
    """Cette fonction prend en paramètres deux deux arrêts et renvoient le plus court chemin, sous forme de la liste des arrêts parcourus ainsi, que la distance minimum en utilisant la 
    méthode de floyd wharshall."""
    M=[[x[:] for x in poids_bus]]                               #Creation de M0
    #------------Creation de P0---------
    P=[[x[:] for x in poids_bus]]
    print(len(P[0]))                                            
    for i in range (len(P[0])):
        for j in range(len(P[0])):
            if P[0][i][j]==np.Inf or P[0][i][j]==0:
                P[0][i][j]=None
            else:
                P[0][i][j]=i
    #-------------------------------------

    for k in range(1,len(M[0])):
        M.append([x[:] for x in M[k-1]])
        P.append([x[:] for x in P[k-1]])
        for i in range(len(M[0])):
            for j in range(len(M[0])):
                if 

                





                    
    chemin=[arrive]                                             #On crée une liste de allant de l'arrivée vers le depart
    arret_actuel=indice_som(arrive)                             #On parcours les arrets en commançant par l'arrivée
    while arret_actuel!=indice_som(depart):                     #Tant que l'arret actuel n'est pas le départ on continue le chemin                   
        pred=P[k][arret_actuel][indice_som(depart)]                          #Prédécesseur de l'arret actuel   
        chemin.append(nom(pred))                                #On ajoute le Prédécesseur au chemin 
        print(f"le pred de {nom(arret_actuel)} est {nom(pred)}")
        sleep(0.2)
        arret_actuel=pred                                       #L'arret actuel devient le Prédécesseur
        
        

    chemin.reverse()                                           #On inverse la liste pour obtenir le chemin depart->arrivée
    return (chemin,M[k][arret_actuel][indice_som(depart)])            #On retourne le chemin et la distance entre ces deux arrets           
        
        
    





#print(ford('PRIM','MONT')==djiksrta('PRIM','MONT'))
print(floyd('PRIM','MONT'))
