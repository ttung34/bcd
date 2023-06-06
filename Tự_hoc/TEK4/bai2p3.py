#lãi suất kép
#công thức lãi suất kép A=P*(1+r/n)**nt
p = int(input("so tien goc ban dau "))
t = float(input("so nam cho vay "))
r = float(input("lai suat danh nghia hang nam "))
n = float(input("so lan lai keo trong mot nam "))
a = p*(1+(r/n))**(n*t)
print(a)