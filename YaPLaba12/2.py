def min_sum_path(N, board):
    dp = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j] = board[i][j]
            elif i == 0:
                dp[i][j] = board[i][j] + dp[i][j-1]
            elif j == 0:
                dp[i][j] = board[i][j] + dp[i-1][j]
            else:
                dp[i][j] = board[i][j] + min(dp[i][j-1], dp[i-1][j])

    return dp[N-1][N-1]


with open('input.txt', 'r') as file:
    N = int(file.readline().strip())
    board = [list(map(int, file.readline().strip().split())) for i in range(N)]

min_sum = min_sum_path(N, board)

with open('output.txt', 'w') as file:
    file.write(str(min_sum))
