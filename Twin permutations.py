for t in range(int(input())):
    n = int(input())
    l = input().split(' ')
    for i in l:
        print(n+1-int(i),end = " ")
    print()