def findmaxvalue(num,arr,max):
    n = len(arr)

    dp=[[0 for j in range(max+1)] for i in range(n)]


    for i in range(n):
        for j in range(max+1):

            if i==0:
                if num-arr[i]==j or num+arr[i]==j:
                    dp[i][j]=1
                else:
                    dp[i][j]=0

            else:

                if j-arr[i]>=0 and j+arr[i]<=max:

                    if dp[i-1][j-arr[i]]==1 or dp[i-1][j+arr[i]]==1:
                        dp[i][j]=1
                elif j-arr[i]>=0:
                    dp[i][j]=dp[i-1][j-arr[i]]
                elif j+arr[i]<=max:
                    dp[i][j]=dp[i-1][j+arr[i]]
                else:
                    dp[i][j]=0

    ans=0
    for j in range(max,-1,-1):
        if dp[n-1][j]==1:
            ans=j
            break
    print(ans)

arr = [3, 10, 6, 4, 5]
num=1
max=15
findmaxvalue(num,arr,max)