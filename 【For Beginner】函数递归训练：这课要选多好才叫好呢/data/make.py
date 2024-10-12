"""
### 题目描述

一年一度的选课又开始了，面对满屏幕的课程，你开始畅想自己在大学四年的过程中在知识的海洋中遨游的样子，想必到了毕业的时候，自己一定会成为学识渊博的人吧。

但是你现在可没时间幻想，因为你需要在最快的时间内规划出自己的选课计划（因为再慢的话课就被抢光了！

选课系统采用了当前最先进的管道式设计，这意味着你只能按照系统给出的课程顺序去选课。具体而言，对于所有的n门课程，

- 每门课程有一个分数，你选择了这门课程，你就可以获得这门课程的分数

- 当你选择了第i门课程，其分数为j，那么下一次你就只能从第i+j到n中选择课程，而不能从1到i-1中选择课程

现在给你n门课程，以及这n门课程的分数，请你计算出你最多能获得多少分。


### 输入格式

第一行一个整数n，表示课程的数量。

第二行n个整数，表示这n门课程的分数score。

### 输出格式

输出一个整数，表示你最多能获得的分数。

### 样例

#### 输入

<pre>
4
5 7 1 19
</pre>

#### 输出

<pre>
20
</pre>

### 样例解释

课程1获得5分，课程2获得7分，课程3获得1分，课程4获得19分，所以最多能获得的分数是1+19=20。

### 数据范围

n <= 1000

1 <= score <= 100
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


def max_score_recursive(i, scores, n):
    # 如果当前课程索引超出范围，返回0
    if i >= n:
        return 0

    # 选择当前课程，并递归计算从下一门可以选择的课程开始的最高分数
    score_with_current = scores[i] + max_score_recursive(i + scores[i], scores, n)

    # 不选择当前课程，直接递归计算下一门课程的最高分数
    score_without_current = max_score_recursive(i + 1, scores, n)

    # 返回两种选择的最高分数
    return max(score_with_current, score_without_current)



for i in range(0, batch + 1):
    with open(os.path.join(root, inputpre + str(i) + inputsuf), 'w') as f:
        n = random.randint(1, 100)
        scores = [random.randint(1, 100) for _ in range(n)]
        f.write(str(n) + '\n')
        f.write(' '.join(map(str, scores)))

    with open(os.path.join(root, outputpre + str(i) + outputsuf), 'w') as f:
        f.write(str(max_score_recursive(0, scores, n)))