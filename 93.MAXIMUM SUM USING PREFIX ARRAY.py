def findmaxsum(arr):
    prefixsum=[]
    sum=0

    for i in range(len(arr)):
        sum+=arr[i]
        prefixsum.append(sum)

    res=-99
    minprefix=0

    for i in range(len(arr)):
        res=max(res,prefixsum[i]-minprefix)
        minprefix=min(minprefix,prefixsum[i])
    print(res)
arr=[-2, -3, 4, -1, -2, 1, 5, -3]
findmaxsum(arr)

arr=[4, -8, 9, -4, 1, -8, -1, 6]
findmaxsum(arr)