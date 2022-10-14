from collections import defaultdict, deque, Counter
import sys
import math


class DSU:
    def __init__(self, n):
        self.parent = []
        self.size = []
        # self.rank = []
        for i in range(n + 1):
            self.parent.append(i)
            self.size.append(1)
            # self.rank.append(0)

    def union(self, u, v):
        pu = self.findPar(u)
        pv = self.findPar(v)
        if pu == pv:
            return
        # if the size of pu is lesser than the size of pv then we will add
        # the pu into pv and the size of pv will increase and vice versa.
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

    def unionByRank(self, u, v):
        pu = self.findPar(u)
        pv = self.findPar(v)
        if pu == pv:
            return
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        # if rank is equal then the rank will be increase
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1

    def findPar(self, node):
        if self.parent[node] == node:
            return node
        # path compression -> log(n)
        # path compression and size -> O(4* alpha)
        self.parent[node] = self.findPar(self.parent[node])
        return self.parent[node]


class info():
    def __init__(self, _open=0, _close=0, _full=0):
        self.open = _open
        self.close = _close
        self.full = _full


class SGTree():
    """docstring for SGTree"""

    def __init__(self, n):
        self.seg = [0 for _ in range(4 * n)]

    def build(self, ind, low, high, arr):
        if low == high:
            self.seg[ind] = arr[low]
            return
        mid = (low + high) // 2
        self.build(2 * ind + 1, low, mid, arr)
        self.build(2 * ind + 2, mid + 1, high, arr)
        self.seg[ind] = min(self.seg[2 * ind + 1], self.seg[2 * ind + 2])

    def query(self, ind, low, high, l, r):
        # no overlap
        # high low  l r   or  l r   high low
        if r < low or l > high:
            return sys.maxsize
        # complete overlap
        # low l r high
        if low <= l and r >= high:
            return self.seg[ind]

        # partial overlap
        mid = (low + high) >> 1
        left = self.query(2 * ind + 1, 0, mid, l, r)
        right = self.query(2 * ind + 2, mid + 1, high, l, r)
        return min(left, right)

    def update(self, ind, low, high, i, val):
        if low == high:
            self.seg = val
            return
        mid = (low + high) >> 1
        if i <= mid:
            self.update(2 * ind + 1, low, mid, i, val)
        else:
            self.update(2 * ind + 1, mid + 1, high, i, val)
        self.seg[ind] = min(self.seg[2 * ind + 1], self.seg[2 * ind + 2])


def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def IntList():
    lis = input().split()
    lis = list(map(int, lis))
    return lis


def StrList():
    s = input()
    lis = [val for val in s]
    # print(lis)
    return lis


def FloatList():
    lis = input().split()
    lis = list(map(float, lis))
    return lis


def searchRange(nums, target):
    res = []
    ans1 = -1
    ans2 = -1

    def bs(nums, key):
        start = 0
        end = len(nums) - 1
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == key:
                ans = mid
                end = mid - 1
            elif nums[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
        return ans

    def bs1(nums, key):
        start = 0
        end = len(nums) - 1
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == key:
                ans = mid
                start = mid + 1
            elif nums[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
        return ans

    ans1 = bs(nums, target)
    ans2 = bs1(nums, target)
    res.append(ans1)
    res.append(ans2)
    return res


def SieveOfEratosthenes(n, isPrime):
    isPrime[0] = isPrime[1] = False
    for i in range(2, n + 1):
        isPrime[i] = True

    p = 2
    while (p * p <= n):
        if (isPrime[p] == True):
            i = p * p
            while (i <= n):
                isPrime[i] = False
                i += p
        p += 1


def findPrimePair(n):
    isPrime = [0] * (n + 1)
    SieveOfEratosthenes(n, isPrime)
    for i in range(0, n):

        if (isPrime[i] and isPrime[n - i]):
            print(i, (n - i))
            return


def query(ind, low, high, l, r, seg):
    # no overlap
    # high low  l r   or  l r   high low
    if r < low or l > high:
        return info()
    # complete overlap
    # low l r high
    if low <= l and r >= high:
        return self.seg[ind]

    # partial overlap
    mid = (low + high) >> 1
    left = self.query(2 * ind + 1, 0, mid, l, r, seg)
    right = self.query(2 * ind + 2, mid + 1, high, l, r, seg)
    return merge(left, right)


def merge(left, right):
    ans = info()

    ans.full = left.full + right.full + min(left.open, right.close)
    ans.open = left.open + right.open + min(left.open, right.close)
    ans.close = left.close + right.close + min(left.open, right.close)
    return ans


def build(ind, low, high, s, seg):
    # print("HEllo")
    if low == high:
        seg[ind] = info(s[low] == "(", s[low] == ")", 0)
        return
    mid = (low + high) // 2
    build(2 * ind + 1, low, mid, s, seg)
    build(2 * ind + 2, mid + 1, high, s, seg)
    seg[ind] = merge(seg[2 * ind + 1], seg[2 * ind + 2])


def solve(i, j, lis, cnt):
    if i >= j:
        return cnt[0]
    if lis[i] == lis[j]:
        return solve(i + 1, j - 1, lis, cnt)
    temp = lis[i + 1:j]
    temp2 = lis[i:j - 1]
    return min(solve(i + 1, j, lis, cnt[0] + 1), solve(i, j - 1, temp2, cnt[0] + 1))


def gridGame():
    n, m = map(int, input().split())
    mx = ['0' for _ in range(m)]
    lis = []
    for i in range(n):
        temp = StrList()
        for i in range(m):
            mx[i] = max(mx[i], temp[i])
        lis.append(temp)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if lis[i][j] == mx[j]:
                cnt += 1
                break
    print(cnt)


def solveByPrateek():
    n = int(input())
    child = defaultdict(list)
    parent = [0 for _ in range(n + 1)]
    level = [0 for _ in range(n + 1)]
    mx = 9
    table = [[0 for _ in range(n + 1)] for i in range(mx + 1)]

    def build():
        table[0] = parent
        for p in range(1, mx + 1):
            for i in range(2, n + 1):
                table[p][i] = table[p - 1][table[p - 1][i]]

    def dfs(node, l):
        level[node] = l
        for c in child[node]:
            parent[c] = node
            dfs(c, l + 1)

    def lca(u, v):
        if level[v] < level[u]:
            u, v = v, u
        k = level[v] - level[u]
        for i in range(mx, -1, -1):
            mask = 1 << i
            if k & mask:
                v = table[i][v]
        if u == v: return u
        for i in range(mx, -1, -1):
            up = table[i][u]
            vp = table[i][v]
            if up != vp:
                u = up
                v = vp
        u = parent[u]
        return u


        # while parent[u] != parent[v]:
        #     u = parent[u]
        #     v = parent[v]
        # return parent[u]

    for i in range(1, n + 1):
        lis = IntList()
        if len(lis)<2:continue
        for j in lis[1:]:
            child[i].append(j)
    dfs(1, 1)
    build()
    q = int(input())
    queries = []
    for _ in range(q):
        u, v = map(int, input().split())
        queries.append((u, v))
    for i, j in queries:
        print(lca(i, j))


for i in range(int(input())):
    print(f"Case {i + 1}:")
    solveByPrateek()
# print(f"Case #{i}:", solveByPRateek())
