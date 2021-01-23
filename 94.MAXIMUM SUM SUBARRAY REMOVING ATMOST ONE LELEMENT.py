def kadane(arr):
    maxendinghere=0
    maxsofar=0
    s=0
    start=0
    e=0
    for i in range(len(arr)):
        maxendinghere+=arr[i]

        if maxsofar<maxendinghere:
            maxsofar=maxendinghere
            start=s
            e=i

        if maxendinghere<0:
            maxendinghere=0
            s=i+1
    return start,e,maxsofar


def findmaxvalue(arr):

    s,e,maxsofar=kadane(arr)

    ans=0

    for i in range(s,e+1):
        ans=max(ans,maxsofar,maxsofar-arr[i])
    print(ans)
arr=[-2, -3, 4, -1, -2, 1, 5, -3]
findmaxvalue(arr)

arr=[1,2, 3, -4,  5]
findmaxvalue(arr)