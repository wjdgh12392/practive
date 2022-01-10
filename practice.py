N = int(input())

for i in range(N):
    r,s = input().split()
    new_s = []
    r = int(r)
    s = list(s)
    for j in s:
        for k in range(0,r):
            new_s.append(j)
    print(''.join(new_s))

print('kkkk')