# numpy==1.19.5
# scipy==1.5.4
# matplotlib==2.2.3
# python==3.6.9
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import math
import scipy.integrate as si


##定义Rect wave函数 Rec_wav方波生成函数
# 第一个参数为方波时间对应的list，第二个参数为方波的幅度。
def Rec_wave(x, A):
    y = np.zeros(len(x))
    for i in range(1, 101, 2):
        y += 4 * A / np.pi * np.sin(2 * np.pi * i * x) / i
    return y


# 定义Frequece Amplitude函数 Fre_ampl
# 第一个参数为信号时间的list，第二个参数为信号对应时间的幅度的list
# 返回两个参数，第一个参数为frequecy的list(所得频率序列需除以总时长)，第二个参数为amplitude的list
def Fre_ampl(x, y):
    y_f = np.fft.fft(y)
    f = np.arange(len(x))
    abs_y = np.abs(y_f)
    normalization_y = abs_y / (len(x))
    half_x = f[range(int(len(x) / 2))]
    normalization_y = normalization_y[range(int(len(x) / 2))]
    return half_x, normalization_y


# 定义Show sin函数 Show_sin
def Show_sin():
    # 定义信号时间
    t = np.arange(0, 1, 0.001)
    # 定义正弦波
    y_sin = 3 * np.sin(12 * np.pi * t)
    plt.figure(num=1, figsize=(8, 6))
    plt.subplot(2, 2, 1)
    plt.axis([0, 1.05, -3.2, 3.2])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    plt.plot(t, y_sin, 'b')
    plt.xlabel('time/(s)')
    plt.ylabel('Amplitude/(V)')
    # 正常采样
    y_sin1 = y_sin.copy()
    i = 0
    N = 15
    while i < N:
        y_sin1[i::N + 1] = 0
        i = i + 1
    plt.subplot(2, 2, 2)
    plt.axis([0, 1.05, -3.2, 3.2])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    plt.vlines(t, 0, y_sin1, 'r')
    plt.xlabel('time/(s)')
    plt.ylabel('Amplitude/(V)')
    # 欠采样
    y_sin2 = y_sin.copy()
    i = 0
    N = 100
    while i < N:
        y_sin2[i::N + 1] = 0
        i = i + 1
    plt.subplot(2, 2, 3)
    plt.axis([0, 1.05, -3.2, 3.2])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    plt.vlines(t, 0, y_sin2, 'c')
    plt.xlabel('time/(s)')
    plt.ylabel('Amplitude/(V)')
    # 还原信号
    b, a = signal.iirdesign(0.08, 0.1, 1, 40)  # 设置低通滤波器
    y_sinh1 = signal.filtfilt(b, a, y_sin1)
    y_sinh2 = signal.filtfilt(b, a, y_sin2)
    plt.subplot(2, 2, 4)
    plt.axis([0, 1.05, -0.5, 0.5])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    plt.plot(t, y_sinh1, color='r', label='enough')
    plt.plot(t, y_sinh2, color='c', label='low')
    plt.legend(loc='upper right')
    plt.xlabel('time/(s)')
    plt.ylabel('Amplitude/(V)')
    """各个信号频谱"""
    plt.figure(num=2, figsize=(8, 6))
    f_sin, am_sin = Fre_ampl(t, y_sin)
    f_sin1, am_sin1 = Fre_ampl(t, y_sin1)
    f_sin2, am_sin2 = Fre_ampl(t, y_sin2)
    f_sinh1, am_sinh1 = Fre_ampl(t, y_sinh1)
    f_sinh2, am_sinh2 = Fre_ampl(t, y_sinh2)
    plt.subplot(5, 1, 1)
    plt.axis([0, 10, 0, 3])
    plt.vlines(f_sin, 0, am_sin, 'b')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')

    plt.subplot(5, 1, 2)
    plt.vlines(f_sin1, 0, am_sin1, 'r')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')

    plt.subplot(5, 1, 3)
    plt.vlines(f_sin2, 0, am_sin2, 'c')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')

    plt.subplot(5, 1, 4)
    plt.axis([0, 10, 0, 0.1])
    plt.vlines(f_sinh1, 0, am_sinh1, 'r')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')

    plt.subplot(5, 1, 5)
    # plt.axis([0,10,0,3])
    plt.vlines(f_sinh2, 0, am_sinh2, 'c')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')


