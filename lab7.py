#SP2018-Algorithms-lab7-Dynamics Programming-LCS problem
#find the longest common subsequence string-LCS problem
#x is the first string, y is the second string, p is x last position, q is y last position
import numpy as np
def lcs(x,y,p,q):
    if p==-1 or q==-1:
        CACHE[p][q]=0
    elif CACHE[p][q]!=-1:
        return CACHE[p][q]
    elif x[p]==y[q]:
        Direction[p][q]=0
        CACHE[p][q]=1+lcs(x,y,p-1,q-1)
    else:
        v1=lcs(x,y,p-1,q)
        v2=lcs(x,y,p,q-1)
        if v1>v2:
            Direction[p][q]=1
            CACHE[p][q]=v1
        else:
            Direction[p][q]=2
            CACHE[p][q]=v2
    return CACHE[p][q]
                  
def printpath(x,y,p,q):
    if p>-1 and q>-1:
        if Direction[p][q]==0:
            printpath(x,y,p-1,q-1)
            print(x[p])
        elif Direction[p][q]==1:
            printpath(x,y,p-1,q)
        elif Direction[p][q]==2:
            printpath(x,y,p,q-1)
                  
x="djslkfdjsjkldsjff"
y="yuisyfjdslfjlkdie"
m=len(x)
n=len(y)
CACHE=np.zeros((m,n))-1
Direction=np.zeros((m,n))-1
        
print("the length is: ",lcs(x,y,m-1,n-1))
printpath(x,y,m-1,n-1)