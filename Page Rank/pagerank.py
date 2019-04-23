G=[]
n=int(input("Enter number of pages:"))
print("Enter adjacency matrix:")

for i in range(n):
    d=input("Enter row {} for adjacency matrix: ".format(str(i+1))).split(' ')
    for i in range(len(d)):
        d[i] = int(d[i])
    
    G.append(d)


pagerank=[1.0/n for i in range(n)]
# L = [0 for i in range(n)]
# tol=1e-3
# alpha=0.85
outgoing=[0,0,0,0]
for i in range(n):
    for j in range(n):
        outgoing[i]+=G[i][j]

for i in range(n):
   pagerank[i]=pagerank[i]/outgoing[i]
   
prob=[0,0,0,0]
for i in range(n):
    for j in range(n):
        if G[i][j] == 1:
            prob[j]=prob[j]+pagerank[i]
            
            
print(prob)


