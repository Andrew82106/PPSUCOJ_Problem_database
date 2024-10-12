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


# 测试样例
n = int(input())
score = input()
scores = [int(score) for score in score.split()]
print(max_score_recursive(0, scores, n))

