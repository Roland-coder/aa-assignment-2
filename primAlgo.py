
INF = 9999999

V = 7

G = [[0, 28, 0, 0, 0, 10, 0],
     [28, 0, 16, 0, 0, 0, 14],
     [0, 16, 0, 12, 0, 0, 0],
     [0, 0, 12, 22, 0, 0, 18],
     [0, 0, 0, 22, 0, 25, 24],
     [10, 0, 0, 0, 25, 0, 0],
     [0, 14, 0, 8, 24, 0, 0]]

selected = [0, 0, 0, 0, 0, 0, 0]

no_edge = 0

selected[5] = True

print("Edge : Weight\n")
while (no_edge < V - 1):
   
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  
                    
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x+1) + "-" + str(y+1) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1
