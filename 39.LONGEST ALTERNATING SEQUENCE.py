def findLAS(arr):
    inc=[0 for i in range(len(arr))]
    dec=[0 for i in range(len(arr))]

    for i in range(len(arr)):
        mx=0
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
arr=[10, 22, 9, 33, 49, 50, 31, 60 ]
findLAS(arr)




