'''
Facebook_Medium
11.11 8:51pm
'''
from collections import deque


class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.set_length(rooms, i, j)

    def set_length(self, room, i, j):
        q = deque()
        q.append([i, j])
        while q:
            grid = q.popleft()
            i = grid[0]
            j = grid[1]
            if i > 0 and room[i - 1][j] > room[i][j] + 1:
                room[i - 1][j] = room[i][j] + 1
                q.append([i - 1, j])
            if i < len(room) - 1 and room[i + 1][j] > room[i][j] + 1:
                room[i + 1][j] = room[i][j] + 1
                q.append([i + 1, j])
            if j > 0 and room[i][j - 1] > room[i][j] + 1:
                room[i][j - 1] = room[i][j] + 1
                q.append([i, j - 1])
            if j < len(room[0]) - 1 and room[i][j + 1] > room[i][j] + 1:
                room[i][j + 1] = room[i][j] + 1
                q.append([i, j + 1])