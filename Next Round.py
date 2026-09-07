n, k = input().split(' ')
n = int(n)
k = int(k)

l = input().split(' ')
count = 0
for i in l:
    if int(i) > 0 and int(i) >= int(l[k-1]):
        count += 1
print(count)