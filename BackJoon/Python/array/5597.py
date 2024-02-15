submitted_list = list()
num_list = list()

for i in range(1,31):
    num_list.append(i)

for _ in range(28):
    n = int(input())
    submitted_list.append(n)

def intersection(lst1, lst2):
    return list(set(lst1).difference(lst2))

print(min(intersection(num_list, submitted_list)))
print(max(intersection(num_list, submitted_list)))   
