#Algorithms-lab 13-all pairs shortest path
from collections import defaultdict
def PrintPath(intermediate,u,v):
    if intermediate[u][v] is None:
        print("INF")
        return
    if intermediate[u][v] == v:
        print(v)
        return
    PrintPath(intermediate,u,intermediate[u][v])
    PrintPath(intermediate,intermediate[u][v],v)
class mygraph(object):
 
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = [] # dictionary to store graph
  
    # function to add an edge between u and v with weight w
    def addedge(self,u,v,w):
        self.graph.append([u,v,w])

    def Floyd_Warshall(self):
        n=self.V
        INF=float('inf')
        D = [[INF for i in range(n)] for j in range(n)]#initialize all D[V][V] = INF      
        intermediate = [[None for i in range(n)] for j in range(n)]#initialize all intermediate[u][v] to null

        for m in range(n):
            D[m][m]=0
        for x in self.graph:
            D[x[0]][x[1]]=x[2]
            intermediate[x[0]][x[1]]=x[1]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if D[i][j]>(D[i][k]+D[k][j]):
                        D[i][j]=(D[i][k]+D[k][j])
                        intermediate[i][j] = k
        
        for i in range(n):
            for j in range(n):
                print("from",i,"to",j,"the shortest path is:")
                PrintPath(intermediate,i,j)
     

if __name__=='__main__':
    g=mygraph(6)
    g.addedge(0,2,1)
    g.addedge(0,3,2)
    g.addedge(2,4,4)
    g.addedge(4,5,3)
    g.addedge(2,5,3)
    g.addedge(3,5,2)
    g.Floyd_Warshall()
    
    
        