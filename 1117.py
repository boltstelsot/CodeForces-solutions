for t in range(int(input())):
    l1 = input()
    l2 = input().split(" ")
    x = int(l1[-1])
    n = int(l1[0])

    d = int(l2[0])
    n1 = []
    for i in range(n):
        n1.append(int(l2[i]))

    for i in range(n-1):
        if (n1[i+1] - n1[i]) > d:
            d = (n1[i+1] - n1[i])

    if (x - n1[-1])*2 > d:
        d = (x - n1[-1])*2

    print(d)
