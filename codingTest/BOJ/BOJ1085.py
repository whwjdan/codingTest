x, y, w, h = map(int,input().split())

min_list = []

min_list.append(h-y)
min_list.append(w-x)
min_list.append(x-0)
min_list.append(y-0)

print(min(min_list))