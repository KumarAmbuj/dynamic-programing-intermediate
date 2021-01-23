def maxproduct(begin,end,arr,n,dp,sell):
    if dp[begin][end]!=-1:
        return dp[begin][end]
    year=(n-(end-begin))
    if begin==end:
        return year*arr[begin]

    x=arr[begin]*year+maxproduct(begin+1,end,arr,n,dp,sell)

    y=arr[end]*year+maxproduct(begin,end-1,arr,n,dp,sell)

    ans=max(x,y)
    dp[begin][end]=ans

    if x>=y:
        sell[begin][end]=0
    else:
        sell[begin][end]=1

    return ans






def findmaxproduct(arr):

    dp=[[-1 for j in range(10)] for i in range(10)]
    sell=[[0 for j in range(10)] for i in range(10)]
    n=len(arr)

    ans=maxproduct(0,n-1,arr,n,dp,sell)

    i=0
    j=n-1
    while(i<=j):

        if sell[i][j]==0:
            print('beg',end=' ')
            i+=1
        else:
            print('end',end=' ')
            j-=1

    print()
    print(ans)

    for i in range(10):
        print(dp[i])

    print('xxxxxxxx')
    for i in range(10):
        print(sell[i])

price = [ 2, 4, 6, 2, 5 ]
findmaxproduct(price)