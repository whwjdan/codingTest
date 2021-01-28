
words = "asdgbb".upper()
setWords = sorted(list(set(words)))

cnt_list = []

print(setWords)
print(words.count('A'))

for i in setWords:
    print(words.count(i))
    cnt_list.append(words.count(i))

print(cnt_list)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))
    print(setWords[max_index])