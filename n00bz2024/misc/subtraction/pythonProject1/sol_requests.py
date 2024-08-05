import socket

import numpy as np

def get_median(lst):
    return round(np.median(lst))

def update_list(a, c):
    return [abs(c - x) for x in a]

def get_mean(lst):
    return round(np.mean(lst))

def read_until_newline(sock):
    buffer = bytearray()
    chunk_size = 4096  # Larger chunk size
    while True:
        data = sock.recv(chunk_size)
        if not data:
            break
        buffer.extend(data)
        if b"\n" in buffer:
            break
    return bytes(buffer)
def main():
    host = 'challs.n00bzunit3d.xyz'
    port = 10270

    # Connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        print("fetching array...")
        initial_array_data = read_until_newline(s)
        initial_array = initial_array_data.decode('utf-8').strip().split(' ')
        a = list(map(int, initial_array))

        print(f"Done. len: {len(a)}")

        prev_len = -1
        # Interact with the server
        for turns in range(20):

            c = get_median(a)

            if len(set(update_list(a, c))) <= prev_len + 10:
                c = round(max(a) // 2)

            # Send the value of c to the server
            s.sendall(f'{c}\n'.encode())

            # Update the list according to the rule
            a = update_list(a, c)

            prev_len = len(set(a))

            # Receive the server's response (this example assumes a single response per input)
        response_data = s.recv(1024).decode().strip()
        print("resp:", response_data)

if __name__ == "__main__":
    main()
