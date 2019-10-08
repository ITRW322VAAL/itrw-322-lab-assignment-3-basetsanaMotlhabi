import socket

HOST='127.0.01'
PORT=9999

with socket.socket(Socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen()
	conn,addr=s.accept()
	with conn:
		print('Server is connected with a address',addr)
		while True:
			data=conn.recv(2048)
			if not data:
				break
			conn.sendall(data)
© 2019 GitHub, Inc.