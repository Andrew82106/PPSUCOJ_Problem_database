"""
### 题目描述

“从前有坐山，山里有座庙，庙里有个老和尚，老和尚在给小和尚讲故事...”

终于有一天，和尚气愤的表示念经念累了，他就决定把他念过的所有经的内容都输出来以表示抗议。

和尚的经文具有一种特殊的规律，大概是这样的：

- 和尚每一次念经都会在心里敲定一个数字n，这个数字代表了他的念经深度。

- 和尚的经文的模版是：从前有坐山，山里有座庙，庙里有个老和尚，老和尚在给小和尚讲XXX的故事

- 读到XXX的时候，和尚会向XXX中插入一次经文模版

- 当和尚插入了n-1次经文模版后，此时他就认为读经已经达到了念经深度n，此时的经文模版中的XXX就会变成``有趣``

- 在此之后，他会完成剩下的经文

现在，给定一个整数n，求出和尚在读经的时候，他的最终经文是什么。

### 输入格式

一个数字n

### 输出格式

一行一个字符串，表示和尚的经文

### 样例

#### 输入

<pre>
2
</pre>

#### 输出

<pre>
从前有坐山，山里有座庙，庙里有个老和尚，老和尚在给小和尚讲从前有坐山，山里有座庙，庙里有个老和尚，老和尚在给小和尚讲有趣的故事的故事
</pre>

### 样例解释

### 数据范围

$n<30$
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
        n = random.randint(1, 30)
        f.write(str(n))

    with open(os.path.join(root, outputpre + str(i) + outputsuf), 'w') as f:
        def solve(n):
            template = "从前有坐山，山里有座庙，庙里有个老和尚，老和尚在给小和尚讲%s的故事"

            # 使用递归解决上面的问题
            def solve_recursive(n1):
                if n1 == 1:
                    return "有趣"
                else:
                    return template % solve_recursive(n1 - 1)
            return template % solve_recursive(n)

        f.write(solve(n))