# 定义Show rectwave函数 Show_rec
def Show_rec():
    # 定义信号时间
    t = np.arange(0, 1, 0.001)
    # 定义方波信号
    y_rec = Rec_wave(t, 3)
    plt.figure(num=1, figsize=(8, 6))
    plt.subplot(2, 2, 1)
    plt.axis([0, 1.05, -3.2, 3.2])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    plt.plot(t, y_rec, 'b')
    plt.xlabel('time/(s)')
    plt.ylabel('Amplitude/(V)')
    # 正常采样
    y_rec1 = y_rec.copy()
    i = 0
    N = 15
    while i < N:
        y_rec1[i::N + 1] = 0
        i = i + 1
    plt.subplot(2, 2, 2)
    plt.axis([0, 1.05, -3.2, 3.2])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    plt.vlines(t, 0, y_rec1, 'r')
    plt.xlabel('time/(s)')
    plt.ylabel('Amplitude/(V)')
    # 欠采样
    y_rec2 = y_rec.copy()
    i = 0
    N = 100
    while i < N:
        y_rec2[i::N + 1] = 0
        i = i + 1
    plt.subplot(2, 2, 3)
    plt.axis([0, 1.05, -3.2, 3.2])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    plt.vlines(t, 0, y_rec2, 'c')
    plt.xlabel('time/(s)')
    plt.ylabel('Amplitude/(V)')
    # 还原信号
    b, a = signal.iirdesign(0.08, 0.1, 1, 40)  # 设置低通滤波器
    y_rech1 = signal.filtfilt(b, a, y_rec1)
    y_rech2 = signal.filtfilt(b, a, y_rec2)
    plt.subplot(2, 2, 4)
    plt.axis([0, 1.05, -0.3, 0.3])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    plt.plot(t, y_rech1, color='r', label='enough')
    plt.plot(t, y_rech2, color='c', label='low')
    plt.legend(loc='upper right')
    plt.xlabel('time/(s)')
    plt.ylabel('Amplitude/(V)')
    plt.figure(num=2, figsize=(8, 6))
    f_rec, am_rec = Fre_ampl(t, y_rec)
    f_rec1, am_rec1 = Fre_ampl(t, y_rec1)
    f_rec2, am_rec2 = Fre_ampl(t, y_rec2)
    f_rech1, am_rech1 = Fre_ampl(t, y_rech1)
    f_rech2, am_rech2 = Fre_ampl(t, y_rech2)
    plt.subplot(5, 1, 1)
    plt.axis([0, 10, 0, 3])
    plt.vlines(f_rec, 0, am_rec, 'b')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')

    plt.subplot(5, 1, 2)
    plt.vlines(f_rec1, 0, am_rec1, 'r')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')

    plt.subplot(5, 1, 3)
    plt.vlines(f_rec2, 0, am_rec2, 'c')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')

    plt.subplot(5, 1, 4)
    plt.axis([0, 10, 0, 0.1])
    plt.vlines(f_rech1, 0, am_rech1, 'r')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')

    plt.subplot(5, 1, 5)
    # plt.axis([0,10,0,3])
    plt.vlines(f_rech2, 0, am_rech2, 'c')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')


# 定义Show Trgwave函数 Show_trg
def Show_trg():
    # 定义信号时间
    t = np.arange(0, 1, 0.001)
    # 定义三角波信号
    n = 1000
    y_trg = np.zeros(n)
    for i in range(1, n + 1):
        y_trg += 12 / ((2 * i - 1) * np.pi * (2 * i - 1) * np.pi) * np.sin((2 * i - 1) * np.pi / 2) * np.sin(
            (2 * i - 1) * np.pi * 100 * t)
    plt.figure(num=1, figsize=(8, 6))
    plt.subplot(2, 2, 1)
    plt.axis([0, 1.05, -3.2, 3.2])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    plt.plot(t, y_trg, 'b')
    plt.xlabel('time/(s)')
    plt.ylabel('Amplitude/(V)')
    # 正常采样
    y_trg1 = y_trg.copy()
    i = 0
    N = 15
    while i < N:
        y_trg1[i::N + 1] = 0
        i = i + 1
    plt.subplot(2, 2, 2)
    plt.axis([0, 1.05, -3.2, 3.2])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    plt.vlines(t, 0, y_trg1, 'r')
    plt.xlabel('time/(s)')
    plt.ylabel('Amplitude/(V)')
    # 欠采样
    y_trg2 = y_trg.copy()
    i = 0
    N = 100
    while i < N:
        y_trg2[i::N + 1] = 0
        i = i + 1
    plt.subplot(2, 2, 3)
    plt.axis([0, 1.05, -3.2, 3.2])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    plt.vlines(t, 0, y_trg2, 'c')
    plt.xlabel('time/(s)')
    plt.ylabel('Amplitude/(V)')
    # 还原信号
    b, a = signal.iirdesign(0.08, 0.1, 1, 40)  # 设置低通滤波器
    y_trgh1 = signal.filtfilt(b, a, y_trg1)
    y_trgh2 = signal.filtfilt(b, a, y_trg2)
    plt.subplot(2, 2, 4)
    plt.axis([0, 1.05, -0.2, 0.2])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    plt.plot(t, y_trgh1, color='r', label='enough')
    plt.plot(t, y_trgh2, color='c', label='low')
    plt.legend(loc='upper right')
    plt.xlabel('time/(s)')
    plt.ylabel('Amplitude/(V)')
    """各个信号频谱"""
    plt.figure(num=2, figsize=(8, 6))
    f_trg, am_trg = Fre_ampl(t, y_trg)
    f_trg1, am_trg1 = Fre_ampl(t, y_trg1)
    f_trg2, am_trg2 = Fre_ampl(t, y_trg2)
    f_trgh1, am_trgh1 = Fre_ampl(t, y_trgh1)
    f_trgh2, am_trgh2 = Fre_ampl(t, y_trgh2)
    plt.subplot(5, 1, 1)
    plt.axis([0, 500, 0, 0.7])
    plt.vlines(f_trg, 0, am_trg, 'b')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')

    plt.subplot(5, 1, 2)
    plt.vlines(f_trg1, 0, am_trg1, 'r')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')

    plt.subplot(5, 1, 3)
    plt.vlines(f_trg2, 0, am_trg2, 'c')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')

    plt.subplot(5, 1, 4)
    plt.axis([0, 100, 0, 0.025])
    plt.vlines(f_trgh1, 0, am_trgh1, 'r')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')

    plt.subplot(5, 1, 5)
    # plt.axis([0,10,0,3])
    plt.vlines(f_trgh2, 0, am_trgh2, 'c')
    plt.xlabel('frequence/(Hz)')
    plt.ylabel('amplitude/(V)')


Show_sin()
# Show_rec()
plt.tight_layout()
# Show_trg()
plt.show()
