
from sys import stdin


def getMaximumProfit(values, n) :
        if n==0:
            return 0
        cnt=0
        prev = values[0]
        for i in values[1:]:
            if i>prev:
                cnt+=i-prev
            prev=i
        return cnt






























#taking input using fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    values = list(map(int, stdin.readline().rstrip().split(" ")))
    return values, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    values, n = takeInput()
    print(getMaximumProfit(values, n))
    t -= 1
