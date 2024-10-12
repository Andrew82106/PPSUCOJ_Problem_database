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


# 读取输入
A, B, C, D = map(int, input().split())

# 计算并输出结果
print(calculate_ways(A, B, C, D))
