from pprint import pprint
from collections import deque
path = ""



maze=[
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
  [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
  [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def getDictionaryOfNeighbours(maze):
  dictionaryOfNeighbours = {}

  for i in range(0, len(maze)):
    for j in range(0, len(maze)):
      if maze[i][j] == 0:
        dictionaryOfNeighbours[(i,j)]= []

  for i in range(0, len(maze)):
    for j in range(0, len(maze)):
      if maze[i][j] == 0 and maze[i][j+1] == 0:
        dictionaryOfNeighbours[(i,j)].append((i,j+1))
        dictionaryOfNeighbours[(i,j+1)].append((i,j))
      if maze[i][j] == 0 and maze[i+1][j] == 0:
        dictionaryOfNeighbours[(i,j)].append((i+1,j))
        dictionaryOfNeighbours[(i+1,j)].append((i,j))

  return dictionaryOfNeighbours

def findPathInMaze(start):
  path = ""
  visited = []
  planned = deque(["", start])

  #overit jestli jsem tam uz nebyl nebo je tot muj cil?


  return path
