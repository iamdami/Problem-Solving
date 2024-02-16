num_list = list(map(int, input().split()))
if str(num_list[0])[::-1] > str(num_list[1])[::-1]:
    print(str(num_list[0])[::-1])
elif str(num_list[0])[::-1] < str(num_list[1])[::-1]:
    print(str(num_list[1])[::-1])
else:
    pass
