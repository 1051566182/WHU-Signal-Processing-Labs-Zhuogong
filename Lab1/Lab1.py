# numpy==1.19.5
# matplotlib==2.2.3
# python==3.6.9
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = [u'simHei']   # 显示中文
plt.rcParams['axes.unicode_minus'] = False      # 解决负号问题

# (1)合成方波
# 定义一个奇次谐波函数
def oddHarmonic(n):
    t = np.arange(0, 0.1, 0.0001) # 定义时间变量,10000hz
    y = (12 / np.pi) * np.sin( 2 * np.pi * 50 * n * t ) / n # 定义奇次谐波函数
    return y

# 定义一个时间变量
t = np.arange(0, 0.1, 0.0001) # 定义时间变量,10000hz
plt.figure(num="方波合成")
# (b)基波分量
y1 = oddHarmonic(1)
# 画出基波分量
plt.subplot(2, 2, 1)
plt.plot(t,y1)
plt.title(u'基波分量')
plt.grid(True)
# plt.show()

# (c)基波分量+3次谐波分量
y2 = oddHarmonic(1) + oddHarmonic(3)
# 画出基波分量+3次谐波分量
plt.subplot(2, 2, 2)
plt.plot(t,y2)
plt.title(u'基波分量+3次谐波分量')
plt.grid(True)
# plt.show()

# (d)基波分量+3次谐波分量+5次谐波分量+7次谐波分量+9次谐波分量
y3 = oddHarmonic(1) + oddHarmonic(3) + oddHarmonic(5) + oddHarmonic(7) + oddHarmonic(9)
# 画出基波分量+3次谐波分量+5次谐波分量+7次谐波分量+9次谐波分量
plt.subplot(2, 2, 3)
plt.plot(t,y3)
plt.title(u'基波分量+3-9次谐波分量')
plt.grid(True)
# plt.show()

# (e)19次，用循环的方式来写
y4 = oddHarmonic(1)
for i in range(3, 20, 2):
    y4 += oddHarmonic(i)
# 画出19次谐波分量
plt.subplot(2, 2, 4)
plt.plot(t,y4)
plt.title(u'基波+3-19次谐波分量')
plt.grid(True)
# 自动调整子图之间的间距
plt.tight_layout()
plt.show()


# (2)设计谐波合成三角波的实验

# 创建一个名为“三角波合成”的图形窗口
plt.figure(num="三角波合成")

# 幅值为2，频率为0.5Hz
E = 2
f0 = 0.5

# t变化为100Hz
t = np.arange(0, 10, 0.01)
ytrig = E / 2
# n取1-19的奇数，当n取偶数的时候，该a_n为0，所以只剩下cos这一项
for n in range(1, 20, 2):
    ytrig += (4 * E / np.pi ** 2) * (np.cos(n * 2 * np.pi * f0 * t)) / n ** 2
# 画出三角波
plt.plot(t, ytrig)
plt.grid(True)
plt.show()


# 设计分析方波、三角波频谱的分析实验
# 创建一个名为“频谱分析”的图形窗口
plt.figure(num="频谱分析")
Fs = 100               # 采样率1000HZ
N = 1000

# 方波傅里叶变换
yfft = 3 * np.abs(np.fft.fft(y4) / N)
yfft = yfft[:N // 2 + 1]
yfft[1:-1] = 2 * yfft[1:-1]
F = Fs * np.arange(N // 2 + 1) / N
plt.subplot(1, 2, 1)
plt.plot(F, yfft)
plt.title(u'方波傅里叶变换')
plt.xlabel('freq/Hz')
plt.ylabel('Amplitude/V')
plt.grid(True)

# 三角波傅里叶变换
yfft = 3 * np.abs(np.fft.fft(ytrig) / N)
yfft = yfft[:N // 2 + 1]
yfft[1:-1] = 2 * yfft[1:-1]
F = Fs * np.arange(N // 2 + 1) / N
plt.subplot(1, 2, 2)
plt.plot(F, yfft)
plt.title('三角波傅里叶变换')
plt.xlabel('freq/Hz')
plt.ylabel('Amplitude/V')
plt.grid(True)

plt.tight_layout()

plt.show()






