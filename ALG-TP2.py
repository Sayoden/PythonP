#Je n'ai pas pu avancé j'ai aidé Louis



from PIL import Image
import numpy as np
im=Image.open("image TP2.png") #à récupérer sur Moodle
T=np.array(im)
#h,l=T.shape #hauteur, largeur de l'image


def diagonale(matrice):
    l = len(T[0])
    for i in range(len(T)): #on parcours la hauteur
        for b in range(l): #on parcours la longueur
            if i != b: #Donc on peut effacer le contenu de l'image
                T[i][b] = 0
    return(T)

im = Image.fromarray(diagonale(T))
im.show()
