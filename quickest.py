import Dijkstra.dijkstra
import Dijkstra.Node

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#    
def quickestWayUp(ladders, snakes):
    # List of first elements in ladders
    iniLadders = [i[0]-1 for i in ladders]
    # List of first elements in snakes
    iniSnakes = [i[0]-1 for i in snakes]
    # Vertex
    v = []
    # Number of nodes
    n = 100
    # Source
    s = 0

    for i in range(n):
        a = Dijkstra.Node.Node(i)
        v.append(a)
    
    # Loading the graph with basic edges (the movement of the dize)
    for i in range(n):
        if i not in iniLadders and i not in iniSnakes:
            for j in range(1,7):
                if i+j <= 99:
                    v[i].Add_child(i+j,1)
    # Loading the ladders nodes
    for i in ladders:
        v[i[0]-1].Add_child(i[1]-1,0)
    
    # Loading the snake nodes
    for i in snakes:
        v[i[0]-1].Add_child(i[1]-1,0)
    
    path = [0 for i in range(len(v))]
    
    dist = Dijkstra.dijkstra.dijkstraDist(v, s, path)[-1]
    
    #In case the node is not reacheable 
    if dist == 1000000000:
        dist = -1
    return dist

def main():
    fptr = open('test_files/myTest.txt', 'r')
    
    t = int(fptr.readline().strip())
    
    for t_itr in range(t):
        n = int(fptr.readline().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, fptr.readline().rstrip().split())))

        m = int(fptr.readline().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, fptr.readline().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        print(result)

    fptr.close()
