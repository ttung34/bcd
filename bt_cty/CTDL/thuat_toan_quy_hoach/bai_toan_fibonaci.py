# n = 100
# f=[0]*n
# f[0]=0
# f[1]=1
# for i in range(2,n):
#     f[i]=f[i-1]+f[i-2]
# print(f)

# Dãy con tăng dài nhất
n = 5
a= [1,7,3,5,6]
# BTCS
f = [0]*n
f[0]=1
for i in range(1,n):
    m=0
    for j in range(i):
        if a[j]<a[i]:
            if f[j]>m:
                m=f[j]
        f[i]=m+1
print(f)