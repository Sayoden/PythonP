from PIL import Image
import numpy as np
im=Image.open("image TP2.png") #à récupérer sur Moodle
T=np.array(im)

def permute_lignes(T):
    B = []

    #On parcours les lignes
    for l in range(len(T)):
        temp = []
        B.append(temp)

        #On parcours maintenant les colonnes
        for c in range(len(T[0])):

            #Colonnes... de temps = colonnes ... de A
            # -1 pour éviter le out of bounds
            temp.append(T[len(T)-l-1][c])

    return np.array(B)


im = Image.fromarray(permute_lignes(T))
im.show()