from collections import deque
def left2right(matrix):
    q1 = deque()
    q2 = deque()
    for i in range(len(matrix)):
        if matrix[i][0] == 1:
            q1.append((i,0))
    count = 1
    edge = len(matrix[0])-1
    while q1:
        p = q1.popleft()
        if p[1] != edge:
            # down
            if p[0] < len(matrix)-1 and matrix[p[0]+1][p[1]] == 1:
                q2.append((p[0]+1,p[1]))
            # right
            if matrix[p[0]][p[1]+1] == 1:
                q2.append((p[0], p[1]+1))
            # up
            if p[0] > 0 and matrix[p[0]-1][p[1]] == 1:
                q2.append((p[0]-1,p[1]))
        else:
            return count
        if not q1:
            count += 1
            q1,q2 = q2,q1
    return 0
if __name__ == '__main__':
    print(left2right([[0,0,1,1,1],[1,0,1,1,0],[1,1,0,1,0],[1,1,0,1,0],[0,1,1,1,0]]))

