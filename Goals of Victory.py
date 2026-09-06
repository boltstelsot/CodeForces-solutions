for t in range(int(input())):
    n = int(input())
    l = input().split(' ')
    s = 0
    for i in l:
        s += int(i)
    print(s*(-1))