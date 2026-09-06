for t in range(int(input())):
    l = input().split(' ')
    n = int(l[0])
    k = int(l[1])
    l1 = input().split(' ')

    #calculating for each i
    for i in range(n):
        #removing i-th index
        n1 = []
        for j in range(n):
            if i != j:
                n1.append(int(l1[j]))
        #checking for each n1
        count = 0
        for j in range(n-2):
            while (n1[j+1]-n1[j]) > k:
                count += 1
                n1[j+1] = n1[j+1] -1
        if i != (n-1):
            print(count,end = " ")
        else:
            print(count)