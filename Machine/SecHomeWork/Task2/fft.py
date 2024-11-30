import numpy as np
import matplotlib.pyplot as plt

# 定义合成方波函数
def square_wave(t, n):
    square_wave = 0
    for i in range(1, n+1):
        square_wave += (1/(2*i-1)) * np.sin((2*(2*i-1)*np.pi*t))
    return (4/np.pi) * square_wave

# 生成时间序列
t = np.linspace(0, 1, 1000, endpoint=False)  # 从0到1生成1000个点

# 合成方波信号，这里n取10
n = 10
square_wave_values = square_wave(t, n)

# 绘制合成方波图
plt.figure()
plt.plot(t, square_wave_values)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Synthesized Square Wave with n=10')
plt.show()
