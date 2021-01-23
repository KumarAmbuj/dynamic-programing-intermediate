def findkmaxsum(arr,k):
    for c in range(k):

        maxendinghere=0
        maxsofar=-float('inf')
        start=0
        end=0
        s=0

        for i in range(len(arr)):
            maxendinghere+=arr[i]
            if maxendinghere>maxsofar:
                maxsofar=maxendinghere
                start=s
                end=i

            if maxendinghere<0:
                maxendinghere=0
                s=i+1


        print('Maximum non-overlapping subarray sum{}: {}, starting index: {}, ending index: {}.'.format(c+1,maxsofar,start,end))

        for l in range(start,end+1):
            arr[l]=-float('inf')



arr1 = [4, 1, 1, -1, -3, -5, 6, 2, -6, -2]
k1 = 3
n1 = len(arr1)
findkmaxsum(arr1,k1)