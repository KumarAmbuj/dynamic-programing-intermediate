def findlength(arr,k):
    n=len(arr)
    dp=[[0 for i in range(len(arr))] for j in range(k)]

    for i in range(k):
        for j in range(n):

            if i==0:
                dp[i][j]=1
            elif j<i:
                dp[i][j]=0
            elif j>=i:
                for l in range(j):
                    if arr[l]<arr[j]:
                        dp[i][j]+=dp[i-1][l]
    sum=0
    for i in range(n):
        sum+=dp[k-1][i]
    print(sum)

arr=[2, 6, 4, 5, 7]
findlength(arr,3)

arr=[12, 8, 11, 13, 10, 15, 14, 16, 20]
findlength(arr,4)