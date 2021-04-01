from PIL import Image
import numpy as np
im=Image.open("image TP2.png") #à récupérer sur Moodle
T=np.array(im)

def transpose(): #Retrait de l'argument inutile
    l = len(T[0])
    newMatrice = []
    for i in range(l):
        saveTemp = []
        newMatrice.append(saveTemp)
        for colonne in range(len(T)):
            saveTemp.append(T[colonne][i])
    return(np.array(newMatrice))

im = Image.fromarray(transpose())
im.show()