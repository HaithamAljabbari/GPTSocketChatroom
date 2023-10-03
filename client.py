import socket
import threading

# Define the server address and port
SERVER_HOST = '127.0.0.1'  # Change this to the server's IP address
SERVER_PORT = 12345  # Change this to the server's port number

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f"Connected to {SERVER_HOST}:{SERVER_PORT}")

# Function to send messages to the server
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Function to receive messages from the server
def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # Handle exceptions if the connection is lost
            print("Disconnected from the server.")
            client_socket.close()
            break

# Start separate threads for sending and receiving messages
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()
