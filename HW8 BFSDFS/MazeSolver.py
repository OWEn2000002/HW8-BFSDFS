#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs_solve_maze(self, row, col):
        if row < 0 or col < 0 or row >= len(self.maze) or col >= len(self.maze[0]) or self.maze[row][col] == 'W' or self.visited[row][col]:
            return False
        if self.maze[row][col] == 'G':
            return True

        self.visited[row][col] = True

        for dr, dc in self.directions:
            if self.dfs_solve_maze(row + dr, col + dc):
                return True

        return False
