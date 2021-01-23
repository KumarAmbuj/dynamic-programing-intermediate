class Path():
    def __init__(self,i,j,val,psf):
        self.i=i
        self.j=j
        self.val=val
        self.psf=psf

def Queue():
    queue=[]
    return queue
def Enqueue(q,s):
    q.append(s)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)

def knapsack(w,wt,val):
    n=len(val)
    dp=[[0 for i in range(w+1)] for j in range(len(val)+1)]


    for i in range(1,n+1):
        for j in range(1,w+1):

            if j-wt[i-1]<0:
                dp[i][j]=dp[i-1][j]

            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-wt[i-1]]+val[i-1])

    print(dp[n][w])

    printpath(w,wt,val,dp)

def printpath(w,wt,val,dp):
    n=len(val)
    queue=Queue()

    Enqueue(queue,Path(n,w,dp[n][w],''))

    while(Size(queue)):

        rem=Dequeue(queue)

        if rem.val==0:
            print(rem.psf)


        else:

            if rem.val==dp[rem.i-1][rem.j]:
                Enqueue(queue,Path(rem.i-1,rem.j,rem.val,rem.psf+''))
            elif rem.val==dp[rem.i-1][rem.j-wt[rem.i-1]]+val[rem.i-1]:
                Enqueue(queue,Path(rem.i-1,rem.j-wt[rem.i-1],dp[rem.i-1][rem.j-wt[rem.i-1]],rem.psf+' '+str(wt[rem.i-1])))



val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
knapsack(W,wt,val)


val = [40, 100, 50, 60]
wt = [20, 10, 40, 30]
W = 60
knapsack(W,wt,val)





