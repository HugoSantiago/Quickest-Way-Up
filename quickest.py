
import math
import os
import random
import re
import sys
import dijkstra

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
infi = 1000000000
class Node:
    def __init__(self, vertexNumber):       
        self.vertexNumber = vertexNumber
        self.children = []
   
    def Add_child(self, vNumber, length):   
        p = Pair(vNumber, length)
        self.children.append(p)
def dijkstraDist(g, s, path):
    dist = [infi for i in range(len(g))]
    visited = [False for i in range(len(g))]
    for i in range(len(g)):       
        path[i] = -1
    dist[s] = 0
    path[s] = -1
    current = s
    sett = set()
    while (True):
        visited[current] = True
        for i in range(len(g[current].children)): 
            v = g[current].children[i].first;           
            if (visited[v]):
                continue
            sett.add(v)
            alt = dist[current] + g[current].children[i].second
   
            if (alt < dist[v]):      
                dist[v] = alt
                path[v] = current;       
        if current in sett:           
            sett.remove(current);       
        if (len(sett) == 0):
            break
        minDist = infi
        index = 0
        for a in sett:       
            if (dist[a] < minDist):          
                minDist = dist[a]
                index = a;          
        current = index;  
    return dist
      
def quickestWayUp(ladders, snakes):
    result = -1
    iniLadders = [i[0] for i in ladders]

    v = []
    n = 100
    s = 0
    for i in range(n):
        a = Node(i)
        v.append(a)
    
    for i in range(n):
        for j in range(1,7):
            if i+j <= 99:
                v[i].Add_child(i+j,1)
    
    for i in ladders:
        v[i[0]].Add_child(i[1],0)
    
    for i in snakes:
        v[i[0]].Add_child(i[1],0)
    
    path = [0 for i in range(len(v))]
    
    result = dijkstraDist(v, s, path)[-1]
    return result

def main():
    fptr = open('myTest.txt', 'r')
    
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

        #fptr.write(str(result) + '\n')
        print(result)

    fptr.close()

# Starting point
main()