"""
### 题目描述

水仙花数这个问题太经典了，以至于每一个讲C语言的老师都会讲这个。

但是它非常的简单和基础，所以这道题是基础题。

输入n，求出1至n范围内的所有水仙花数。

所谓水仙花数，就是指各位数字立方之和等于该数的数；

例如：因为$153=1^3+5^3+3^3$，所以153是一个水仙花数。

### 输入格式

输入一行，为$n(n<1000)$

### 输出格式

输出1至n范围内的所有水仙花数，每个数占一行。

### 样例

#### 输入

<pre>
1
</pre>

#### 输出

<pre>
1
</pre>

### 数据范围

$n<1000$
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
        n = random.randint(1, 1000)
        f.write(str(n) + '\n')
    with open(os.path.join(root, outputpre + str(i) + outputsuf), 'w') as f:
        for j in range(1, n + 1):
            if sum(map(lambda x: int(x) ** 3, str(j))) == j:
                f.write(str(j) + '\n')
