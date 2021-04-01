def trianglePascal(n):
    """
    :param n: int
    :return: list[][]
    """
    liste = [[1],[1,1]]

    for i in range(0,n):

        if i == 0:
            print(liste[0])
        if i == 1:
            print(liste[1])
        if i != 0 and i != 1:
            liste.append([1])
            for j in range(1, i):
                liste[i].append(liste[i-1][j-1] + liste[i-1][j])
            liste[i].append(1)
            print(liste[i])
    return liste


print(trianglePascal(6))