x = int(input())
n = int(input())
res = 0

for i in range(1, n+1):
    a, b = map(int, input().split())
    res += a * b
if res == x:
    print("Yes")
else:
    print("No")
