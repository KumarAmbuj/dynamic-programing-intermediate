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

def findlongestzigzag(arr):
    inc=[0 for i in range(len(arr))]
    dec=[0 for i in range(len(arr))]


    for i in range(len(arr)):
        mx=0
        #dec
        for j in range(i):
            if arr[j]>arr[i]:
                mx=max(mx,inc[j])
        dec[i]=mx+1

        mx=0
        for j in range(i):
            if arr[j]<arr[i]:
                mx=max(mx,dec[j])
        inc[i]=mx+1
    mx=0
    for i in range(len(arr)):
        mx=max(mx,inc[i],dec[i])
    print(mx)
    print(inc)
    print(dec)
    printpath(inc,dec,arr,mx)
def printpath(inc,dec,arr,mx):
    queue=Queue()
    for i in range(len(arr)):
        if inc[i]==mx or dec[i]==mx:
            Enqueue(queue,Path(mx,i,str(arr[i])))

    while(Size(queue)):
        rem=Dequeue(queue)
        if rem.l==1:
            print(rem.psf)
        else:

            for j in range(rem.i):
                if inc[j]==rem.l-1 or dec[j]==rem.l-1:
                    Enqueue(queue,Path(rem.l-1,j,str(arr[j])+' '+rem.psf))

arr=[10, 22, 9, 33, 49, 50, 31, 60]
findlongestzigzag(arr)
