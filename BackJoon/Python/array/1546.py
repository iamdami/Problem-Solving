subject_cnt = int(input())
ori_grade_list = list(map(int, input().split()))
new_grade_list = list()

for _ in range(subject_cnt):
    new_grade_list.append(ori_grade_list[_] / max(ori_grade_list) * 100)
print(sum(new_grade_list) / subject_cnt)
