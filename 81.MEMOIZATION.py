def findallcount(n,bcount,ccount):
    if bcount<0 or ccount<0:
        return 0
    if n==0:
        return 1
    if bcount==0 and ccount==0:
        return 1

    res=findallcount(n-1,bcount,ccount)
    res+=findallcount(n-1,bcount-1,ccount)
    res+=findallcount(n-1,bcount,ccount-1)

    return res


def findcount(n):
    ans=findallcount(n,1,2)
    print(ans)

findcount(3)
findcount(4)
findcount(5)