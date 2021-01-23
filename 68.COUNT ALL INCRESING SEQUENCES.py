def findallcount(arr):
    n=len(arr)

    dp=[[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if i==0:
                dp[i][j]=1
            elif j<i:
                dp[i][j]=0
            else:
                for k in range(j):
                    if arr[k]<arr[j]:
                        dp[i][j]+=dp[i-1][k]
    count=0
    for i in range(n):
        for j in range(n):
            count+=dp[i][j]

    print(count)
arr = [1, 2, 3, 4]
findallcount(arr)

arr = [4,3,6,5]
findallcount(arr)


arr = [3, 2, 4, 5, 4]
findallcount(arr)
