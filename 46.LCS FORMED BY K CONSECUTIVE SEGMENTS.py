def findlength(s1,s2,k):
    m=len(s1)
    n=len(s2)

    lcs=[[0 for j in range(n+1)] for i in range(m+1)]
    cnt = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            lcs[i][j]=max(lcs[i][j+1],lcs[i+1][j])

            if s1[i]==s2[j]:
                cnt[i][j]=cnt[i+1][j+1]+1

            if cnt[i][j]>=k:

                for a in range(k,cnt[i][j]+1):

                    lcs[i][j]=max(lcs[i][j],lcs[i+a][j+a]+a)
    print(lcs[0][0])

s1='aggasdfa'
s2='aggajasdfa'
k=4
findlength(s1,s2,k)

