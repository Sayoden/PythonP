import numpy as np

def moyennesMatieres(dico):
    # TBulletinDeNotes = dico(string : liste(nombre))
    # la clé est le nom d'une matiére
    # la valeur est la liste des notes obtenues dans cette matiére

    moyennes = {}
    for cle, valeur in dico.items():
        moyenne = 0
        nbNotes = 0
        print(len(valeur))
        for i in range(len(valeur)):
            nbNotes += 1
            moyenne += valeur[i]
        moyennes[cle] = moyenne/nbNotes
    return moyennes

def transposee(t):
    """
   Cette fonction définit la transposée d'une matrice t^T
   :param t: la matrice de départ
   :return: matrice qui est associé à la matrice transposée tA
   """
    t_T = []
    intt = len(t)
    o = len(t[0])
    for i in range(o) :
        e = []
        t_T.append(e)
        for j in range(intt):
            e.append(t[j][i])
    return np.array(t_T)

def supprimeMatière(matiere, promo):

    for etudiant in TPromotion :
        del etudiant [matiere]

print(transposee(np.array([[1,2,3],[4,5,6]])))
print(moyennesMatieres({'SE' : [11.5, 12, 11], 'SD': [12, 14]}))