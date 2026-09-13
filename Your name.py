for t in range(int(input())):
    n = int(input())    #number of cubes/letters
    l=input().split(' ')
    s=l[0]
    t=l[-1]

    check = True
    for i in t:
        if i not in s or s.count(i)!=t.count(i):
            print('NO')
            check = False
            break
    if check:
        print('YES')