import json as js
U = open("donneesbus.json", "r")
data = U.read()
U.close()
donneesbus= js.loads(data)
arrets=donneesbus.keys()
nom_arrets=[]
for i in arrets:
    nom_arrets.append(i)

def nom(ind):
    return nom_arrets[ind]

def indice_som(nom_som):
    return nom_arrets.index(nom_som)

def latitude(nom_som):
    return donneesbus[nom_som][0]

def longitude(nom_som):
    return donneesbus[nom_som][1]

def coordonnes(nom_som):
    return latitude(nom_som),longitude(nom_som)

def voisin(nom_som):
    return donneesbus[nom_som][2]

def dic_adjacence(donnees):
    dic={}
    for i in donnees.keys():
        dic[i]=donnees[i][2]
    return dic

def lst_adjacence(donnees):
    lst=[[0 for loop in range (len(nom_arrets))] for loop in range (len(nom_arrets))]
    for i in donnees.keys():
        for j in donnees[i][2]:
            lst[indice_som(i)][indice_som(j)]=1
    return lst

print(lst_adjacence(donneesbus))