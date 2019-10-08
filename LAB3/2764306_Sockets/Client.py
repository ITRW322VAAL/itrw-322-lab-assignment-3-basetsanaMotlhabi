import socket

HOST='127.0.01'
PORT=9999

with socket.socket(Socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connesct((HOST,PORT))
	s.sendall(b'Hello,Sever')
	data=conn.recv(2048)
	print('Recieved',repr(data))