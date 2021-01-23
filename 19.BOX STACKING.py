class Box:
    def __init__(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
def partition(arr,p,r):
    x=arr[r]
    i=p-1
    for j in range(p,r):
        if arr[j].l*arr[j].w <x.l*x.w:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1
def Quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)


def findmaxheight(arr):

    index=0
    n=len(arr)

    narr=[Box(0,0,0) for i in range(3*n)]
    for i in range(n):
        narr[index].h = arr[i].h
        narr[index].l = max(arr[i].l, arr[i].w)
        narr[index].w = min(arr[i].l, arr[i].w)
        index += 1

        # First rotation of the box
        narr[index].h = arr[i].w
        narr[index].l = max(arr[i].h, arr[i].l)
        narr[index].w = min(arr[i].h, arr[i].l)
        index += 1

        # Second rotation of the box
        narr[index].h = arr[i].l
        narr[index].l = max(arr[i].h, arr[i].w)
        narr[index].w = min(arr[i].h, arr[i].w)
        index += 1
    n*=3


    Quicksort(narr,0,n-1)

    dp=[0 for i in range(n)]

    for i in range(n):
        mx=0
        for j in range(i):
            if narr[j].l<narr[i].l and narr[j].w<narr[i].w:
                mx=max(mx,dp[j])
        dp[i]=mx+narr[i].h

    mx=0
    for i in range(n):
        mx=max(mx,dp[i])
    print(mx)



arr = [Box(4, 6, 7), Box(1, 2, 3),
           Box(4, 5, 6), Box(10, 12, 32)]

findmaxheight(arr)