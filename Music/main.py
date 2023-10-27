# librosa==0.9.2
# matplotlib==2.2.3
# numpy==1.19.5
# scipy==1.5.4
# python==3.6.9
import librosa
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

plt.rcParams['font.sans-serif'] = [u'simHei']   # 显示中文
plt.rcParams['axes.unicode_minus'] = False      # 解决负号问题

# 读取音频文件
# audio_file = './data/视唱-8k.wav'
audio_file = './data/Hum.wav'
y, sr = librosa.load(audio_file)

# 预加重滤波 高通滤波，增强信号中的高频成分，平滑音频信号的频谱特性
pre_emphasis_coefficient = 0.97  # 预加重系数，可以根据需要调整
y_pre_emphasis = signal.lfilter([1, -pre_emphasis_coefficient], [1], y) # 用于预加重的滤波器

# 提取基频（音高）信息
f0, voiced_flag, voiced_probs = librosa.pyin(y_pre_emphasis, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C6'))

valid_values = f0[~np.isnan(f0)] # 去除无效值
max_freq = np.max(valid_values)
min_freq = np.min(valid_values)

# 标准音高刻度
standard_notes = ['C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2',
                  'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3',
                  'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4',
                  'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5',
                  'C6']

note_frequencies = [librosa.note_to_hz(note) for note in standard_notes] # 标准音高对应的频率
f0_standard = [min(note_frequencies, key=lambda x: abs(x - freq)) for freq in f0] # 将f0每个点的频率转换为标准音高，存储在f0_standard中

times = librosa.times_like(f0)

# 绘制原始波形图
plt.figure(figsize=(10, 4))
plt.plot(y, label='原始波形')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('原始音频波形')
plt.legend()
plt.grid()
plt.show()

# 绘制原始音高图
plt.figure(figsize=(10, 4))
plt.plot(times, f0, label='原始音高 (Hz)')
plt.yticks(librosa.note_to_hz(standard_notes), standard_notes) # 设置y轴刻度
plt.ylim(min_freq, max_freq)  # 限制y轴显示的音高范围
plt.xlabel('Time (s)')
plt.ylabel('Pitch (Note Name)')
plt.title('原始音高图 ')
plt.legend()
plt.grid()
plt.show()

# 绘制中值滤波后的音高图像
plt.figure(figsize=(10, 4))
times = times[2:]
plt.plot(times, f0_standard[2:], label='中值滤波后音高 (Hz)')
plt.yticks(librosa.note_to_hz(standard_notes), standard_notes) # 设置y轴刻度
plt.ylim(min_freq, max_freq)  # 限制y轴显示的音高范围
plt.xlabel('Time (s)')
plt.ylabel('Pitch (Note Name)')
plt.title('中值滤波后的音高图')
plt.legend()
plt.grid()
plt.show()
