import socket
import time

# Server address and port
server_address = '24.199.110.35'
server_port = 42189

# Number of questions you want to answer
questions = -1  # bruh...

# Create a socket connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server_address, server_port))

    data = s.recv(1024).decode().strip()
    print(f"[DEBUG] uh?: {data}")

    # Send the number of questions
    print(f"Sending: {questions}")
    s.sendall(f"{questions}\n".encode())

    all_correct = True

    for i in range(questions):
        # Receive the question
        data = s.recv(1024).decode().strip()
        print(f"[DEBUG] Question: {data}")


        # Check if the received data is a question
        if "what is" in data:
            # Extract the numbers from the question
            parts = data.split()
            try:
                a = int(parts[-4])
                b = int(parts[-2])
            except ValueError:
                print("Failed to parse numbers from the question.")
                print(parts)
                all_correct = False
                break

            # Calculate the correct answer
            sum = a + b

            print(f"ANSWERING: {sum}")
            s.sendall(f"{sum}\n".encode())

            # Handle the "calculating" message and delay
            response = s.recv(18).decode().strip()
            #print(f"[DEBUG]: {response} [DEBUG_END]")
            print(response)
            print()



            if "You made my little brother cry" in response:
                print("Incorrect answer. Exiting.")
                all_correct = False
                break
        else:
            print("Unexpected response from server.")
            all_correct = False
            break

    if all_correct:
        # Fetch and print the flag
        flag = s.recv(1024).decode().strip()
        print("Flag:", flag)

print("All questions answered correctly!")
