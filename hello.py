import socket

s = socket.socket()
s.bind(('', 8000))
s.listen(1)
print("Listening on port 8000...")

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)  # Receive request (not used here)
    conn.send(b"Hello, world!")  # Send simple response
    conn.close()
