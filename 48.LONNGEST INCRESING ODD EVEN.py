class Path:
    def __init__(self,l,i,psf):

        self.l=l
        self.i = i
        self.psf=psf

def Queue():
    queue=[]
    return queue
def Enqueue(queue,s):
    queue.append(s)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)


def findmaxoddeven(arr):
    lis=[0 for i in range(len(arr))]

    for i in range(len(arr)):
        mx=0

        if arr[i]%2==0:
            for j in range(i):
                if arr[j]<arr[i] and arr[j]%2==1:
                    mx=max(mx,lis[j])
        else:
            for j in range(i):
                if arr[j]<arr[i] and arr[j]%2==0:
                    mx=max(mx,lis[j])

        lis[i]=mx+1
    mx=0
    for i in range(len(arr)):
        mx=max(mx,lis[i])
    print(mx)

    printpath(lis,arr,mx)

def printpath(lis,arr,mx):
    queue=Queue()
    for i in range(len(arr)):
        if lis[i]==mx:
            Enqueue(queue,Path(mx,i,str(arr[i])))

    while(Size(queue)):
        rem=Dequeue(queue)

        if rem.l==1:
            print(rem.psf)
        else:
            if arr[rem.i]%2==0:
                for j in range(rem.i):
                    if arr[j]%2==1 and lis[j]==rem.l-1 and arr[j]<arr[rem.i]:
                        Enqueue(queue,Path(rem.l-1,j,str(arr[j])+' '+rem.psf))


            elif arr[rem.i]%2==1:
                for j in range(rem.i):
                    if arr[j]%2==0 and lis[j]==rem.l-1 and arr[j]<arr[rem.i]:
                        Enqueue(queue,Path(rem.l-1,j,str(arr[j])+' '+rem.psf))


arr=[5, 6, 9, 4, 7, 8]
findmaxoddeven(arr)

arr=[1, 12, 2, 22, 5, 30, 31, 14, 17, 11]
findmaxoddeven(arr)

