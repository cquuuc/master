import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 定义网格大小和细胞大小
gridSize = 40
cellSize = 10
grid = np.random.choice([0, 1], (gridSize, gridSize))

# 更新网格
def updateGrid(*args):
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
    grid[:] = newGrid

# 计算邻居细胞数量
def getNeighborCount(row, col):
    count = np.sum(grid[row-1:row+2, col-1:col+2]) - grid[row, col]
    return count

# 绘制网格
def drawGrid(*args):
    plt.clf()
    plt.imshow(grid, cmap='binary')
    plt.xticks([])
    plt.yticks([])

# 创建动画
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, updateGrid, frames=100, interval=100, blit=False, repeat=False)
ani2 = animation.FuncAnimation(fig, drawGrid, frames=100, interval=100, blit=False, repeat=False)

plt.show()
