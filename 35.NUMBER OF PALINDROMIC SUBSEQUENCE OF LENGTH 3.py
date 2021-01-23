def findnumber(s,m):
    n=len(s)
    l=[[0 for j in range(n)] for i in range(26)]
    r=[[0 for j in range(n)] for i in range(26)]

    l[ord(s[0])-ord('a')][0]=1

    for i in range(1,n):
        for j in range(26):

            l[j][i]+=l[j][i-1]

        l[ord(s[i])-ord('a')][i]+=1

    r[ord(s[n-1])-ord('a')][n-1]=1

    k=n-2
    while(k>=0):

        for j in range(26):

            r[j][k]+=r[j][k+1]
        r[ord(s[k])-ord('a')][k]+=1
        k-=1


    ans=0
    if m==1:
        for i in range(26):
            ans+=l[i][n-1]

    elif m==2:
        for i in range(26):
            a=l[i][n-1]
            if a>=2:
                ans+=a*(a-1)//2
    else:
        for i in range(1,n-1):
            for j in range(26):
                ans+=l[j][i-1]*r[j][i+1]

    print(ans)

s='abccbc'
k=2
findnumber(s,k)

