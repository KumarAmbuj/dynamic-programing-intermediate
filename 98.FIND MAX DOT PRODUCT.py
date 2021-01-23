def findmaxDotproduct(arr1,arr2):
    m=len(arr1)
    n=len(arr2)

    dp=[[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(i,m+1):

            dp[i][j]=max(dp[i-1][j-1]+arr2[i-1]*arr1[j-1],dp[i][j-1])

    print(dp[n][m])

A = [2, 3 , 1, 7, 8]
B = [3, 6, 7]
findmaxDotproduct(A,B)


A = [1, 2, 3, 6, 1, 4]
B = [4, 5, 1]
findmaxDotproduct(A,B)
