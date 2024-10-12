"""
### 题目描述

为了提高同学们的体能水平，学校组织了校园乐跑活动。具体的规则是，在A周教学周内需要跑总计B公里。

在经过一周的测试后，小A发现自己一周最多只能跑C公里，再多跑身体就受不了了。

但是为了完成体能锻炼的任务，更好的提升自己的能力，小A觉得每周他至少要跑D公里。

小A希望你帮他计算出，在他可接受的上述规则下，每周的跑步公里数有多少种分配方式？

### 输入格式

输入包含一行，包含四个整数A、B、C、D，用空格隔开。


### 输出格式

输出包含一行，包含一个整数，表示符合要求的分配方式总数。


### 样例

#### 输入

<pre>
2 10 6 1
</pre>

#### 输出

<pre>
3
</pre>

### 样例解释

小A每周最多只能跑6公里，最少要跑1公里，由于一共要跑10公里，则可行的分配方式如下：

- 第一周 6公里，第二周 4公里
- 第一周 5公里，第二周 5公里
- 第一周 4公里，第二周 6公里


总共 3 种分配方式。

### 数据范围

0<A<10

1<B<100

0<D<C<50
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


def calculate_ways(weeks, remaining_distance, max_distance, min_distance):
    # 如果剩余的周数为0，检查剩余的距离是否为0
    if weeks == 0:
        return 1 if remaining_distance <= 0 else 0

    if remaining_distance <= 0 and weeks >= 0:
        return 1

    ways = 0
    # 遍历当前周的所有可能距离
    for distance in range(min_distance, max_distance + 1):
        # 递归计算剩余周数的分配方式
        ways += calculate_ways(weeks - 1, remaining_distance - distance, max_distance, min_distance)

    return ways



for i in range(0, batch + 1):
    with open(os.path.join(root, inputpre + str(i) + inputsuf), 'w') as f:
        A, B, C = random.randint(1, 10), random.randint(1, 100), random.randint(1, 50)
        D = random.randint(1, C)
        f.write(str(A) + ' ' + str(B) + ' ' + str(C) + ' ' + str(D))

    with open(os.path.join(root, outputpre + str(i) + outputsuf), 'w') as f:
        f.write(str(calculate_ways(A, B, C, D)))
