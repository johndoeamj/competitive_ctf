import socket

def find_max_path(eggs):
    n = len(eggs)
    dp = [[0] * n for _ in range(n)]
    path = [[''] * n for _ in range(n)]

    # Initialize the starting point
    dp[0][0] = eggs[0][0]

    # Fill the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + eggs[0][j]
        path[0][j] = 'r'

    # Fill the first column
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + eggs[i][0]
        path[i][0] = 'd'

    # Fill the rest of the dp table
    for i in range(1, n):
        for j in range(1, n):
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j] + eggs[i][j]
                path[i][j] = 'd'
            else:
                dp[i][j] = dp[i][j-1] + eggs[i][j]
                path[i][j] = 'r'

    # Reconstruct the path
    max_path = []
    x, y = n-1, n-1
    while x > 0 or y > 0:
        max_path.append(path[x][y])
        if path[x][y] == 'd':
            x -= 1
        else:
            y -= 1
    max_path.reverse()

    return dp[n-1][n-1], ''.join(max_path)

def read_until_optimal(sock):
    buffer = bytearray()
    chunk_size = 4096  # Larger chunk size
    while True:
        data = sock.recv(chunk_size)
        if not data:
            break
        buffer.extend(data)
        if b"optimal" in buffer:
            break
    return bytes(buffer)

# Connect to the server
host = '24.199.110.35'
port = 43298
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

try:

    for _ in range(10):
        #print("Fetching grid...")
        result = read_until_optimal(sock)

        response = result.decode('utf-8')
        #print(response)

        response_lines = response.splitlines()
        n_lines = len(response_lines)
        #print(f"n_lines: {n_lines}")
        #if n_lines < 5:
        #    print(f"response_lines: {response_lines}")
        #print(f"lastLine: {response_lines[-1]}")

        #reconstruct grid skipping last line
        grid = []
        for line in response_lines[:-1]:
            row = [int(x) for x in line.split()]
            grid.append(row)
        #print("Reconstructed grid. Calculating best path...")

        max_score, max_path = find_max_path(grid)
        sock.sendall(f"{max_path}\n".encode('utf-8'))

        #print(f"Done. Sent best path with SCORE={max_score} to the server.")

    # get flag
    data = sock.recv(4096).decode('utf-8')
    print(data)


finally:
    # Close the socket connection
    sock.close()
