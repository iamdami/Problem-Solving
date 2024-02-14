num_list = list()
num = 0
for i in range(9):
    num = int(input())
    num_list.append(num)
max_num = max(num_list)
max_idx = num_list.index(max_num)
print(max_num)
print(max_idx + 1)
