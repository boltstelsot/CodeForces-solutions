for t in range(int(input())):
    n = int(input())
    n1 = input().split(' ')
    n2 = []
    for i in n1:
        n2.append(i)
    for k in range(1,n-1):
        for i in range(1,n-1):
            if n1[i] > n1[i-1] and n1[i] > n1[i+1]:
                n1[i], n1[i+1] = n1[i+1], n1[i]
    n2.sort()
    if n1 == n2:
        print('YES')
    else:
        print('NO')