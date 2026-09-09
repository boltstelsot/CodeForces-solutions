for t in range(int(input())):
    n=int(input())
    l=input().split(' ')
    if l.count('0') < 2:
        print(-1)
    else:
        if l[0] == '1' and l[-1] == '1':
            print(2)
        elif l[0] == '1' or l[-1] == '1':
            print(1)
        else:
            print(0)