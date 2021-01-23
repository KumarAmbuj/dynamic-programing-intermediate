def findcount(n):
    ones=1
    zeros=1

    for i in range(2,n+1):
        nones=zeros
        nzeros=ones+zeros

        ones=nones
        zeros=nzeros

    ans=ones+zeros
    print(ans)

findcount(2)
findcount(3)

def findways(n):
    ones=[0 for i in range(n+1)]
    zeros=[0 for i in range(n+1)]

    zeros[1]=1
    ones[1]=1

    for i in range(2,n+1):
        ones[i]=zeros[i-1]
        zeros[i]=ones[i-1]+zeros[i-1]
    ans=zeros[n]+ones[n]
    print(ans)
findways(2)
findways(3)
