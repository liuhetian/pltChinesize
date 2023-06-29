# pltChinesize
一键解决matplotlib.pyplot和sns不支持中文的问题，主要针对mac和linux服务器

windows可以直接使用`plt.rcParams['font.family'] = 'simhei'`

## 使用方法
点击下载压缩包或者
```
git clone https://github.com/liuhetian/pltChinesize.git
```
之后开始运行，脚本会安装同路径下的一个ttf文件，安装完后会输出字体的名字，之后需要用这个字体名字来调用该字体。

自带了微软雅黑字体，也可以自己下载字体放在一起然后运行。
```shell
cd pltChinesize
python main.py
```
会输出一串字符，这个字符就是字体的名字。

## 测试是否成功
```python
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'simhei'  # 这里可以替换
plt.rcParams['axes.unicode_minus'] = False

a = np.array([5, 20, 15, 25, 10])
b = np.array([10, 15, 20, 15, 5])
plt.barh(range(len(a)), a)
plt.barh(range(len(b)), -b)
plt.title('你好')
plt.savefig('test.jpg')
```

## 其他

默认会把字体安装到当前python环境的matplotlib库的字体文件夹，如果运行时增加一个参数`all_users`，就会把字体安装到系统字体文件夹。
```
python main.py all_users
```
