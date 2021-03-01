"""
def pow_fun(first, second, mod):
    ret = 1
    while second:
        if second % 2 == 1:
            ret = ret * first % mod
            first = first * first % mod
        else:
            second //= 2
    return print(ret)


a, b, c = map(int, input().split())
pow_fun(a, b, c)
"""


a, b, c = map(int, input().split())

multi_form = []
while True:
    if b == 1: break
    if b % 2 == 0: multi_form.append(False)
    else: multi_form.append(True)
    b = b // 2

    
d = a % c
result = d
for form in multi_form[::-1]:
    if form: result = result ** 2 * (d)
    else: result = result ** 2
    result = result % c

print(result)
