def sommeColonnesPaires(liste):
    """
    :param liste: list[][]
    :return: list[]
    """
    listfinale = []

    for i in range(len(liste)):

        tempList = liste[i]

        somme = 0
        for n in range(0, len(tempList)):
            print(tempList[n])
            if (tempList[n] % 2) == 0:
                somme += tempList[n]
        listfinale.append(somme)

    return listfinale


liste = [[7,3,5,2], [9,1,6,8], [2,4,1,9]]
print(sommeColonnesPaires(liste))


