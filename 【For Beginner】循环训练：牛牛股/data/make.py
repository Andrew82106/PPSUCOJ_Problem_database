"""
### 题目描述

最近股票暴涨，所有版块一片通红，越来越多的人也想要购买股票，幻想着追高赚一把。

带着这样的想法，小A决定买一些股票，但是小A并不知道他现在选的这个股票是否好，因此找到了精通计算机的你来帮他的忙。

小A整理了一支股票最近n天的股价，他现在想让你帮忙分析一下，这只股票有多少天涨了，并且计算出涨的天数占总天数的比例。

小A定义，如果一个股票比他前面的一天的价格高，那就是涨了。对于第一天，由于没有前一天，那也默认是涨了，因为他比较自信。

### 输入格式

输入第一行为n，即小A搜集的天数。

接下来一行n个整数，表示第i天的股价。

### 输出格式

n天中股票涨了的天数的比例，保留到小数点后4位。

### 样例

#### 输入

<pre>
6
1 2 3 3 3 3
</pre>

#### 输出

<pre>
0.5000
</pre>

### 样例解释

样例中1到3天都算涨了，其他的没有。因此涨了3天，占总天数的0.5，即50%，所以输出0.5000。

### 数据范围

$n < 10000$

$0 < a_i < 10000$
"""
import os
import random

root = os.path.dirname(__file__)
inputpre = "t"
inputsuf = '.in'
outputpre = "t"
outputsuf = '.out'
batch = 20


for i in range(0, batch + 1):
    with open(os.path.join(root, inputpre + str(i) + inputsuf), 'w') as f:
        n = random.randint(1, 10000)
        A = []
        f.write(str(n) + '\n')
        for j in range(0, n):
            A.append(random.randint(0, 10000))
        f.write(' '.join(str(x) for x in A))
    with open(os.path.join(root, outputpre + str(i) + outputsuf), 'w') as f:
        up = 1
        for j in range(1, n):
            if A[j] > A[j - 1]:
                up += 1
        f.write('{:.4f}'.format(up / n))
