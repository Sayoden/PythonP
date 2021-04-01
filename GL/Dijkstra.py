from collections import deque
def dijkstra(graph, vertex):
    queue = deque([vertex])
    distance = {vertex: 0}
    while queue:
        t = queue.popleft()
        print("On visite le sommet " + str(t))
        for voisin in graph[t]:
            queue.append(voisin)
            nouvelle_distance = distance[t] + graph[t][voisin]
            if(voisin not in distance or nouvelle_distance < distance[voisin]):
                distance[voisin] = nouvelle_distance
                print("Met à jour le sommet " + str(voisin) + " avec la distance : " + str(nouvelle_distance))

    return distance
#Liste d'ajacence du graphe
graph = {'A':{'B':3,'C':4},'B':{'E':2},'C':{'D':0},'D':{'F':3},'E':{'F', 1}}
distance = dijkstra(graph,'A')
print("Distances" + str(distance))