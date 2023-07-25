import pandas as pd
import kanglib


# 创建一个DataFrame以供测试
df = pd.DataFrame({
    'column1': [1, 2, 3],
    'column2': [4, 5, 6],
    'weights': [0.5, 0.6, 0.7]
})

# 使用calculate_weighted_value函数
df = kanglib.calculate_weighted_value(df, ['column2'], 'weights', 'result')  # 'column1', 
print(df)


print('-----df[ressult]:\n')
print(df['result'])


import matplotlib.pyplot as plt

# 绘制结果
plt.plot(df['result'])
plt.title('Result over Index')
plt.xlabel('Index')
plt.ylabel('Result')
plt.show()


