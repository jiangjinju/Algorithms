#Algorithms-Minimum Spanning Tree-Lab11
 
from collections import defaultdict
class mygraph(object):
 
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = [] # dictionary to store graph       
  
    # function to add an edge between u and v with weight w
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
 
    # Find function using path compression
    def find(self, parent, i):
        if parent[i] == i:#tree root
            return i
        return self.find(parent, parent[i])#recursively find the tree root
 
    #union function by rank(rank is tree depth)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Always attach smaller tree to bigger tree
        if rank[xroot] < rank[yroot]:#means x is smaller tree
            parent[xroot] = yroot #then attach y tree's root is the parent of x tree's root
        elif rank[xroot] > rank[yroot]: #otherwise x tree's root is y tree's root
            parent[yroot] = xroot

        else : #if same rank, then attach y tree to x tree, and the rank increased by 1
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # Kruskal's minimum spanning tree alogrithms
    def KruskalMST(self): 
        result =[] #output the spanining tree
 
        i = 0 # i is index for sorted edge, iteration from 0 till the end
        e = 0 # counting till n-1
        self.graph =  sorted(self.graph,key=lambda item: item[2])#sorted by edge weight in increasing order 
        parent = []
        rank = []
 
        # make disjoint sets
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
     
        # The maximum edge is vertices-1(n-1)
        while e < self.V -1 :
 
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent,u)
            y = self.find(parent,v)

            if x != y:#if not the same root, then union
                e = e + 1    
                result.append([u,v,w])
                self.union(parent, rank, x, y)            
 
        # print the contents of result[] to display the built MST
        print ("MST based on Kruskal algorithms and using rank and path compression")
        for u,v,weight  in result:
            #print str(u) + " -- " + str(v) + " == " + str(weight)
            print ("%d -- %d == %d" % (u,v,weight))
if __name__=='__main__':
    g =mygraph(7)
    g.addEdge(1, 2, 4)
    g.addEdge(1, 5, 2)
    g.addEdge(2, 3, 6)
    g.addEdge(2, 5, 5)
    g.addEdge(5, 6, 8)
    g.addEdge(6, 4, 7)
    g.addEdge(5, 3, 1)
    g.addEdge(0, 1, 9)
 
    g.KruskalMST()

            