import numpy as np
from Render import Render
import turtle
 
def live_or_die(arr):
    '''
    计算下一个时刻，当前单元格的存活状态
    :param arr: 3*3的二维数组，代表当前单元格和他的所有邻居
    :return:
        0：die
        1：live
    '''
    crrent_status = arr[1,1]
    neighbor_live_num= 0
    if crrent_status == 1:
        neighbor_live_num = np.count_nonzero(arr) - 1  # np.count_nonzero(arr))  统计非0元素的个数
    else:
        neighbor_live_num = np.count_nonzero(arr)
    if neighbor_live_num == 2:
        next_status = crrent_status
    elif neighbor_live_num == 3:
        next_status = 1
    else:
        next_status = 0
    return next_status
 
def origin_to_extend(source):
    '''
    将源二维数组的外围添加一圈邻居,数值填充为0,作为哨兵,以防止判断外圈单元格时出现下标越界
    :param source: 源二维数组
    :return: 扩充后的二维数组
    '''
 
    m,n = source.shape
    res = np.zeros((m+2,n+2))
    res[1:m+1,1:n+1] = source
    return res
 
def draw_x_life_game(arr,x,size):
    '''
    绘制x次迭代的生命游戏的世界
    :return:
    '''
    now = arr
    Render(now, -750, 0, size)  # 绘制当前状态
 
    for k in range(x):
        #计算下一代
        next_time = now
        ex_now = origin_to_extend(now)
        m, n = now.shape
        for i in range(m):
            for j in range(n):
                next_time[i,j] = live_or_die(ex_now[i:i+3,j:j+3])
        # print(next_time)
        Render(next_time, -750 + (size * (n + 1))*(k+1), 0, size)
        # if (-750 + (size * (n + 1))*(k+1)<750):
        #   pic1=n,pic2=k
          # Render(next_time, -750 + (size * (pic1 + 1))*(pic1+1), 0, size)
        # else:
        #   pic1=0,pic2=0
        #   Render(next_time, -750 + (size * (n + 1))*(k+1), 0, size)
        now = next_time
 
def main():
    # now = np.array([[0, 0, 0, 0, 0, 1, 0],
    #                 [0, 0, 0, 0, 1, 0, 0],
    #                 [0, 0, 0, 0, 1, 1, 1],
    #                 [0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 1, 1, 0, 0, 0],
    #                 [0, 0, 0, 1, 0, 0, 0],
    #                 [1, 1, 1, 0, 0, 0, 0],
    #                 [1, 0, 0, 0, 0, 0, 0],
    #                 ])

    # now = np.eye(11,11)

    #解构赋值
    [now]=np.random.standard_normal(size=(1,11,11))
    #1页3行3列
    now[now>0]=1
    now[now<=0]=0

    draw_x_life_game(now, 30,4)#迭代次 小正方形边长
    #保存图片
    # ts = turtle.getscreen()
    # ts.getcanvas().postscript(file="Task2.eps")
    turtle.done()
 
if __name__ == '__main__':
    main()
 
 