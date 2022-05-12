import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

tree = [[] for _ in range(n+1)]
md = 0

for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))

def dfs(n,d):
    left,right = 0,0
    for node, w in tree[n]:
        r = dfs(node,w)
        if left <= right:
            left = max(left,r)
        else:
            right = max(right,r)
            
    global md
    md = max(md,left+right)
    return max(left+d,right+d)
            
dfs(1,0)
print(md)