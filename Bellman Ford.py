def bellmonFord(n, m, src, dest, edges):
        dis = [1000000000]*(n+1)
        dis[src]=0
        for i in range(n-1):
            for it in edges:
                u=it[0]
                v=it[1]
                wt = it[2]
                if dis[u]!=10**9 and dis[u]+wt < dis[v]:
                    dis[v]=dis[u]+wt
        return dis[dest]