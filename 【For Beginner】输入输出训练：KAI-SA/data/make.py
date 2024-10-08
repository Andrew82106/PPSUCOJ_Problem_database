"""
### 题目描述

凯撒加密是一种古老的加密方式，它将字母表中的每个字母替换为字母表中固定位置之后的字母。例如，如果我们将字母表中的每个字母替换为字母表中固定位置之后的字母，那么字母A将被替换为字母B，字母B将被替换为字母C，以此类推。字母表中的最后一个字母Z将被替换为字母A。

我们将凯撒加密中字母替换的位置定义为参数$n$，比如，当$n=3$时， 字母A将被替换为字母D，字母B将被替换为字母E，以此类推。字母表中的最后一个字母Z将被替换为字母C。

现在，犯罪分子的电脑中有一段密文，密文以分号分隔句子，并且句子中存在一些多余的数字。作为公安技术的拔尖人才，你需要将这段密文分句，并且去除其中多余的数字，最后解密剩下的文字，将解密后的文字输出。

### 输入输出格式
输入包含两行，第一行一个数字，为参数$n$，$n<26$。接下来一行，一个字符串，为密文。

输出包含多行，为解密结果。
```
"""
import os
import random
import copy

root = os.path.dirname(__file__)
inputpre = "t"
inputsuf = '.in'
outputpre = "t"
outputsuf = '.out'
batch = 10

def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isupper():
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted += char
    return encrypted


def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isupper():
            decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            decrypted += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted += char
    return decrypted


for i in range(0, batch + 1):
    with open(os.path.join(root, f"{inputpre}{i}{inputsuf}"), 'w') as f:
        n = random.randint(0, 25)
        ori = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=100))
        Str = caesar_encrypt(ori, n)
        # 向Str中多次加入数字
        Str1 = copy.deepcopy(Str)
        for _ in range(10):
            start = random.randint(0, len(Str1))
            Str1 = Str1[:start] + str(random.randint(0, 10000)) + Str1[start:]

        ori2 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=100))
        Str2 = caesar_encrypt(ori2, n)
        # 向Str2中多次加入数字
        for _ in range(10):
            start = random.randint(0, len(Str2))
            Str2 = Str2[:start] + str(random.randint(0, 10000)) + Str2[start:]
        f.write(f"{n}\n{Str1};{Str2}")
    with open(os.path.join(root, f"{outputpre}{i}{outputsuf}"), 'w') as f:
        f.write(ori+"\n"+ori2)
