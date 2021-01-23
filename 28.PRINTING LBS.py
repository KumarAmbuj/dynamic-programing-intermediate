class Path:
    def __init__(self,s,l,i,flag,psf):
        self.s=s
        self.l=l
        self.i=i
        self.flag=flag
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



def findLBS(arr):
    lis=[0 for i in range(len(arr))]
    lds=[0 for i in range(len(arr))]

    #for lis
    for i in range(len(arr)):
        mx=0
        for j in range(i):
            if arr[j]<arr[i]:
                mx=max(mx,lis[j])
        lis[i]=mx+1

    #
    for i in range(len(arr)-1,-1,-1):
        mx=0
        for j in range(len(arr)-1,i,-1):
            if arr[j]<arr[i]:
                mx=max(mx,lds[j])
        lds[i]=mx+1
    mx=0

    for i in range(len(arr)):
        if lis[i]+lds[i]>mx:
            mx=lis[i]+lds[i]

    queue=Queue()
    for i in range(len(arr)):
        if lis[i]+lds[i]==mx:
            Enqueue(queue,Path(i,lis[i],i,False,str(arr[i])))


    while(Size(queue)):
        rem=Dequeue(queue)

        if rem.l==1 and rem.flag==False:
            Enqueue(queue,Path(rem.s,lds[rem.s],rem.s,True,rem.psf))
        elif rem.l==1 and rem.flag==True:
            print(rem.psf)

        elif rem.flag==False:

            for j in range(rem.i):
                if rem.l-lis[j]==1 and arr[j]<arr[rem.i]:
                    Enqueue(queue,Path(rem.s,rem.l-1,j,rem.flag,str(arr[j])+' '+rem.psf))

        elif rem.flag==True:

            for j in range(len(arr)-1,rem.i,-1):
                if rem.l-lds[j]==1 and arr[j]<arr[rem.i]:
                    Enqueue(queue,Path(rem.s,rem.l-1,j,rem.flag,rem.psf+' '+str(arr[j])))

arr=[1, 11, 2, 10, 4, 5, 2, 1]
findLBS(arr)

arr=[80, 60, 30, 40, 20, 10]
findLBS(arr)

arr=[12, 11, 40, 5, 3, 1]
findLBS(arr)





