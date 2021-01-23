def findways(n):
    space=1
    building=1

    for i in range(2,n+1):
        nbuilding=space
        nspace=space+building

        building=nbuilding
        space=nspace

    res=space+building
    ans=res*res
    print(ans)

findways(1)
findways(3)
findways(4)
