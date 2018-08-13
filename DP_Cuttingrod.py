#Algorithms-Lab9-Dynamic Programing-cutting rod problem
#c is unit cutting cost
#n is rod total length
import copy
def OPT(price,n,c):
    profit=[0 for x in range(n+1)]
    cutlength=[] #the lenght of each piece
    profit[0]=0    
    profit[1] = price[0]
    cutlength.append([])
    cutlength[0]=[]
    cutlength.append([])
    cutlength[1]=[]
    for i in range(2,n+1):
        cutlength.append([])
        m = price[i-1]
        cutindex=-1
        for j in range(1,i):
            if price[j-1]+profit[i-j]-c>m:
                m=price[j-1]+profit[i-j]-c
                cutindex=j
        profit[i]=m
        if(cutindex!=-1):
            cutlength[i]=copy.copy(cutlength[i-cutindex])
            cutlength[i].append(cutindex)
   
    return profit[n],cutlength[n]
#testing script
price_list=[3,4.5,8,9,10,17,17,20,22]
n=8 #rod length
c=1 #unit cutting cost
m,k=OPT(price_list,n,c)
print("max profit is: ",m)
sum=n
print("the cutting pieces are:")
for x in k:
    sum-=x
    print(x)
print(sum)