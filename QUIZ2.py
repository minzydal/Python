import sys
import heapq
import time

INF = sys.maxsize
inputs = list(map(int, input().split(' ')))
assert len(inputs) == 2
# V = 정점(Vertex)개수, E = 간선(Edge)개수
V, E = inputs
K = int(input())

# 모든 정점으로부터 모든 정점까지의 가중치를 담은 2차행렬
distance_map = [[float('inf')
                 if i != j else 0
                 for i in range(V)] for j in range(V)]

print(distance_map)

G = [[] for _ in range(V+1)]

for i in range(E):
    inputs = list(map(int, input().split(' ')))
    assert len(inputs) == 3
    u, v, w = inputs # u = 시작 정점
    distance_map[u-1][v-1] = w
    G[u].append([w, v]) #jiwon

s = time.time()
result = [INF for _ in range(V+1)] #결과 저장
result[K] = 0

#우선순위 큐
q = []
heapq.heappush(q, [0,K]) #거리 비교

while q:
    dis, end = heapq.heappop(q) #pop

    if result[end] < dis: #해당 경로가 이전 경로보다 길면
        continue #스킵

    for d, x in G[end]: #노드 탐색
        d += dis
        if d < result[x]:  # 거리를 비교해서
            result[x] = d
            heapq.heappush(q, [d, x])  # 우선순위 큐에 넣어줌

for i in range(1, V+1):
    print(result[i] if result[i] != INF else "INF")
e = time.time()

print("수행 시간: {0:3.6f}초".format(e - s))