n, m = map(int, input().split())
bkt = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    bkt[i-1], bkt[j-1] = bkt[j-1], bkt[i-1]
for _ in range(n):
    print(bkt[_], end=" ")
