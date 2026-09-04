for i in range(int(input())):
    l = input().split(" ")
    l1 = []
    for i in l:
        l1.append(int(i))
    
    a = (min(l1))
    l1.remove(min(l1))
    b = (min(l1))
    
    if a+b > (max(l1)):
        print((max(l1))-a)
    else:
        print(b)
