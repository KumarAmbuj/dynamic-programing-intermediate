def findSubsets(arr,k):
    n=len(arr)

    dp=[[[] for i in range(n)] for j in range(n)]
    count=0
    for i in range(n):
        for j in range(n):
            if i==0:
                dp[i][j].append(j)
            elif j<i:
                dp[i][j].append(0)

            else:
                for m in range(j):

                    for l in range(len(dp[i-1][m])):

                        dp[i][j].append(dp[i-1][m][l]^arr[j])

                for l in range(len(dp[i][j])):
                    if dp[i][j][l]==k:
                        count+=1



    print(count)

arr = [1, 2, 3, 4, 5]
k = 4
findSubsets(arr,k)

arr = [6,9,4,2]
k = 6
findSubsets(arr,k)



