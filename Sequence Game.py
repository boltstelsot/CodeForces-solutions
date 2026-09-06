for t in range(int(input())):
    n = int(input())
    l = input().split(' ')
#making the integer list
    b = []
    for i in l:
        b.append(int(i))
#creating useful variable        
    ans = [int(b[0])]
#Processing using each entry
    for i in range(1,n):
        if b[i] > b[i-1]:
            ans.append(b[i])
        elif b[i] < b[i-1]:
            ans.append(b[i])
            ans.append(b[i])
        elif b[i] == b[i-1]:
            ans.append(b[i])
#displaying answer
    print(len(ans))
    for i in ans:
        print(i, end = " ")
    print()