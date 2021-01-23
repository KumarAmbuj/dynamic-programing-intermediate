def findmaxproduct(arr):
    maxendinghere=1
    maxsofar=-float('inf')

    for i in range(len(arr)):
        maxendinghere*=arr[i]
        if maxendinghere>maxsofar:
            maxsofar=maxendinghere

        if maxendinghere==0:
            maxendinghere=1

    print(maxsofar)

arr=[-2, -3, 0, -2, -40]
findmaxproduct(arr)

arr=[0, -4, 0, -2]
findmaxproduct(arr)