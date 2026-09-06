for t in range(int(input())):
    n = int(input())
    l = input().split(' ')

    n1 = []
    for i in l:
        n1.append(int(i))

    n1.sort()
    while n1[-1] not in [1,0]:
        for i in n1:
            i = abs(i - (min(n1)//2))
        print(n1)

    print(max(n1.count(1),n1.count(0),n1.count(2)))