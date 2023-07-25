# code_pypi
code_pypi for pypi , use pip in future for my digital tools world 



  当然可以。这是一个最基本的示例来展示如何创建一个Python包，并将其上传到PyPI。假设你想创建一个叫做`example_package`的包，该包有一个函数`hello`，可以打印出“Hello, World!”。

1. 首先，我们需要创建以下的文件结构：
    ```
    example_package/
    ├── example_package
    │   ├── __init__.py
    ├── setup.py
    ```

    - `example_package/`：这是项目的根目录，它的名字并不重要，不会影响你的包的名字。
    - `example_package/example_package/`：这是包的主目录，它的名字就是你包的名字，Python代码应该放在这个目录下。
    - `example_package/example_package/__init__.py`：这是包的初始化文件，在这个文件中，我们会定义我们的`hello`函数。
    - `example_package/setup.py`：这是包的安装脚本，我们在这个脚本中定义我们的包的元数据，例如它的名字，版本，作者等。

2. 在`__init__.py`中，我们定义我们的`hello`函数：
    ```python
    def hello():
        print("Hello, World!")
    ```

3. 在`setup.py`中，我们定义我们的包的元数据：
    ```python
    from setuptools import setup, find_packages

    setup(
        name="example_package",
        version="0.1",
        packages=find_packages()
    )
    ```

4. 现在你可以在你的项目的根目录中运行`python setup.py install`，这会在你的环境中安装你的包。你可以在Python解释器中导入你的包并运行你的`hello`函数：
    ```python
    from example_package import hello
    hello()
    ```

5. 如果你的函数运行正确，你可以创建一个PyPI账户，并安装`twine`：`pip install twine`。

6. 然后你可以创建一个源码发行版（source distribution）和一个轮子发行版（wheel distribution）：
    ```bash
    python setup.py sdist
    python setup.py bdist_wheel
    ```

7. 最后，你可以使用`twine`上传你的发行版到PyPI：
    ```bash
    twine upload dist/*
    ```

--
git remote set-url origin ..
git push ok 

----


kang@Love-Grace example_package$ tree
.
├── build
│   ├── bdist.macosx-12-arm64
│   └── lib
│       └── example_package
│           └── __init__.py
├── dist
│   └── example_package-0.1-py3.11.egg
├── example_package
│   ├── __init__.py
│   └── __pycache__
│       └── __init__.cpython-311.pyc
├── example_package.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
└── setup.py




这些文件和文件夹是 Python 打包和分发工具生成的。下面是每个文件和文件夹的简单描述：

1. `build/`: 这个文件夹包含了 Python 的安装进程中使用的所有临时文件。你不需要担心这个文件夹里的内容，这是由 setup.py 安装进程自动创建和管理的。

2. `dist/`: 当你运行 `python setup.py sdist bdist_wheel` 命令时，所有的发行版（即打包的文件）都会放在这个文件夹中。在这个例子中，你看到的 `example_package-0.1-py3.11.egg` 是一个 Egg 分发，这是一种用于 Python 包的二进制分发格式。

3. `example_package/`: 这个文件夹是你的实际 Python 包。它包含你写的所有 Python 代码和资源文件。在这个例子中，它包含一个 `__init__.py` 文件，这是 Python 包的标准部分。

4. `example_package.egg-info/`: 这个文件夹包含了分发元数据，也就是关于你的包的信息，如名称、版本、作者等。这是由 `python setup.py` 命令创建的。

5. `setup.py`: 这是一个 Python 脚本，用于从你的源代码创建分发内容。当其他人想安装你的包时，这个脚本会被运行。

6. `__pycache__/` 和 `.pyc` 文件: 当你运行一个 Python 程序时，Python 会编译你的 `.py` 文件到 `.pyc` 文件，这些文件在 `__pycache__` 文件夹下。这样做可以加速 Python 的加载和运行时间。这些文件对你的源码分发没有影响，可以忽略。

在你将你的 Python 包上传到 PyPI 时，你会将 `dist/` 文件夹中的内容上传，而不是其他的文件和文件夹。


---制作发行版本
├── dist
│   ├── example_package-0.1-py3-none-any.whl
│   ├── example_package-0.1-py3.11.egg
│   └── example_package-0.1.tar.gz

------
准备发行：

关于改名：
你需要更改你的 `setup.py` 文件中的 `name` 字段。这是你的项目在 PyPI 上的名称，所以如果 "example-package" 已经被使用了，你需要将它更改为其他独特的名称。

这是 `setup.py` 文件的一部分示例：

```python
from setuptools import setup, find_packages

setup(
    name="your-unique-package-name",  # 更改这里的名称
    version="0.1",
    packages=find_packages(),
)
```

在这个示例中，你需要将 "your-unique-package-name" 更改为你选择的新名称。

之后你需要重新运行 `python setup.py sdist bdist_wheel` 以生成新的发行版，然后你可以尝试再次上传：`twine upload dist/*`。
-----

关于版本更新：

是的，你可以保持相同的包名（例如 "kanglib"），并在这个包内部进行代码的修改、添加或删除。每次你做出改变并想要将新版本发布到PyPI时，你需要更改`setup.py`文件中的`version`字段，以表示这是一个新版本的包。

例如，如果你开始时将版本设置为"0.1"，然后你对代码进行了修改并准备发布新版本，你可以将版本更新为"0.2"。在这个过程中，包名可以保持不变。

注意：在使用 `twine upload dist/*`上传新版本时，旧版本的发行版仍将保留在PyPI上，用户也可以选择下载旧版本的包。如果你想要删除旧的发行版，你需要登录到你的PyPI账户，进入项目管理页面进行删除操作。
---

关于版本更新

如果你想彻底改变项目的结构并且完全脱离 `example_package` 的相关内容，你可以按照下述步骤来操作：

1. 首先删除你项目中 `example_package` 的相关文件和文件夹，同时也删除 `build`、`dist`、`kanglib.egg-info`、`example_package.egg-info` 这四个目录。

2. 然后你可以重新创建一个名为 `kanglib` 的目录，并在该目录下创建一个 `__init__.py` 文件。你可以将 `hello` 函数定义在这个文件里。这样，你的目录结构应该看起来像这样：

   ```
   .
   ├── kanglib
   │   └── __init__.py
   └── setup.py
   ```

3. 接着，你需要在 `setup.py` 文件中更新包名和版本号。确保在 `setup()` 函数中 `name` 参数设为 'kanglib'，`version` 参数设为 '0.2'。

4. 现在你可以重新生成你的发布包。首先运行 `python setup.py sdist bdist_wheel` 来生成新的发行版。

5. 最后，使用 `twine upload --skip-existing dist/*` 来上传新版本的包。`--skip-existing` 参数会跳过已经存在的同名版本，只上传新的版本。

6. 现在你可以在 PyPI 网站上看到新的 'kanglib' 0.2 版本。同时，你也可以通过 `pip install --upgrade kanglib` 来升级到新版本。

注意，这个过程将会完全删除你之前所有与 `example_package` 相关的内容，并且在你的包中只保留 `kanglib` 和它下面的 `hello` 函数。
------
`twine upload --skip-existing dist/*`
----
-----
完成第一项工具，下面尽心刚测试

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

--
配置 kangtools


