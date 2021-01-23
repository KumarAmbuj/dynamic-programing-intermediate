class Bag:
    def __init__(self,s,f,p):
        self.s=s
        self.f=f
        self.p=p
def Partition(arr,p,r):
    i=p-1
    x=arr[r]
    for j in range(p,r):
        if arr[j].s<x.s:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

def Quicksort(arr,p,r):
    if p<r:
        q=Partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)

def findjobscheduling(arr):

    narr=[]

    for i in range(len(arr)):
        narr.append(Bag(arr[i][0],arr[i][1],arr[i][2]))

    Quicksort(narr,0,len(narr)-1)

    dp=[0 for i in range(len(narr))]

    for i in range(len(narr)):
        mx=0
        for j in range(i):
            if narr[j].f<=narr[i].s:
                mx=max(mx,dp[j])
        dp[i]= mx + (narr[i].p)
    mx=0
    for i in range(len(narr)):
        mx=max(mx,dp[i])
    print(mx)

arr = [[3, 10, 20],
       [1, 2, 50],
       [6, 19, 100],
       [2, 100, 200]]

findjobscheduling(arr)


