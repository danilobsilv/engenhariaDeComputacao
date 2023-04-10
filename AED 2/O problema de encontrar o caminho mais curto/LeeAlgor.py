import sys
from collections import deque
 
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]
 
def isValid(mat, visited, row, col):
    return (row >= 0) and (row < len(mat)) and (col >= 0) and (col < len(mat[0])) \
           and mat[row][col] == 1 and not visited[row][col]
 
 
def findShortestPathLength(mat, src, dest):
 
    i, j = src
 
    x, y = dest
 
    if not mat or len(mat) == 0 or mat[i][j] == 0 or mat[x][y] == 0:
        return -1
 
    (M, N) = (len(mat), len(mat[0]))
 
    visited = [[False for x in range(N)] for y in range(M)]
 
    q = deque()
 
    visited[i][j] = True
 
    q.append((i, j, 0))

    min_dist = sys.maxsize
 
    while q:
 
        (i, j, dist) = q.popleft()
 
        if i == x and j == y:
            min_dist = dist
            break

        for k in range(4):
            if isValid(mat, visited, i + row[k], j + col[k]):
                visited[i + row[k]][j + col[k]] = True
                q.append((i + row[k], j + col[k], dist + 1))
 
    if min_dist != sys.maxsize:
        return min_dist
    else:
        return -1
 
 
if __name__ == '__main__':
 
    mat = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]
 
    src = (0, 0)
    dest = (7, 5)
 
    min_dist = findShortestPathLength(mat, src, dest)
 
    if min_dist != -1:
        print("O menor caminho da fonte até o destino tem tamanho", min_dist)
    else:
        print("O destino não pode ser alcançado a partir da fonte.")
