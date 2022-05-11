import pandas as pd
import numpy as np
import copy
from math import (pi,acos,sin,cos)


# Initialisation
donnees=pd.read_csv(r'./donnees.csv',sep=';')
arrets={}
for c in range (len(donnees)):
    arrets[donnees['arret'][c]]=[float(donnees['longitude'][c].replace(",",".")),
                                    float(donnees['lattitude'][c].replace(",",".")),
                                    list(donnees['listesucc'][c].replace('[','').replace(']','').replace("'","").replace(" ","").split(","))]
nom_arrets=list(arrets.keys())

def nom(ind):
    return nom_arrets[ind]

def indice_som(nom_som):
    return nom_arrets.index(nom_som)

def latitude(nom_som):
    return arrets[nom_som][0]

def longitude(nom_som):
    return arrets[nom_som][1]

def coordonnes(nom_som):
    return latitude(nom_som),longitude(nom_som)

def voisin(nom_som):
    return arrets[nom_som][2]

def dic_adjacence(donnees):
    dic={}
    for i in donnees:
        dic[i]=donnees[i][2]
    return dic

def liste_adjacence(donnees):
    lst = [[0]*len(donnees) for _ in range(len(donnees))]
    for c in arrets:
        succ=voisin(c)
        for i in succ:
            lst[indice_som(c)][indice_som(i)]=1
    return lst

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
    lat1=latitude(arret1)
    lat2=latitude(arret2)
    long1=longitude(arret1)
    long2=longitude(arret2)
    return distanceGPS(lat1,lat2,long1,long2)


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

mat_bus=liste_adjacence(arrets)
poids_bus=copy.deepcopy(mat_bus)                     #Copie profonde de la matrice d'adjacence qui possède le même ordre

for i in range (len(poids_bus)):                      #On parcours la matrice poids_bus
    for y in range(len(poids_bus[i])):                
        poids_bus[i][y]=distarc(nom(i),nom(y))        #On y inscrit la distance entre les deux arrêts selectionnés [floatant ou Infini]