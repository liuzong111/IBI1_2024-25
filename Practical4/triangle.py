#calculate the 1+2+...+n (n=1,2,...,10)
for n in range(1,11):
    T=0
    for i in range(n+1):
        T+=i
    print("T"+str(n)+"="+str(int(T)))