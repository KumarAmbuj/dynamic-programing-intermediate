class Path:
    def __init__(self,l,i,psf):
        self.l=l
        self.i=i
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


def findmaxlength(arr):
    lis=[0 for i in range(len(arr))]

    for i in range(len(arr)):
        mx=0

        for j in range(i):

            if arr[j]<arr[i] and arr[i]-arr[j]==1:
                mx=max(mx,lis[j])
        lis[i]=mx+1

    mx=0
    for i in range(len(arr)):
        mx=max(mx,lis[i])

    print(mx)
    printingpath(lis,mx,arr)

def printingpath(lis,mx,arr):
    queue=Queue()

    for i in range(len(arr)):
        if lis[i]==mx:
            Enqueue(queue,Path(mx,i,str(arr[i])))
    while(Size(queue)):
        rem=Dequeue(queue)

        if rem.l==1:
            print(rem.psf)

        else:

            for j in range(rem.i):
                if rem.l-lis[j]==1 and arr[rem.i]-arr[j]==1:
                    Enqueue(queue,Path(rem.l-1,j,str(arr[j])+' '+rem.psf))

arr=[3, 10, 3, 11, 4, 5, 6, 7, 8, 12]
findmaxlength(arr)

arr=[6, 7, 8, 3, 4, 5, 9, 10]
findmaxlength(arr)

