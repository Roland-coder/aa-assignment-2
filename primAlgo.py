
#initializing arbitarily large value that would be used to set the minimum weights in our graph operation
# This number is initailly very large so that once we begin our graph  operation, its value needs to be larger than the initail weight in our graph structure
# that we choose to start from and get the minimum spanning tree

INF = 9999999

# Initailize a variable that holds the number of vertices in our graph
V = 7

# Initialize graph structure. the structure used here is an adjacency matrix, where the first indeices contain the individual vertices on the graph
# The second indices or dimension, contain a representation of how the individual vertices relate with the other vertices in the graph
# Created a list tha has 7 elements, which are the number of vertices in our graph
# every element in the list is a list itslef, having 7 elements based on the number of vertices in the graph
# To get the relationship between the vertices, G[i][j] >= 1 indicate that there is an edge between vertex i and j and the value in that index is the weight between the two edges


G = [[0, 28, 0, 0, 0, 10, 0],
     [28, 0, 16, 0, 0, 0, 14],
     [0, 16, 0, 12, 0, 0, 0],
     [0, 0, 12, 22, 0, 0, 18],
     [0, 0, 0, 22, 0, 25, 24],
     [10, 0, 0, 0, 25, 0, 0],
     [0, 14, 0, 8, 24, 0, 0]]

#Initializing list that has 7 elements indicating the number of vertices in the graph
#This list will be used to select vertices that would be used to get minimum spanning trees by selecting individual vertices and checking the edges and weights around them
selected = [0, 0, 0, 0, 0, 0, 0]

# Initializing a values that holds the number of edges left in the graph
# this value will be updated in our loop below
no_edge = 0

# Selecting the vertex we will be starting with
# the instructions stated that we start at vertex 6 and our graph structure starts from 1
# Since we are implementing this in python, we select index 5 to represent the 6th vertex since Python starts indexing from 0 and not 1
selected[5] = True


# Printing the spanning tree 
print("Edge : Weight\n")

# While loop that runs so long as the number of edges is less than the number of vertices minus 1
# Again this is because we are using python and the indexing starts from zero hence why the implentation shows edges less than v-1 and not edges less than v
while (no_edge < V - 1):
   
    #Initializing minimum value as the arbitrarily large value initialized at the top
    minimum = INF
    # Initializing temporal values, x and y that would be used to hold previous and next vertex of the spanning tree
    x = 0
    y = 0
    # for lopp that runs till the number of vertices and checks if the loop operation number is same as selected value at the top
    for i in range(V):
        if selected[i]:
          #once we are at that vertex location, we then lop through it again to get minimum value found in the list
            for j in range(V):
                    # Ensure that the index selected is not same as location of vertex in graph and G[i][j] is not equal to zero
                if ((not selected[j]) and G[i][j]):  
                    #if the minimum valueis greater than the value at index G[i][j], we update the minimum value with our new 
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                    # pass values of i and j to x and y so that they can be printed to the console
                        x = i
                        y = j
    # print sequence of movement and the weight of the edge
    print(str(x+1) + "-" + str(y+1) + ":" + str(G[x][y]))
     #update select value with the next vertex
    selected[y] = True
     #Increment number of edges by 1
    no_edge += 1
