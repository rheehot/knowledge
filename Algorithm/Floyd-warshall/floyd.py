import sys

# 무한대 가정
INF = int(1e9)

# 노드와 간선의 갯수
n, m = map(int, sys.stdin.readline().split())

# 2차원 그래프를 INF로 초기화
matrix = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기자신으로 가는 경로는 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            matrix[i][j] = 0

# 각 간선의 정보로 행렬 초기화
for _ in range(m):
    # c = a에서 b로 가는 비용
    a, b, c = map(int, sys.stdin.readline().split())
    matrix[a][b] = c

# 플로이드 워셜 알고리즘 수행 => 경유지, 출발지, 도착지 순으로 반복문 수행
# 경유지 k
for k in range(1, n + 1):
    # 출발지 a
    for a in range(1, n + 1):
        # 도착지 b
        for b in range(1, n + 1):
            matrix[a][b] = min(matrix[a][b], matrix[a][k] + matrix[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할수 없는 경로라면 INF 출력
        if matrix[a][b] == 1e9:
            print("INF", end=" ")
        else:
            print(matrix[a][b], end=" ")
    print()
