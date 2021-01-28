import math
T = int(input())
for _ in range(T):
    H, W, N = map(int,input().split())
    if N%H == 0:
        front = (H)*100
        back = math.ceil(N/H)
    else:
        front = (N%H)*100
        back = math.ceil(N/H)
    print(front+back)