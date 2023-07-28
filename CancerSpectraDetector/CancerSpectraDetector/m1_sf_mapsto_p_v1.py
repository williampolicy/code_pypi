import numpy as np
import matplotlib.pyplot as plt

# 定义待测系统F，这里我们假设它是一个简单的线性函数
def system_F(s):
    return 2 * s + 1

# 定义输入样本s的分布，这里我们假设它是一个正态分布
input_samples = np.random.normal(loc=0, scale=1, size=1000)

# 计算系统F对输入样本的响应
output_samples = system_F(input_samples)

# 创建一个新的figure
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# 绘制输入样本的分布
axs[0].hist(input_samples, bins=50, density=True)
axs[0].set_title('Input distribution')
axs[0].set_xlabel('Input')
axs[0].set_ylabel('Density')

# 绘制输出样本的分布
axs[1].hist(output_samples, bins=50, density=True)
axs[1].set_title('Output distribution')
axs[1].set_xlabel('Output')
axs[1].set_ylabel('Density')

# 显示图像
plt.tight_layout()
plt.show()
