for t in range(int(input())):
    n=int(input())
    l=input().split(' ')

    n1=[]
    for i in l:
        n1.append(int(i))
    n1.sort()

    count_1=0
    count_0=0
    count_2=0
    parity=(n1[-1]&1)

    for i in n1:
        if i%2==1:
            count_1+=1
        else:
            if parity==0:
                if i%4==0:
                    count_2+=1
                elif i%4==2:
                    count_0+=1
            elif parity==1:
                if i%4==0:
                    count_0+=1
                elif i%4==2:
                    count_2+=1
    print(max(count_0,count_1,count_2))