welcome to Kang digital magic world:
V0.3：calculate_weighted_value
thank you for your trust. if you have any questions, please contact me. kangxiaowen@gmail.com


首先，创建两个DataFrame：一个是活动水平序列，另一个是权重序列。请看以下的Python代码：

```python
import pandas as pd
import kanglib
import matplotlib.pyplot as plt

# 创建一个日期范围
dates = pd.date_range(start='2022-01-01', periods=365)

# 创建活动水平DataFrame
activity_levels_df = pd.DataFrame({
    'date': dates,
    'activity_level': [0.2] * len(dates)
})

# 创建权重DataFrame
weights_df = pd.DataFrame({
    'date': dates,
    'weight': [0.5] * len(dates)
})

# 合并这两个DataFrame
df = pd.merge(activity_levels_df, weights_df, on='date')

# 使用calculate_weighted_value函数
df = kanglib.calculate_weighted_value(df, ['activity_level'], 'weight', 'result')

# 打印DataFrame
print(df)

# 绘制结果
plt.plot(df['date'], df['result'])
plt.title('Weighted Activity Level over Time')
plt.xlabel('Date')
plt.ylabel('Weighted Activity Level')
plt.show()
```

这段代码首先创建了两个DataFrame，一个包含活动水平，另一个包含权重，都是针对相同的日期范围。然后，它们被合并到同一个DataFrame中，然后使用`calculate_weighted_value`函数计算加权活动水平。然后它打印出这个DataFrame，并将结果列绘制成一条折线图，x轴是日期，y轴是加权活动水平。

---
rm dist/*
python setup.py sdist bdist_wheel
twine upload dist/*
pip install --upgrade kanglib
pip install --no-cache-dir --upgrade kanglib



---
## 使用示例

下面是如何使用 `kanglib.calculate_weighted_value` 函数的示例：

```python
import pandas as pd
import kanglib
import matplotlib.pyplot as plt
import numpy as np

# 创建一个日期范围
dates = pd.date_range(start='2022-01-01', periods=365*2)

# 创建活动水平DataFrame
activity_levels_df = pd.DataFrame({
    'date': dates,
    'activity_level': np.random.rand(len(dates))
})

# 创建权重DataFrame
weights_df = pd.DataFrame({
    'date': dates,
    'weight': np.random.rand(len(dates))
})

# 合并这两个DataFrame
df = pd.merge(activity_levels_df, weights_df, on='date')

# 使用calculate_weighted_value函数
df = kanglib.calculate_weighted_value(df, ['activity_level'], 'weight', 'result')

# 打印DataFrame
print(df)

# 绘制结果
plt.plot(df['date'], df['result'])
plt.title('Weighted Activity Level over Time')
plt.xlabel('Date')
plt.ylabel('Weighted Activity Level')
plt.show()


```

两种办法可以查看说明和案例
方法一：

kang@Love-Grace code_pypi$ python check_kanglib.py 
import kanglib
import inspect

functions = inspect.getmembers(kanglib, inspect.isfunction)

for name, func in functions:
    print(f"Function name: {name}")
    print("Documentation:")
    print(inspect.getdoc(func))
    print("\n" + "="*50 + "\n")



方法二：
https://pypi.org/project/kanglib/0.5/

