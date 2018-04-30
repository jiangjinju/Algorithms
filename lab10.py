#Algorithms-lab 10-check the connectivity between u and v
from collections import defaultdict
class mygraph(object):
    def __init__(self,numofvertices):
        self.V=numofvertices
        self.graph=defaultdict(list)
    def addedge(self,v,u):
        self.graph[v].append(u)
        self.graph[u].append(v)
    def removeedge(self,v,u):
        self.graph[v].remove(u)
        self.graph[u].remove(v)
    def iscycle(self,v,visited,parent):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                return self.iscycle(i,visited,v)
            elif parent!=i:
                return True
        return False
    #DFS visit, set visited=True, default is false
    def DFS(self,u,visit):       
        visit[u]=True
        for i in self.graph[u]:
            if visit[i]==False:
                self.DFS(i,visit)
    #check whether it is reachable from u to v
    def reachable(self,u,v):
        visit=[False]*(self.V)    
        self.DFS(u,visit)
        if visit[v]==True:
            return True
        else:
            return False            

if __name__=='__main__':
    g=mygraph(6)
    g.addedge(0,2)
    g.addedge(0,3)
    g.addedge(2,4)
    g.addedge(4,5)
    g.addedge(1,5)
    g.removeedge(4,5)
    e1=4
    e2=5
    if g.reachable(e1,e2):
        print("it is connected between",e1,"and",e2)
    else:
        print("no connection between",e1,"and",e2)
        