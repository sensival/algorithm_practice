# n x m 크기의 금광이 있습니다.각 칸은 특정한 크기의 금이 들어있습니다. (1,1) ~ (n,m)의 좌표가 있고 1번째 열부터 시작하여 m번 동안 오른쪽위, 오른쪽아래, 오른쪽으로 이동할수 있다.
# 가장 많이 채굴 할 수 있는 금의 크기를 구하시오.
# 첫째줄에 테스트케이스 개수가 입력되고, 둘째줄부터 테스트 케이스 마다 n m 이 주어지고, 다음줄에 매장된 금의 개수가 주어집니다.

# 입력예시
# 2
# 3 4 
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

# 출력
# 19
# 16
for tc in range(int(input())):
    n, m = map(int, input().split()) # 행n 열m 입력
    array =list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    for j in range(1, m):
        for i in range(n): # 첫 행~
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            if i == n -1:
                left_down = 0

            else:
                left_down = dp[i + 1][j - 1]
            
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)
            
