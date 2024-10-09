"""
### 题目描述

高等数学中的求导高中就讲过，其本质是探究函数的变化速度。显然，和积分一样，求导主要也是面对连续函数而言的。对于计算机而言，不太可能直接对连续函数求导。

因此计算机也是先将连续函数离散化后进行近似的求导运算。（当然也有牛顿迭代法这种操作，但那是对于某一个点进行求导）

计算机中，对于一个函数值$f(x)$，其在某个区间的整数域中的函数值序列（长度为n）为$a_1,a_2,..,a_n$，则对该函数进行求导得到的新函数值序列（长度为n-1）可以近似为$a_2-a_1,a_3-a_2,...a_n-a_{n-1}$。

在计算机科学中常常将这种操作称为差分，而非求导。

输入一个函数值序列，输出其求导后的结果序列。

### 输入格式

输入第一行一个整数n，表示函数值序列的长度。

输入第二行n个整数，表示函数值序列。


### 输出格式

输出一行n-1个整数，表示求导后的结果序列。


### 样例

#### 输入

<pre>
5
1 2 3 4 5
</pre>

#### 输出

<pre>
1 1 1 1
</pre>

### 样例解释

根据样例输入，函数值序列为1,2,3,4,5，求导后得到的结果计算过程为：

$2-1=1$

$3-2=1$

$4-3=1$

$5-4=1$

因此输出1 1 1 1。

### 数据范围

对于所有数据，1≤n≤1000，函数值序列中的每个数在[-1000,1000]范围内。
"""

n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    print(a[i] - a[i - 1], end=' ')
