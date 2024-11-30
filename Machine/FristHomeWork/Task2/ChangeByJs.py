import numpy as np
import matplotlib.pyplot as plt

# 定义网格大小和细胞大小
gridSize = 40
cellSize = 10
grid = np.random.choice([0, 1], (gridSize, gridSize))

# 更新和绘制网格
def updateGrid():
    global grid
    newGrid = np.copy(grid)
    for i in range(gridSize):
        for j in range(gridSize):
            total = getNeighborCount(i, j)
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1
    grid = newGrid

def getNeighborCount(row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            newRow = (row + i + gridSize) % gridSize
            newCol = (col + j + gridSize) % gridSize
            count += grid[newRow, newCol]
    return count

def drawGrid():
    plt.clf()
    plt.imshow(grid, cmap='binary')
    plt.xticks([])
    plt.yticks([])
    plt.pause(0.001)

# 主循环
while True:
    updateGrid()
    drawGrid()
