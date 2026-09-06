for t in range(int(input())):
    l = input().split(' ')
    n = int(l[0])
    k = int(l[1])

    s = input()
    count = 0
    for i in range(0,n,k):
        if "0" not in s[i:i+k]:
            count += 1
    print(count)