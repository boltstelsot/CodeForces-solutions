for t in range(int(input())):
    n = int(input())
    l = input().split(' ')
#                               First logic(46ms)
    n1 = []
    for i in l:
        n1.append(int(i))
    if sum(n1)&1 == 0:
            print('YES')
    else:
         print('NO')

"""                             Second logic(62ms)
    n1.sort()
    parity_check = False
    for i in range(n):
        a = sum(n1[:i])
        b = sum(n1[i:])
        if a&1 == b&1:
            parity_check = True
            break
            
    if parity_check:
        print('YES')
    else:
        print('NO')
"""