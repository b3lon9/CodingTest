# 2023-10-10-화:아침
# p.110 상하좌우

size = 5
x, y = 1, 1
direction = ['R', 'R', 'R', 'U', 'D', 'D']

print('direction:', direction)

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for d in direction:
    for i in range(len(move_types)):
        if d == move_types[i]:
            nx  = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny <1 or nx > size or ny > size:
        continue
    x, y = nx, ny

print(x, y)