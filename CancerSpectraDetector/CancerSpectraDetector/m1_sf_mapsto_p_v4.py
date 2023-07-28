import numpy as np
import matplotlib.pyplot as plt

# 定义高斯函数
def gaussian(x, mu, sigma):
    return np.exp(-((x - mu)**2) / (2 * sigma**2))

# 定义待测系统F，它是10个高斯函数的合成
def system_F(s):
    peaks = [gaussian(s, mu, 0.5) for mu in np.linspace(-5, 5, 10)]
    return sum(peaks)

# 定义输入样本s的分布，这里我们假设它是一个正态分布
input_samples = np.random.normal(loc=0, scale=2.5, size=1000)

# 计算系统F对输入样本的响应
output_samples = system_F(input_samples)

# 创建一个新的figure
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# 绘制输入样本的分布
axs[0].hist(input_samples, bins=50, density=True)
axs[0].set_title('Input distribution')
axs[0].set_xlabel('Input')
axs[0].set_ylabel('Density')

# 绘制系统F的特征谱
x = np.linspace(-6, 6, 1000)
y = system_F(x)
axs[1].plot(x, y)
axs[1].set_title('Spectral characteristics of system F')
axs[1].set_xlabel('Input')
axs[1].set_ylabel('Output')

# 绘制输出样本的分布
axs[2].hist(output_samples, bins=50, density=True)
axs[2].set_title('Output distribution')
axs[2].set_xlabel('Output')
axs[2].set_ylabel('Density')

# 显示图像
plt.tight_layout()
plt.show()
