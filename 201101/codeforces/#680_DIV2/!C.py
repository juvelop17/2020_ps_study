import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')


#####################################################


# p = ax
# x = bq + r (r != 0)
# p = a(bq + r)
#   = abq + ar







def solution(p, q):
    max_num = -1

    if p % q != 0:
        return p

    


    for di in new_divisors:
        if di % q != 0:
            max_num = di
            break

    return max_num


t = int(input())
for tt in range(t):
    p, q = map(int, input().split())
    print(solution(p, q))


#####################################################

print('time',time.time_ns()-ptime)

