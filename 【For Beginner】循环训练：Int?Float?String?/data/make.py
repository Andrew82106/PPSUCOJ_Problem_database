"""
### 题目描述

Int是指整数，在Python中一个整数变量可以存很大很大的数字，但在C和C++中，整数包含了int类型，long类型，long long类型等等，不同的类型存放的数的大小不一样。

Float是指浮点数，在Python中一个浮点数变量可以存很大很大的数字，但在C和C++中，浮点数包含了float类型，double类型等等，不同的类型存放的数的精度也不一样。

String是指字符串，在Python中一个字符串变量可以存任意长度的字符串，但在C和C++中，字符串只能存一定长度的字符串。

但在本题中，Int泛指所有的整数， Float泛指所有的浮点数（小数）， String泛指所有的字符串。

输入n个值，输出对应的值的类型。

### 输入格式

输入第一行是n，代表值的个数

接下来的n行，每行一个值，其类型可能是Int，Float，String。

### 输出格式

输出n行每行一个字符串，代表对应的值的类型。

如果是Int类型的，则输出Int， 如果是Float类型的，则输出Float， 如果是String类型的，则输出String。

### 样例

#### 输入

<pre>
0.1
0.2
PPSUC Cyber SWAT
11451
</pre>

#### 输出

<pre>
Float
Float
String
Int
</pre>

### 样例解释

第一个值是0.1，是小数；

第二个值是0.2，是小数；

第三个值是PPSUC Cyber SWAT，是字符串；

第四个值是11451，是整数。

因此输出：
```text
Float
Float
Float
String
Int
```

### 数据范围

$n<100$
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
        n = random.randint(1, 100)
        # n = 2
        f.write(str(n) + '\n')
        A = []
        for j in range(0, n):
            seed = random.randint(0, 10)
            if seed % 3 == 0:
                # 向A中添加一个小数
                A.append(str(random.uniform(0, 1000000)))
            elif seed % 3 == 1:
                # 向A中添加一个只包含字母的字符串
                A.append(str(chr(random.randint(65, 90)) + chr(random.randint(65, 90))))
            else:
                # 向A中添加一个整数
                A.append(str(random.randint(0, 1000000)))

        for j in A:
            f.write(j + '\n')
    with open(os.path.join(root, outputpre + str(i) + outputsuf), 'w') as f:
        for j in A:
            if '.' in str(j):
                f.write('Float\n')
            elif str(j)[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                f.write('String\n')
            else:
                f.write('Int\n')