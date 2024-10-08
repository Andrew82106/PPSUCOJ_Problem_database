"""
作为入门题，显然是不会为难大家的，但是普通的Hello World又太简单了，因此我们来一点好玩的。

输入一个数字n，如果:

- 这个数字是2的倍数，则输出一次`Hello World!\n`
- 这个数字是3的倍数，则输出一次`Hello PPSUC!\n`
- 这个数字是5的倍数，则输出一次`Hello CyberSWAT!\n`
- 这个数字是7的倍数，则输出一次`Hello C/C++!\n`
- 这个数字是11的倍数，则输出一次`Hello Python!\n`
- 这个数字是13的倍数，则输出一次`Hello Java!\n`
- 这个数字是17的倍数，则输出一次`Hello PHP!\n`
"""
import os
import random
root = os.path.dirname(__file__)
inputpre = "t"
inputsuf = '.in'
outputpre = "t"
outputsuf = '.out'
batch = 10
for i in range(1, batch+1):
    filename = inputpre + str(i) + inputsuf
    with open(os.path.join(root, filename), 'w') as f:
        n = random.randint(1, 1000)
        f.write(str(n) + '\n')
    filename = outputpre + str(i) + outputsuf
    with open(os.path.join(root, filename), 'w') as f:
        if n % 2 == 0:
            f.write('Hello World!\n')
        if n % 3 == 0:
            f.write('Hello PPSUC!\n')
        if n % 5 == 0:
            f.write('Hello CyberSWAT!\n')
        if n % 7 == 0:
            f.write('Hello C/C++!\n')
        if n % 11 == 0:
            f.write('Hello Python!\n')
        if n % 13 == 0:
            f.write('Hello Java!\n')
        if n % 17 == 0:
            f.write('Hello PHP!\n')
# 生成10个测试数据
