

while True:
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == 0:
        break
    elif a[2]**2 == a[0]**2 + a[1]**2 :
        print('right')
    else:
        print('wrong')
