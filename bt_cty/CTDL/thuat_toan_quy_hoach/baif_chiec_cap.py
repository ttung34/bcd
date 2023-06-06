fi = open('balo.txt')
n,b = list(map(int,fi.readline())).split()
c=[]
w=[]
for i in  range(1,n+1):
    ci,wi = list(map(int,fi.readlines().split()))
    c.append(ci)
    w.append(wi)
print(c.w)
kq =[ [0]*(b+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1,b+1):
        kq[i][j]=kq[i-1][j]
        if j>=w[i]: #Neu nhu trong luong cho phet lon hin hoacj bang 
            kq[i][j] = max(kq[i-1][j], kq[i-1]-w[i]+c[i])

print(kq[n][b])
i = n
j = b
s=[]
while i!=0: 
    if kq[i][j]!= kq[i-1][j]:
        s.append(i)
        j=j-w[i]
    i-=1
print(s) 
    