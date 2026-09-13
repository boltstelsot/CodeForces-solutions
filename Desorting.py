for t in range(int(input())):
    n=int(input())
    l=input().split(' ')
    a=[]                    #making a
    for i in l:
        a.append(int(i))
    count=max(a)
    for i in range(1,n):    #iterating the difference
        if a[i]<a[i-1]:
            count=0
            break
        else:
            m=(abs(a[i]-a[i-1])//2)+1
            count=min(count,m)
    print(count)