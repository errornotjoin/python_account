import socket
import ssl

user_host = socket.gethostbyname(socket.gethostname())
list_of_allowed_commands = ["Check if server is running", "Check Minecraft Server", "EXIT"]
s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
print("Server is starting...")
s.bind((user_host, 7777))
s.listen(5)

print("Server is listening...")

print("Server setup complete.")
for command in list_of_allowed_commands:
    print(f"Allowed command: {command}")
user = input("Press Enter to send command to the server: ")

if user in list_of_allowed_commands:
    print(f"Sending command: {user}")
else:
    print("Invalid command.")

while True:
    conn, addr = s.accept()
    with conn:
        print(conn.recv(1024).decode())
        conn.send(f"Command received: {user}".encode())

s.close()
