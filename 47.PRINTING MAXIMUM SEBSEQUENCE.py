class Path:
    def __init__(self,i,sum,psf):
        self.i=i
        self.sum=sum
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


def maxincreasingsum(arr):
    lis=[0 for i in range(len(arr))]

    for i in range(len(arr)):
        mx=0

        for j in range(i):
            if arr[j]<arr[i]:
                mx=max(mx,lis[j])
        lis[i]=mx+arr[i]

    mx=0
    for i in range(len(arr)):
        mx=max(mx,lis[i])

    print(mx)
    printpath(lis,arr,mx)

def printpath(lis,arr,mx):

    queue=Queue()
    for i in range(len(arr)):
        if mx==lis[i]:
            Enqueue(queue,Path(i,mx-arr[i],str(arr[i])))
    while(Size(queue)):
        rem=Dequeue(queue)

        if rem.sum==0:
            print(rem.psf)
        else:
            for j in range(rem.i):
                if arr[j]<arr[rem.i] and lis[j]==rem.sum:
                    Enqueue(queue,Path(j,rem.sum-arr[j],str(arr[j])+' '+rem.psf))



arr=[1, 101, 2, 3, 100, 4, 5]
maxincreasingsum(arr)