def findLCS(P,Q,k):
    m=len(P)
    n=len(Q)

    dp=[[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):

            if P[i]==Q[j]:
                dp[i][j]=dp[i+1][j+1]+1
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])

    common=dp[0][0]

    sum=common
    for i in range(1,k+1):
        if m-common-i>=0:
            sum+=1
    print(sum)
P = [ 8, 3 ]
Q = [ 1, 3 ]
K = 1
findLCS(P,Q,K)

P = [ 1, 2, 3, 4, 5 ]
Q = [ 5, 3, 1, 4, 2 ]
K = 1
findLCS(P,Q,K)

a = [1,2,3,4]
b = [0,0,2,4]
k = 1
findLCS(a,b,k)