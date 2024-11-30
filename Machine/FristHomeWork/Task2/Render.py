import turtle
import numpy as np
'''
/**
  * @parma m: row
  * @parma n: col
  * @parma x0: xstar
  * @parma y0: ystar
  * @parma d: length of cell
  */
'''
def cell_run_out(this,x,y):
  this.up()
  this.goto(x,y)
  this.down()

def draw_cell(this,d,color):
  this.fillcolor(color) #选择颜色
  this.begin_fill()     #填充图形
  this.setheading(0)    #绘图方向向右水平方向
  for i in range(4): #绘制一个正方形细胞
    this.fd(d)
    this.left(90)
  this.end_fill()

def Render(arr,x0,y0,d):
  t=turtle.Turtle()
  t.pencolor('#3dee00')
  turtle.tracer(0) #动画默认关闭
  cell_run_out(t,x0,y0)
  m,n=arr.shape
  for i in range(m):
    for j in range(n):
      if arr[i,j]==1:
        color='black'
      else:
        color='white'
      draw_cell(t,d,color)
      t.fd(d)
    t.backward(d*n)
    if i != m-1:
      t.setheading(-90)
      t.fd(d)
  turtle.update()
  # turtle.done()

  



if __name__ =='__main__':
  #解构赋值
  [x]=np.random.standard_normal(size=(1,3,3))
  #1页3行3列

  # x = np.array([[0,1,0],
  #               [1,0,1],
  #               [0,0,1]])

  x[x>0]=1
  x[x<=0]=0
  Render(x,0,0,5)
  turtle.done()
  
