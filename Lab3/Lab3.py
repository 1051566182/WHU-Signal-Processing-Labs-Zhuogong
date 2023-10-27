# matplotlib==2.2.3
# scipy==1.5.4
# numpy==1.19.5
# python==3.6.9
import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np
import math

# 输入电阻、电感和电容的数值
R = float(input("请输入电阻/(欧姆Ω): "))
L = float(input("请输入电感/(亨利H): "))
C = float(input("请输入电容/(法拉F): "))

# 阻尼系数
a = R / (2 * L)
# 谐振角频率
w0 = 1 / math.sqrt(L * C)
# 定义时间和电源电压
t = np.arange(0, 100, 0.01)
ut = np.array([1 for i in t])

# 根据不同状态计算电流和电压
if a > w0 and a > 0:
    print("过阻尼")
    B = math.sqrt(a * a - w0 * w0)
    i_lt = ((1 / L) * np.exp(-a * t) * np.sinh(B * t)) / (B * ut)
    v_ct = (np.exp(-a * t) * (np.exp(-a * t) / (a + B) - np.exp(-a * t) / (a - B))) / (2 * B * L * C) + 1
elif a == w0 and a > 0:
    print("临界阻尼")
    i_lt = (1 / L) * t * np.exp(-a * t)
    v_ct = (1 / (L * C * a * a)) * (1 - (a * t + 1) * np.exp(-a * t))
elif a < w0 and a > 0:
    print("欠阻尼")
    w1 = math.sqrt(w0 * w0 - a * a)
    i_lt = w1 * L * np.exp(-a * t) * np.sin(w1 * t)
    v_ct = 1 - np.exp(-a * t) * (np.cos(w1 * t) + np.sin(w1 * t))
elif a == 0:
    print("无阻尼")
    i_lt = L * w0 * np.sin(w0 * t)
    v_ct = 1 - np.cos(w0 * t)

# 绘制图形，调整子图的高度高一些

plt.subplot(4, 1, 1)
plt.grid(True)
plt.plot(t, i_lt, color='r')
plt.xlabel("time/s")
plt.ylabel("Il(t)/A")


plt.subplot(4, 1, 2)
plt.grid(True)
plt.plot(t, v_ct, color='g')
plt.xlabel("time/s")
plt.ylabel("Vc(t)/V")


plt.subplot(4, 1, 3)
plt.plot(v_ct, i_lt, color='b')
plt.xlabel("Vc(t)/V")
plt.ylabel("Il(t)/A")
plt.grid(True)

plt.tight_layout()
plt.show()