N = int(input())
l = input().split(' ')
n = []
for i in l:
    n.append(abs(int(i)))
print(min(n))