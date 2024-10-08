"""
### 题目描述

给一个多项式函数$f(x)=\sum_{i=0}^n a_i x^i$，对于每一个给出的x的值，计算并输出$f(x)$的值

### 输入格式

输入共两行。

第一行为一个数，即多项式函数中的x。

第二行为多项式函数，用latex格式展示。

latex是一种用于在文档中插入数学公式的标记语言，它支持各种数学符号和公式，可以用于在文档中插入数学公式。例如，x的n次方在latex中就写为：

```text
x^n
```

多项式函数x的平方加上2倍x的5次方写作:

```text
x^2+2x^5
```

### 样例

#### 输入

<pre>
4
x^2
</pre>

#### 输出

<pre>
16
</pre>

### 数据范围

$x<100$
"""
import os
import random
root = os.path.dirname(__file__)
inputpre = "t"
inputsuf = '.in'
outputpre = "t"
outputsuf = '.out'
batch = 20


import random


def generate_data():
    # 定义多项式的最高次数
    max_degree = 5
    # 定义多项式的项数
    num_terms = random.randint(1, max_degree)

    # 生成多项式的系数和指数
    coefficients = []
    exponents = []
    for _ in range(num_terms):
        exponent = random.randint(1, max_degree)
        while exponent in exponents:  # 确保指数不重复
            exponent = random.randint(1, max_degree)
        exponents.append(exponent)
        coefficient = random.randint(1, 10)  # 系数范围1到10
        coefficients.append(coefficient)

    # 生成多项式的字符串表示形式
    polynomial_str = ""
    for i in range(len(coefficients)):
        if coefficients[i] > 0 and i != 0:
            polynomial_str += "+"
        if abs(coefficients[i]) != 1 or exponents[i] == 0:
            polynomial_str += str(abs(coefficients[i]))
        if exponents[i] > 0:
            polynomial_str += "x"
            if exponents[i] > 1:
                polynomial_str += "^" + str(exponents[i])

    # 生成x的值
    x_value = random.randint(0, 99)  # x的值小于100

    return x_value, polynomial_str


# 生成并打印数据
# x, polynomial = generate_data()
# print(x)
# print(polynomial)


def evaluate_polynomial(x, polynomial_str):
    # 先将polynomial_str的每个加号后面都加上一个(，将polynomial_str的每个加号前面都加上一个)
    polynomial_str = polynomial_str.replace('+', ')+(')
    polynomial_str = '('+ polynomial_str + ')'
    polynomial_str = polynomial_str.replace('(x', '(1x')
    polynomial_str = polynomial_str.replace('x', '*(x')
    polynomial_str = polynomial_str.replace(')', '))')
    polynomial_str = polynomial_str.replace('^', '**')
    result = eval(polynomial_str)
    return result

"""
# 读取输入
# x, polynomial_str = generate_data()

x, polynomial_str = 81, 'x^4+10x+9x^3'
# 计算多项式的值
result = evaluate_polynomial(x, polynomial_str)

# 输出结果
print(x)
print(polynomial_str)
print(result)




"""

for i in range(0, batch+1):
    with open(inputpre + str(i) + inputsuf, 'w') as f:
        x, polynomial_str = generate_data()
        f.write(str(x) + '\n')
        f.write(polynomial_str + '\n')
        f.close()
    print(polynomial_str)
    with open(outputpre + str(i) + outputsuf, 'w') as f:
        f.write(str(evaluate_polynomial(x, polynomial_str)) + '\n')
        f.close()
