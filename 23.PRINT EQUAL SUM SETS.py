class Path:
    def __init__(self,sum,i,j,psf):
        self.sum=sum
        self.i=i
        self.j=j
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


def findEqualSum(arr):
    sum=0
    n=len(arr)
    for i in range(n):
        sum+=arr[i]

    if sum%2==1:
        print(-1)
        return
    else:
        sum=sum//2


    dp=[[False for j in range(sum+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(sum+1):

            if i==0 and j==0:
                dp[i][j]=True
            elif i==0:
                dp[i][j]=False
            elif j==0:
                dp[i][j]=True

            else:
                if j<arr[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]

    if dp[n][sum]==False:
        print(-1)
    else:
        findpath(arr,n,sum,dp)
def findpath(arr,n,sum,dp):
    queue=Queue()
    Enqueue(queue,Path(sum,n,sum,''))

    while(Size(queue)):
        rem=Dequeue(queue)

        if rem.i==0 or rem.j==0:
            print(rem.psf)
        else:
            if dp[rem.i-1][rem.j]==True:
                Enqueue(queue,Path(rem.sum,rem.i-1,rem.j,rem.psf+''))
            if rem.j-arr[rem.i-1]>=0:
                if dp[rem.i - 1][rem.sum - arr[rem.i - 1]] == True:
                    Enqueue(queue, Path(rem.sum - arr[rem.i - 1], rem.i, rem.j - arr[rem.i - 1],
                                        rem.psf + ' ' + str(arr[rem.i - 1])))





arr=[5, 5, 1, 11]
findEqualSum(arr)

