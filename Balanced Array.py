for t in range(int(input())):
    n = int(input())
    if n%4 == 0:
        print('YES')
        s = (n*(n+2))//4
        l = s - (n//2 - 1)**2
        
        for i in range(n//2):
            print((i+1)*2, end=" ")

        for i in range(n//2-1):
            print((i*2)+1, end=" ")
        
        print(l)       
    else:
        print('NO')