'''
设计一个扫地机器人。
这个机器人可以前进，向左转，向右转。
方法有move, turnRight, turnLeft, clean()。
设计相应的数据结构使得它能扫完整个房间。房间大小未知，机器人的初始位置未知,最后回到起点。

思路：
主要是DFS

还有关于Grid的设计，我用了pq，
检查这个pq中存储的点是不是连续的，如果不是，则说明有地方没有到

http://www.1point3acres.com/bbs/thread-289514-2-1.html
'''
from queue import PriorityQueue
class Grids(object):
    def __init__(self):
        self.pq = PriorityQueue()
    def insert(self,posi, status):
        self.pq.put((posi,status))

    def checkStatus(self):
        return True
def move(d):
    return True

def clean():
    return

def turnRight(k):
    return

def turnLeft(k):
    return

dir = [[-1,0],[0,1],[1,0],[0,-1]]
def sweep(posi, visited, d):
    if posi in visited:
        return
    clean()
    visited.insert(posi,'Clean')
    for i in range(4):

        turnRight(1 if i > 0 else 0)
        next_dir = (i+d) % 4
        next_posi = (posi[0]+dir[next_dir][0],posi[1]+dir[next_dir][1])
        if next_posi not in visited:
            if move():
                sweep(next_posi, visited, next_dir)
                # move back
                move()
                # change to previous direction
                turnRight(2)
        else:
            visited.insert((posi[0]+dir[i][0],posi[1]+dir[i][1]),'Blocked')
        # turn to opposite direction of d
        turnRight(3)
visited = Grids()
sweep((0,0),visited)
# 检查这个pq中存储的点是不是连续的，如果不是，则说明有地方没有到
visited.checkStatus()



