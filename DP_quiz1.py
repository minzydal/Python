import time

# 점화식
# dp[i] = max(dp[i][j-1], dp[i][j]) + arr[i][j]

# 층 개수
print("층 개수를 입력하세요 : ")
H = int(input())

int_triangle = []
print("층 별 값을 입력하세요 : ")
for i in range(H):
    line = list(map(int, input().split(' ')))
    assert len(line) == i + 1
    int_triangle.append(line)

s = time.time()
for i in range(1, H):
    # i 번째 층 길이
    length = len(int_triangle[i])

    # 층의 원소들을 계산
    for j in range(length):
        # 층의 맨 앞자리 값은 이전 층의 첫 번째 값을 더한 것
        if j == 0:
            int_triangle[i][j] += int_triangle[i - 1][j]
            continue

        # 층의 마지막 자리 값은 이전 층의 마지막 값을 더한 것
        if j == length - 1:
            int_triangle[i][j] += int_triangle[i - 1][j - 1]
            continue

        # 그 외는 점화식에 따라 계산
        int_triangle[i][j] += max(int_triangle[i - 1][j - 1], int_triangle[i - 1][j])
e = time.time()

# 마지막 층의 최대 값을 출력
print("마지막 층의 최대 값 : ", max(int_triangle[H - 1]))
# 수행시간 출력
print("수행 시간: {0:3.6f}초".format(e - s))