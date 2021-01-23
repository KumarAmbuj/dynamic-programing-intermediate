class Path:
    def __init__(self,i,j,l,s,e):
        self.i=i
        self.j=j
        self.l=l
        self.s=s
        self.e=e
def Queue():
    queue=[]
    return queue
def Enqueue(q,s):
    q.append(s)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)


def findlps(s):
    dp=[[0 for i in range(len(s))] for j in range(len(s))]


    for g in range(len(s)):
        i=0
        j=g
        while(j<len(s)):
            if g==0:
                dp[i][j]=1

            elif g==1:
                if s[i]==s[j]:
                    dp[i][j]=2
                else:
                    dp[i][j]=1

            else:
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i+1][j])
            i+=1
            j+=1
    print(dp[0][len(s)-1])
    printpalindrome(s,dp)


def printpalindrome(s,dp):
    queue=Queue()

    Enqueue(queue,Path(0,len(s)-1,dp[0][len(s)-1],'',''))

    while(Size(queue)):

        rem=Dequeue(queue)

        if rem.l==0:

            res=rem.s+rem.e
            print(res)
        elif rem.l==1:
            res=rem.s+s[rem.i]+rem.e
            print(res)
        else:
            if s[rem.i] == s[rem.j]:
                Enqueue(queue, Path(rem.i + 1, rem.j - 1, rem.l - 2, rem.s + s[rem.i], s[rem.j] + rem.e))
            else:
                if dp[rem.i][rem.j] == dp[rem.i][rem.j - 1]:
                    Enqueue(queue, Path(rem.i, rem.j - 1, rem.l, rem.s, rem.e))
                if dp[rem.i][rem.j] == dp[rem.i + 1][rem.j]:
                    Enqueue(queue, Path(rem.i + 1, rem.j, rem.l, rem.s, rem.e))

s='BBABCBCAB'
findlps(s)

s='ABKCCBC'
findlps(s)

s='GEEKSFORGEEKS'
findlps(s)
