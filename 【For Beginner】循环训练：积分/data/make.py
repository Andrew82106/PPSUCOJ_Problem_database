"""
### 题目描述

高等数学中的积分一般是对于连续函数而言（连续函数就是每个地方都有值的函数）。对于函数$f(x)$，其在$[a,b]$上的积分写作：

$\int_{a}^b f(x)dx$

这个式子的含义是在区间$[a,b]$上将函数$f(x)$的值加起来。

但是对于计算机而言，连续函数是没法直接积分的，因此一般会将函数离散后进行近似的积分。

本题将函数$f(x)=Ax^3+Bx^2+Cx+D$放在整数域中进行离散化（这意味着函数只在整数处有值），请编写程序求积分$\int_{a}^b f(x)dx$


### 输入格式

输入第一行为函数的系数A，B，C，D，以空格分隔。

输入第二行为积分的下限a，上限b，以空格分隔。

输入第三行为函数中变量x的取值。


### 输出格式

计算$\int_{a}^b f(x)dx = \int_{a}^b (Ax^3+Bx^2+Cx+D)dx$

### 样例

#### 输入

<pre>
0 0 1 0
0 10
10
</pre>

#### 输出

<pre>

</pre>

### 样例解释

函数系数为``0 0 1 0``，即函数为$f(x)=x$，函数在区间$[0,10]$上有值为$0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10$

则对该函数积分等价于把这些值加起来，故

$\int_{0}^{10} f(x)dx = 0+1+2+3+4+5+6+7+8+9+10 = 55$

### 数据范围

$A,B,C,D<50$

$-100 < a < b <100$

$-100 < x < 100$
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
        A, B, C, D = random.randint(-50, 50), random.randint(-50, 50), random.randint(-50, 50), random.randint(-50, 50)
        a, b = random.randint(-100, 100), random.randint(-100, 100)
        x = random.randint(-100, 100)
        f.write(f"{A} {B} {C} {D}\n{a} {b}\n{x}")
    with open(os.path.join(root, outputpre + str(i) + outputsuf), 'w') as f:
        res = 0
        for i in range(a, b + 1):
            res += A * (i ** 3) + B * (i ** 2) + C * i + D
        f.write(f"{res}")