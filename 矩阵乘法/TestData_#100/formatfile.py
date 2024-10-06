import os

目录路径 = "/Users/andrewlee/Desktop/Projects/网特/PPSUCOJ题目/矩阵乘法/TestData_#100"
文件列表 = os.listdir(目录路径)

for 旧文件名 in 文件列表:
    if 旧文件名.endswith('.in') or 旧文件名.endswith('.out'):
        新文件名 = 't' + 旧文件名
        旧文件路径 = os.path.join(目录路径, 旧文件名)
        新文件路径 = os.path.join(目录路径, 新文件名)
        os.rename(旧文件路径, 新文件路径)
        print(f"已将文件 {旧文件名} 重命名为 {新文件名}")