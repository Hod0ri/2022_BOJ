import sys

N, K = map(int, input().split())
s = [[0,0]]
b = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    s.append(list(map(int, input().split())))
    
for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = s[i][0] 
        value = s[i][1]
        
        if j < w:
            b[i][j] = b[i - 1][j]
        else:
            b[i][j] = max(value + b[i - 1][j - w], b[i - 1][j])

print(b[N][K])