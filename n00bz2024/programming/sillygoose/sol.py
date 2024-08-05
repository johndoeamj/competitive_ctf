import socket

def binary_search_guess():
    host = '24.199.110.35'
    port = 41199

    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Initialize binary search bounds
    low = 0
    high = 10**100
    turns = 0

    while turns < 500:
        turns += 1
        guess = (low + high) // 2
        s.sendall(f"{guess}\n".encode())

        # Receive the response
        response = s.recv(1024).decode().strip()
        print(response)

        if "too large" in response:
            high = guess - 1
        elif "too small" in response:
            low = guess + 1
        elif "congratulations" in response:
            break
        elif "you ran out of time" in response or "you are no fun" in response or "you have a skill issue" in response:
            break

    s.close()

if __name__ == "__main__":
    binary_search_guess()

