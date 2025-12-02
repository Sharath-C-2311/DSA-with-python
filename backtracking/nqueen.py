class Solution:
    def solveNQueens(self, n):
        grid=[["." for _ in range(n)] for i in range(n)]
        ans=[]
        def safe(grid,i,j):
            for a in range(len(grid)):
                if grid[a][j] == "Q":
                    return False
            
            x=i
            y=j

            while x>=0 and y>=0:
                if grid[x][y]=="Q":
                    return False
                x-=1
                y-=1
            
            x=i
            y=j

            while x>=0 and y<len(grid):
                if grid[x][y] == "Q":
                    return False
                x-=1
                y+=1
            return True
        def solve(grid,cur,ans):
            if cur==len(grid):
                temp=[]
                for i in grid:
                    tr=""
                    for j in i:
                        tr+=j
                    temp.append(tr)
                ans.append(temp)
                return
            
            for i in range(len(grid)):
                if safe(grid,cur,i) == True:
                    grid[cur][i]="Q"
                    solve(grid,cur+1,ans)
                    grid[cur][i]="."
        solve(grid,0,ans)

        return ans