class Path():
    def __init__(self,i,j,l,psf):
        self.i=i
        self.j=j
        self.l=l
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



def findlcs(s1,s2):

    m=len(s1)
    n=len(s2)

    dp=[[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if s1[i]==s2[j]:
                dp[i][j]=dp[i+1][j+1]+1
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])

    print(dp[0][0])
    printinglcs(dp,s1,s2)
def printinglcs(dp,s1,s2):
    queue=Queue()

    Enqueue(queue,Path(0,0,dp[0][0],''))
    while(Size(queue)):
        rem=Dequeue(queue)
        if rem.l==0:
            print(rem.psf)
        else:
            if s1[rem.i]==s2[rem.j]:
                Enqueue(queue,Path(rem.i+1,rem.j+1,rem.l-1,s1[rem.i]+rem.psf))
            else:
                l=dp[rem.i][rem.j]
                if l==dp[rem.i][rem.j+1] and l==dp[rem.i+1][rem.j]:
                    if ord(s1[rem.i+1])<ord(s2[rem.j+1]):
                        Enqueue(queue,Path(rem.i+1,rem.j,rem.l,rem.psf))
                        Enqueue(queue, Path(rem.i, rem.j + 1, rem.l, rem.psf))
                    else:
                        Enqueue(queue,Path(rem.i,rem.j+1,rem.l,rem.psf))
                        Enqueue(queue, Path(rem.i + 1, rem.j, rem.l, rem.psf))
                else:
                    if l==dp[rem.i][rem.j+1]:
                        Enqueue(queue,Path(rem.i,rem.j+1,rem.l,rem.psf))
                    elif l==dp[rem.i+1][rem.j]:
                        Enqueue(queue,Path(rem.i+1,rem.j,rem.l,rem.psf))



s1 = "abcabcaa"
s2 = "acbacba"
findlcs(s1,s2)