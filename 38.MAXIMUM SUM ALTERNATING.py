def findmaxsum(arr):
    inc=[0 for i in range(len(arr))]
    dec=[0 for i in range(len(arr))]

    inc[0]=arr[0]
    dec[0]=arr[0]

    for i in range(1,len(arr)):
        mx=0
        #dec
        for j in range(i):
            if arr[j]>arr[i]:
                mx=max(mx,inc[j])
        dec[i]=mx+arr[i]

        #inc
        mx=0
        for j in range(i):
            if arr[j]<arr[i]:
                mx=max(mx,dec[j])
        inc[i]=mx+arr[i]
    mx=0
    for i in range(len(arr)):
        mx=max(mx,inc[i],dec[i])
    print(mx)

   


arr=[8,2,3,5,7,9,10]
findmaxsum(arr)

arr=[4, 3, 8, 5, 3, 8]
findmaxsum(arr)
