basket_cnt, trial = map(int, input().split())
basket = [0 for _ in range(basket_cnt)]
for _ in range(trial):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        basket[n - 1] = k
for n in range(basket_cnt):
    print(basket[n], end=" ")
