import random, time

random.seed(2222)
n = 3
start = time.time()

eggs = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(0, 9))
        print(row[j], end=' ')
    eggs.append(row)
    print()

# Dynamic Programming to find the max score
dp = [[0] * n for _ in range(n)]
dp[0][0] = eggs[0][0]

for i in range(n):
    for j in range(n):
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + eggs[i][j])
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + eggs[i][j])

print("DP")
for i in range(n):
    for j in range(n):
        print(dp[i][j], end=" ")
    print()



# Reconstruct the path
path = []
x, y = n-1, n-1
while x > 0 or y > 0:
    if x == 0:
        path.append('r')
        y -= 1
    elif y == 0:
        path.append('d')
        x -= 1
    elif dp[x-1][y] > dp[x][y-1]:
        path.append('d')
        x -= 1
    else:
        path.append('r')
        y -= 1
path.reverse()
inputPath = ''.join(path)


maxScore = dp[n-1][n-1]
print(maxScore)
print(inputPath)

for v, i in enumerate(inputPath):
    if v == 'r':
        inputPath[i] = 'd'
    elif v == 'r':
        inputPath[i] = 'd'
# Use the calculated path to verify the score

inputAns = eggs[0][0]
x = 0
y = 0

for direction in inputPath:
    match direction:
        case 'r':
            x += 1
        case 'd':
            y += 1
        case _:
            exit()

    if x == n or y == n:
        print("out of bounds")
        exit()

    inputAns += eggs[x][y]
    print(f"CALC_SCORE: {inputAns}, (x,y): ({x},{y})")
print("CALC_SCORE: ", inputAns)

assert inputAns == maxScore, f"Calculated score {inputAns} does not match max score {maxScore}"

print("Thanks for finding all my eggs")
f = open("/flag.txt.txt", "r")
print(f.read())
