class Temple:
    def __init__(self,l,r):
        self.l=l
        self.r=r


def templeOffering(arr):
    n=len(arr)
    chainSize=[]
    for i in range(len(arr)):
        chainSize.append(Temple(-1,-1))

    chainSize[0].l=1
    chainSize[n-1].r=1

    for i in range(1,n):
        if arr[i-1]<arr[i]:
            chainSize[i].l=chainSize[i-1].l+1
        else:
            chainSize[i].l=1
    for i in range(n-2,-1,-1):
        if arr[i]>arr[i+1]:
            chainSize[i].r=chainSize[i+1].r+1
        else:
            chainSize[i].r=1

    sum=0

    for i in range(n):
        sum+=max(chainSize[i].l,chainSize[i].r)

    print(sum)

arr=[1,2,2]

templeOffering(arr)

arr=[1, 4, 3, 6, 2, 1 ]

templeOffering(arr)
