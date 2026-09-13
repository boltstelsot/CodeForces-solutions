for t in range(int(input())):
    l=input().split(' ')
    x=int(l[0])
    k=int(l[1])

    if x%k!=0:
        print(1)
        print(x)
    else:
        print(2)
        print(str(x+1)+" "+str(-1))