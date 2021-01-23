def findNumber(n):
    #jacob Number
    dpj=[0 for i in range(n+1)]
    #licas Number
    dpl=[0 for i in range(n+1)]

    dpj[0]=0
    dpj[1]=1

    dpl[0]=2
    dpl[1]=1

    for i in range(2,n+1):
        dpj[i]=dpj[i-1]+2*(dpj[i-2])
        dpl[i]=dpl[i-1]+2*(dpl[i-2])

    print('Jacob Number',dpj[n])
    print('Jacob-Lucas Number ',dpl[n])

findNumber(5)




