for t in range(int(input())):
    n = int(input())
    l1 = input().split(' ')
    checker = []
    for i in range(n):
        if l1[i] not in checker:
            checker.append(l1[i])
        if len(checker) > 2:
            break
    if len(checker) == 1:
        print('YES')
    elif len(checker) > 2:
        print('NO')
    elif len(l1) & 1 == 0:
        if l1.count(checker[0]) == l1.count(checker[1]):
            print('YES')
        else:
            print('NO')
    elif len(l1) & 1 == 1:
        if abs(l1.count(checker[0]) - l1.count(checker[1])) == 1:
            print('YES')
        else:
            print('NO')