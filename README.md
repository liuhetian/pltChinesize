# pltChinesize
一键解决matplotlib.pyplot和sns不支持中文的问题，主要针对mac和linux服务器，windows不清楚

## 使用方法
将ttf文件和main.py放在一起，然后
```shell
python main.py
```
会输出一串字符，这个字符就是字体的名字。字体名字和字体的文件名不是一个东西。

## 测试是否成功
```python
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = '这里写上面的脚本输出的字体名字'
plt.rcParams['axes.unicode_minus'] = False

a = np.array([5, 20, 15, 25, 10])
b = np.array([10, 15, 20, 15, 5])
plt.barh(range(len(a)), a)
plt.barh(range(len(b)), -b)
plt.title('你好')
plt.save('test.jpg')
```
