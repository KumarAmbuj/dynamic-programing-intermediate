def findmaxcoin(arr):
    flag=1
    m=len(arr)
    n=len(arr[0])
    dp=[[0 for j in range(n)]for i in range(m)]

    for i in range(m):
        if flag==1:
            for j in range(n):
                if i==0 and j==0 and arr[i][j]=='E':
                    dp[i][j]=0
                elif i == 0 and j == 0 and arr[i][j] == 'C':
                    dp[i][j]=1

                elif j==0:
                    if arr[i][j]=='C':
                        dp[i][j]=dp[i-1][j]+1
                        flag=1-flag
                    elif arr[i][j]=='E':
                        dp[i][j]=dp[i-1][j]

                    elif arr[i][j]=='#':
                        dp[i][j]=None
                elif i==0:
                    if arr[i][j]=='#':
                        dp[i][j]=None
                    elif arr[i][j]=='E':
                        if dp[i][j-1]!=None:
                            dp[i][j]=dp[i][j-1]
                        else:
                            dp[i][j]=None
                    elif arr[i][j]=='C':
                        if dp[i][j-1]!=None:
                            dp[i][j]=dp[i][j-1]+1
                        else:
                            dp[i][j]=None


                else:
                    if arr[i][j]=='#':
                        dp[i][j]=None
                    elif arr[i][j]=='E':
                        if dp[i-1][j]==None:
                            dp[i][j]=dp[i][j-1]
                        elif dp[i][j-1]==None:
                            dp[i][j]=dp[i-1][j]
                            flag=1-flag
                        else:
                            mx=max(dp[i-1][j],dp[i][j-1])
                            if mx==dp[i-1][j]:
                                dp[i][j]=dp[i-1][j]
                                flag=1-flag
                            else:
                                dp[i][j]=dp[i][j-1]
                    elif arr[i][j]=='C':
                        if dp[i-1][j]==None:
                            dp[i][j]=dp[i][j-1]+1
                        elif dp[i][j-1]==None:
                            dp[i][j]=dp[i-1][j]+1
                            flag=1-flag
                        elif dp[i-1][j]!=None and dp[i][j-1]!=None:
                            mx=max(dp[i-1][j],dp[i][j-1])
                            if mx==dp[i-1][j]:
                                dp[i][j]=dp[i-1][j]+1
                                flag=1-flag
                            else:
                                dp[i][j]=dp[i][j-1]+1




        elif flag==0:
            for j in range(n-1,-1,-1):

                if j == n-1:
                    if arr[i][j] == 'C':
                        dp[i][j] = dp[i - 1][j] + 1
                        flag = 1 - flag
                    elif arr[i][j] == 'E':
                        dp[i][j] = dp[i - 1][j]

                    elif arr[i][j] == '#':
                        dp[i][j] = None

                else:
                    if arr[i][j] == '#':
                        dp[i][j] = None
                    elif arr[i][j] == 'E':
                        if dp[i - 1][j] == None:
                            dp[i][j] = dp[i][j + 1]
                        elif dp[i ][j+1] == None:
                            dp[i][j] = dp[i - 1][j]
                            flag = 1 - flag
                        else:
                            mx = max(dp[i - 1][j], dp[i][j - 1])
                            if mx == dp[i - 1][j]:
                                dp[i][j] = dp[i - 1][j]
                                flag = 1 - flag
                            else:
                                dp[i][j] = dp[i][j + 1]
                    elif arr[i][j] == 'C':
                        if dp[i - 1][j] == None:
                            dp[i][j] = dp[i][j + 1] + 1

                        elif dp[i ][j+1] == None:
                            dp[i][j] = dp[i - 1][j] + 1
                            flag = 1 - flag
                        else:
                            mx = max(dp[i - 1][j], dp[i][j - 1])
                            if mx == dp[i - 1][j]:
                                dp[i][j] = dp[i - 1][j] + 1
                                flag = 1 - flag
                            else:
                                dp[i][j] = dp[i][j + 1] + 1

    mx=0
    for i in range(m):
        for j in range(n):
            if dp[i][j]!=None:
                mx=max(mx,dp[i][j])

    print(mx)
    for i in range(len(dp)):
        print(dp[i])

arr = [ ['E', 'C', 'C', 'C', 'C'],
          ['C', '#', 'C', '#', 'E'],
          ['#', 'C', 'C', '#', 'C'],
          ['C', 'E', 'E', 'C', 'E'],
          ['C', 'E', '#', 'C', 'E'] ]
findmaxcoin(arr)
