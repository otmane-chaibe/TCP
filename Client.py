import sys
from socket import*
# Get the server hostname, port and data length as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]
count = argv[3]

# Command line argument is a string, change the port and data length into integer
port = int(port)
count = int(count)

# Initialize and print data to be sent
data = 'X' * count

# Create TCP client socket. Note the use of SOCK_STREAM for TCP packet
clientSocket= socket(AF_INET, SOCK_STREAM)

# Create TCP connection to server
print("Connecting to " + host + ", " + str(port))
clientSocket.connect((host, port))

# Send data through TCP connection
print("Sending data to server: " + data)
clientSocket.send(data.encode())

# Receive the server response
dataEcho= clientSocket.recv(count) 

# Display the server response as an output
print("Receive data from server: " + dataEcho.decode())

# Close the client socket
clientSocket.close()
