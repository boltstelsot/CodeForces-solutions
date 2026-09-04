"""for t in range(int(input())):
    l = input().split(' ')
    x = input()
    s = input()
    count = 0
    if s in x:
        print(count)
        continue
    while s not in x:
        x = x*2
        count += 1
        if s in x:
            print(count)
            break
        elif len(x) > (len(s))*2:
            print(-1)
            break
"""                 #The above code took 125ms at 100kb (Code by Me)
                    #The below code took 140ms at 300kb (code by CP-31)
for t in range(int(input())):
    l = input().split(' ')
    x = input()
    s = input()

    if s in x:
        print(0)
        continue
    for i in range(1,6):
        x = x*2
        if s in x:
            print(i)
            break
    if s not in x:
        print(-1)