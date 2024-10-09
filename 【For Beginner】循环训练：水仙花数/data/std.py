n = int(input())
for j in range(1, n + 1):
    if sum(map(lambda x: int(x) ** 3, str(j))) == j:
        print(j)