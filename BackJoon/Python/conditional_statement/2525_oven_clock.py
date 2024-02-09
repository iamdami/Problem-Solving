h, m = map(int, input().split())
cook_time = int(input())
entire_time =  m + cook_time

if entire_time >= 60:
    h += entire_time // 60
    m = (entire_time) % 60
    if h == 24:
        h = 0
    if h > 24:
        h = h - 24
    if m == 60:
        h = h + 1
        m = m - 60
        if h == 24:
            h = 0
        if h > 24:
            h = h - 24
    print(f"{h} {m}")
elif entire_time < 60:
    m = entire_time
    print(f"{h} {m}")
