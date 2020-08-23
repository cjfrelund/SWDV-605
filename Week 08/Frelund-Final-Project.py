# Frelund-Word-Ladder-Problem.py
#    A simple program that utilizes the Floyd-Warshall Algorithm to find the shortest distance in a matrix using a graph.
# by: Charles Frelund

# Floyd Warshall Algorithm in python

# The number of vertices
numberOfVertices = 9

INF = 999


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda rowVertex: list(
        map(lambda columnVertex: columnVertex, rowVertex)), G))

    # Adding vertices individually
    for vertex in range(numberOfVertices):
        for rowVertex in range(numberOfVertices):
            for columnVertex in range(numberOfVertices):
                distance[rowVertex][columnVertex] = min(
                    distance[rowVertex][columnVertex], distance[rowVertex][vertex] + distance[vertex][columnVertex])
    # Prints the total distance calculated based on the matrix.
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for rowVertex in range(numberOfVertices):
        for columnVertex in range(numberOfVertices):
            if(distance[rowVertex][columnVertex] == INF):
                print("INF", end=" ")
            else:
                print(distance[rowVertex][columnVertex], end="  ")
        print(" ")


G = [
    [0, 2, INF, 1, INF, INF, INF, INF, INF],
    [2, 0, 2, INF, 2, INF, INF, INF, INF],
    [INF, 2, 0, INF, 2, 2, INF, INF, INF],
    [1, INF, INF, 0, 1, INF, 1, INF, INF],
    [1, 2, 2, 1, 0, 2, 1, 1, INF],
    [INF, INF, 2, INF, 2, 0, INF, INF, 2],
    [INF, INF, INF, 1, 1, INF, 0, 1, INF],
    [INF, INF, INF, INF, 1, INF, 1, 0, 1],
    [INF, INF, INF, INF, 1, 2, INF, 1, 0]
]
floyd_warshall(G)
