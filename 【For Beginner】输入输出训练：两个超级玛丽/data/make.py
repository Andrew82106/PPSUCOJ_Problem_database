"""
你问为什么酒馆老板能够招到这么多随从？因为他有漏斗蛋糕！

输入一个数字n，输出一个高度为n的漏斗蛋糕。

高度为1的漏斗蛋糕如下：

```text
*
```
高度为2的漏斗蛋糕如下：
```text
**
*
```
高度为3的漏斗蛋糕如下：
```text
***
**
*
```
"""
import os
import random
root = os.path.dirname(__file__)
inputpre = "t"
inputsuf = '.in'
outputpre = "t"
outputsuf = '.out'
batch = 10
for i in range(0, batch+1):
    with open(os.path.join(root, inputpre + str(i) + inputsuf), 'w') as f:
        n = str(random.randint(1, 100))
        f.write(n + '\n')
    with open(os.path.join(root, outputpre + str(i) + outputsuf), 'w') as f:
        for j in range(int(n)):
            for k in range(j+1):
                f.write('*')
            f.write('\n')