import math
for t in range(int(input())):
    l = input().split(' ')
    a, b, c = int(l[0]), int(l[1]), int(l[2])
    A = math.floor(c/2+0.5) + a
    K = math.floor(c/2) + b
    if A > K:
        print('First')
    else:
        print('Second')