import numpy as np
import matplotlib.pyplot as plt

# 定义待测系统F，这里我们假设它是一个简单的线性函数
def system_F(s):
    return 2 * s + 1

# 定义输入样本s的分布，这里我们假设它是一个正态分布
input_samples = np.random.normal(loc=0, scale=1, size=1000)

# 计算系统F对输入样本的响应
output_samples = system_F(input_samples)

# 绘制输出样本的分布
plt.hist(output_samples, bins=50, density=True)
plt.xlabel('Output')
plt.ylabel('Density')
plt.title('Output distribution')
plt.show()
