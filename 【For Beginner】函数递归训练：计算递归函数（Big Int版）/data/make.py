"""
### 题目描述

递归是一个很重要的编程概念，其含义是函数通过调用自身解决问题。

以计算函数为例，用稍微规范一点的语言描述，可以这样写：

若要计算函数$f(x)$，已知其表达式为:

- $f(x)=g[f(x-1)]，x>1$
- $f(1)=A$
- $A$为常数

时，该函数为递归函数，计算该函数的值，则可以递归地求解。

具体而言，上述递归函数的计算过程如下：

1. 若$x=1$，则$f(x)=A$，计算结束。
2. 若$x>1$，则$f(x)=g[f(x-1)]$，计算$f(x-1)$，然后计算$f(x)$，计算结束。

本题中，函数$f(x)$的表达式为：

1. $f(x)=x^2+x+1+\lg[(f(x-1)^{100000}], x>1$
2. $f(1)=1$

给定x，计算函数值，保留到小数点后6位。

### 输入格式

一个数x。

### 输出格式

一个数，为函数值。

### 样例

#### 输入

<pre>
18
</pre>

#### 输出

<pre>
576413.493644
</pre>


### 数据范围

x <= 50


"""
import math
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
        x = random.randint(1, 50)
        print(x)
        f.write(str(x))

    with open(os.path.join(root, outputpre + str(i) + outputsuf), 'w') as f:
        def solve(n):
            if n <= 1:
                return 1
            else:
                return n ** 2 + n + 1 + 100000*math.log10(solve(n - 1))

        # 输出函数值到文件，保留到小数点后6位
        f.write("%.6f" % solve(x))
