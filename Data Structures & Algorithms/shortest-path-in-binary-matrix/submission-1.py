class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,-1), (-1,1)]
        q = deque()
        q.append([1, 0, 0])
        visit = set()
        visit.add((0,0))
        while q:
            dist, r,c = q.popleft()
            if grid[r][c] == 1:
                return -1
            if r == len(grid)-1 and c== len(grid)-1:
                return dist
           
            for dr, dc in directions:
                nr = r+dr
                nc= c+dc
                if nr <0 or nr>= len(grid) or nc<0 or nc>= len(grid) or grid[nr][nc]== 1 or (nr,nc) in visit:
                    continue
                q.append([dist+1, nr,nc])
                visit.add((nr,nc))
        return -1
            

