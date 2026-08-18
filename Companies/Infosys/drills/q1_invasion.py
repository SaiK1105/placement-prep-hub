from collections import deque

import sys
input = sys.stdin.readline
def Solve(n,m,grid):
        n = len(grid)
        m = len(grid[0])
        q = deque()
        visited = [[0]*m for _ in range(n)]
        cntFresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'A':
                    q.append((i,j,0))
                    visited[i][j] = 1
                else:
                    visited[i][j] = 0
                if grid[i][j] == 'E':
                    cntFresh+=1
        tm = 0
        drow = [-1,0,1,0]
        dcol = [0,-1,0,1]
        cnt = 0
        while q:
            r,c,t = q.popleft()
            tm = max(tm,t)
            for i in range(0,4):
                nrow = r+drow[i]
                ncol = c+dcol[i]
                if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol] == 'E' and visited[nrow][ncol] == 0:
                    q.append((nrow,ncol,t+1))
                    visited[nrow][ncol] = 1
                    cnt +=1
        if cnt!=cntFresh :
            return -1
        return tm

n = int(input())
m = int(input())
grid = [input().strip() for _ in range(n)]
print(Solve(n,m,grid))