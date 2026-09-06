for t in range(int(input())):
    n = int(input())
    l = input().split(' ')
#making the list integer cause otherwise it doesn't work 
    k = []
    for i in l:
        k.append(int(i))
#creating useful variables
    b,c,m = [],[],max(k)
#going through each entry and appending them to b or c accordingly
    for i in k:
        if int(i) == int(m):
            c.append(m)
        else:
            b.append(int(i))
#displaying the answer
    if b == []:
        print(-1)
    else:
        print(len(b),len(c))
        for i in b:
            print(i,end = " ")
        print()
        for i in c:
            print(i,end = " ")
        print()