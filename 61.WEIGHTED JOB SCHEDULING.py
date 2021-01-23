class Bag:
    def __init__(self,job,s,f,p):
        self.job=job
        self.s=s
        self.f=f
        self.p=p
class Path:
    def __init__(self,sum,i,psf):
        self.sum=sum
        self.i=i
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
        narr.append(Bag(i+1,arr[i][0],arr[i][1],arr[i][2]))
    Quicksort(narr,0,len(arr)-1)


    lis=[0 for i in range(len(narr))]

    for i in range(len(lis)):
        mx=0
        for j in range(i):

            if narr[j].f<=narr[i].s:
                mx=max(mx,lis[j])
        lis[i]= mx + (narr[i].p)
    mx=0
    for i in range(len(lis)):
        mx=max(mx,lis[i])
    print(mx)

    printingpath(lis,narr,mx)

def printingpath(lis,narr,mx):
    queue=Queue()


    for i in range(len(lis)):
        if lis[i]==mx:
            l=[]
            l.append(narr[i].job)
            Enqueue(queue,Path(mx-narr[i].p,i,l))

    while(Size(queue)):
        rem=Dequeue(queue)

        if rem.sum==0:

            for i in range(len(rem.psf)):
                l=[]
                for j in range(len(narr)):
                    if narr[j].job==rem.psf[i]:
                        l.append(narr[j].s)
                        l.append(narr[j].f)
                        l.append(narr[j].p)

                print('job',rem.psf[i],':',l)
        else:

            for j in range(rem.i):

                if narr[j].f<=narr[rem.i].s and lis[j]==rem.sum:

                    rem.psf.insert(0,narr[j].job)

                    Enqueue(queue,Path(rem.sum-narr[j].p,j,rem.psf))






arr = [[3, 10, 20],
       [1, 2, 50],
       [6, 19, 100],
       [2, 100, 200]]

findjobscheduling(arr)


