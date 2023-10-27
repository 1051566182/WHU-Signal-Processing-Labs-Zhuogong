# numpy==1.19.5
# matplotlib==2.2.3
# scipy==1.5.4
# sounddevice==0.4.4
# python==3.6.9
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import sounddevice as sd

plt.rcParams['font.sans-serif'] = [u'simHei']   # 显示中文
plt.rcParams['axes.unicode_minus'] = False      # 解决负号问题

# 读取 Windows 系统目录下的 ding.wav 文件
filename = 'violin.wav'

# 读取音频文件
Fs, audio_data = wavfile.read(filename)

# 选择一个声道（这里选择左声道）
channel = 0
audio_signal = audio_data[:]

# 计算音频信号的FFT
N = len(audio_signal)
audio_fft = np.abs(np.fft.fft(audio_signal) / N)
t = np.arange(0, N) * (1 / Fs)

# 绘制音频信号的频谱
plt.figure('音频信号频谱', figsize=(10, 6))
plt.plot(t, audio_fft)
plt.title('音频信号频谱', fontsize=16)
plt.xlabel('频率 (Hz)', fontsize=12)
plt.ylabel('幅度', fontsize=12)
plt.grid(True)

# 求取2048点FFT
N1 = 2048
audio_fft_2048 = np.abs(np.fft.fft(audio_signal, n=N1) / N1)
t1 = np.arange(0, N1) * (1 / Fs)

# 求取1024点FFT
N2 = 1024
audio_fft_1024 = np.abs(np.fft.fft(audio_signal, n=N2) / N2)
t2 = np.arange(0, N2) * (1 / Fs)

# 绘制不同点FFT的频谱
plt.figure('不同点FFT的频谱', figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(t1, audio_fft_2048)
plt.title('2048点FFT', fontsize=16)
plt.xlabel('频率 (Hz)', fontsize=12)
plt.ylabel('幅度', fontsize=12)
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(t2, audio_fft_1024)
plt.title('1024点FFT', fontsize=16)
plt.xlabel('频率 (Hz)', fontsize=12)
plt.ylabel('幅度', fontsize=12)
plt.grid(True)

# 执行傅里叶逆变换并绘制
audio_ifft = np.fft.ifft(audio_fft, n=N)
audio_ifft = audio_ifft.real

plt.figure('音频信号反傅里叶变换', figsize=(10, 6))
plt.plot(t, audio_ifft)
plt.title('音频信号反傅里叶变换', fontsize=16)
plt.xlabel('时间 (s)', fontsize=12)
plt.ylabel('幅度', fontsize=12)
plt.grid(True)

# 找到幅度最大的正弦分量
max_amplitude_index = np.argmax(audio_fft)
max_amplitude = audio_fft[max_amplitude_index]

# 构造同幅度的正弦信号
max_amplitude_freq = max_amplitude_index * Fs / N
t_max_amplitude = np.arange(0, N) * (1 / Fs)
sinusoidal_signal = max_amplitude * np.sin(2 * np.pi * max_amplitude_freq * t_max_amplitude)

# 比较原始信号与构造的正弦信号
plt.figure('原始信号与正弦信号比较', figsize=(10, 6))
plt.plot(t, audio_signal, label='原始信号')
# plt.plot(t_max_amplitude, sinusoidal_signal, label='同幅度正弦信号')
plt.title('原始信号与正弦信号比较', fontsize=16)
plt.xlabel('时间 (s)', fontsize=12)
plt.ylabel('幅度', fontsize=12)
plt.legend()
plt.grid(True)


plt.figure('原始信号与正弦信号比较2', figsize=(10, 6))
plt.axis([0, 0.01, -200, 200])
plt.plot(t_max_amplitude, sinusoidal_signal, label='同幅度正弦信号')
plt.title('原始信号与正弦信号比较', fontsize=16)



plt.show()
# print(sinusoidal_signal)
# 播放最大正弦分量的信号
sd.play(sinusoidal_signal, Fs)
sd.wait()
