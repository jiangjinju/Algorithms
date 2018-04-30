#Algorithms-Dijkstra's Algorithms for Shortest Path with weighted edge-Lab12-final
import heapq

def dijkstra(adj, costs, s, t):
    Q = []     # priority queue of items; note item is mutable.
    d = {s: 0} # vertex -> minimal distance
    Qd = {}    # vertex -> [d[v], parent_v, v]
    p = {}     # predecessor
    visited_set = set([s])

    for v in adj.get(s, []):
        d[v] = costs[s, v]
        item = [d[v], s, v]
        heapq.heappush(Q, item)
        Qd[v] = item

    while Q:
        #print (Q)
        cost, parent, u = heapq.heappop(Q)
        if u not in visited_set:
            #print ('visit:', u)
            p[u]= parent
            visited_set.add(u)
            if u == t:
                return p, d[u]
            for v in adj.get(u, []):
                if d.get(v):
                    if d[v] > costs[u, v] + d[u]:
                        d[v] =  costs[u, v] + d[u]
                        Qd[v][0] = d[v]    # decrease key
                        Qd[v][1] = u       # update predecessor
                        heapq._siftdown(Q, 0, Q.index(Qd[v]))
                else:
                    d[v] = costs[u, v] + d[u]
                    item = [d[v], u, v]
                    heapq.heappush(Q, item)
                    Qd[v] = item

    return None

def make_undirected(cost):
    ucost = {}
    for k, w in cost.items():
        ucost[k] = w
        ucost[(k[1],k[0])] = w
    return ucost

if __name__=='__main__':

    # adjacent list
    adj = { 0: [1,3],
            1: [2,3],
            2: [4],
            3: [1,2,4],
            4: [0,2]}

    # edge costs
    cost = {(0,1):10,
            (0,3):5,
            (1,3):2,
            (3,1):3,
            (1,2):1,
            (2,4):4,
            (4,2):6,
            (3,2):9,
            (3,4):2,
            (4,0):7}

    #cost = make_undirected(cost)

    s=0
    for t,value in adj.items():        
        if t!=s:
            print(s,"to",t)
            predecessors, min_cost = dijkstra(adj, cost, s, t)
            c = t
            path = [c]
            print ('min cost:', min_cost)
            while predecessors.get(c):
                path.insert(0, predecessors[c])
                c = predecessors[c]

            print ('shortest path:', path)