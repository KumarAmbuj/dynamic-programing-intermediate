def findcount(n):
    a=[0 for i in range(n+1)]
    b=[0 for i in range(n+1)]
    c=[0 for i in range(n+1)]
    a[1]=1
    b[1]=1
    c[1]=1
    bcount=0
    ccount=0

    for i in range(2,n+1):
        a[i]=a[i-1]+b[i-1]+c[i-1]
        b[i]=(a[i-1]-bcount)+(c[i-1]-bcount)
        if n>=3:
            c[i]=a[i-1]-ccount
            c[i]+=(b[i-1]-ccount)
            ccount=ccount+c[i-2]
            c[i]+=(c[i-1]-ccount)
        elif n<3:
            c[i] = b[i - 1] + a[i - 1] + c[i - 1]
        bcount=2*bcount+b[i-1]

    ans=a[n]+b[n]+c[n]
    print(ans)

findcount(4)
findcount(5)

