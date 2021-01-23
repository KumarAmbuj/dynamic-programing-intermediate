def findmaxrevenue(M,x,r,t):

    dp=[0 for i in range(len(x))]

    for i in range(len(x)):
        mx=0

        for j in range(i):
            if (x[i]-x[j])>t:
                mx=max(mx,dp[j])
        dp[i]=mx+r[i]

    mx=0
    for i in range(len(x)):
        mx=max(mx,dp[i])
    print(mx)

M = 20
x = [6, 7, 12, 13, 14]
revenue = [5, 6, 5,  3,  1]
t = 5
findmaxrevenue(M,x,revenue,t)

M = 15
x = [6, 9, 12, 14]
revenue = [5, 6, 3, 7]
t = 2
findmaxrevenue(M,x,revenue,t)

m = 20
x = [6, 7, 12, 13, 14]
revenue = [5, 6, 5, 3, 1]
n = len(x)
t = 5
findmaxrevenue(M,x,revenue,t)