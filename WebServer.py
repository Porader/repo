import socket 
import os.path

socketS = socket.socket() 
socketS.bind(('localhost',8000))
socketS.listen(10)
print 'Listening socket. Please waiting...'

while True:
    connection, address  = socketS.accept()
    data = connection.recv(buffer_size)
    path = ''
    result = data.split('\n')[0].split(' ')[1]
    path = './' + result 
	
    if not os.path.isfile(path):
            path ='./index.html' 
            
    file = open(path, 'r')
    connection.send("""HTTP/1.1 200 OK\nContent-Type: text/html\n\n\n""" + file.read())
    file.close()
    connection.close()
socketS.close() 
