s = input()
chk_list = [-1]*26

for i in range(len(s)):
    if chk_list[ord(s[i])-ord("a")] != -1:
        continue
    else:
        chk_list[ord(s[i])-ord("a")] = i

for _ in range(26):
    print(chk_list[_], end=" ")
