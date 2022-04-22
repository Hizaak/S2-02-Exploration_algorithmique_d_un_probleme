import pandas as pd


#QUESTION A
df1=pd.read_csv('donneesbus.csv',sep=';')
dicarret={}
for c in range (len(df1)):
    dicarret[df1['arret'][c]]=[df1['lattitude'][c],df1['longitude'][c],df1['listesucc'][c].replace("'","").strip('][').split(', ')]


#QUESTION B
nom=[]
for c in dicarret:
    nom.append(c)



#QUESTION C
def nom_ind(ind):
    return nom[ind]

def indice_som(nom_som):
    return nom.index(nom_som)

def latitude(nom_som):
    return dicarret[nom_som][0]

def longitude(nom_som):
    return dicarret[nom_som][1]

def voisin(nom_som):
    return dicarret[nom_som][2]


#QUESTION D
mat_bus=[[None]*len(dicarret)]*len(dicarret)
for c in range (len(nom)):
    succ=voisin(nom[c])
    print(succ)
    for i in succ:
        
        mat_bus[c][indice_som(i)]=1
print(mat_bus)
    

    