def findLBS(arr):
    lis=[0 for i in range(len(arr))]
    lds=[0 for i in range(len(arr))]

    for i in range(len(arr)):
        mx=0

        for j in range(i):
            if arr[j]<arr[i]:
                mx=max(mx,lis[j])
        lis[i]=mx+1

    for i in range(len(arr)-1,-1,-1):
        mx=0
        for j in range(len(arr)-1,i,-1):
            if arr[j]<arr[i]:
                mx=max(mx,lds[j])
        lds[i]=mx+1

    mx=0

    for i in range(len(arr)):
        mx=max(mx,lis[i]+lds[i]-1)
    print(mx)
arr = [1, 11, 2, 10, 4, 5, 2, 1]
findLBS(arr)
