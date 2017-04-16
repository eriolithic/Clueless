import socket
import sys
import errno
from thread import *

def threaded_client(conn, addr):
    conn.send('Welcome, type your info\n')

    while True:
        try:
            data = conn.recv(4096)
            reply = 'Server: '+ data
            if not data:
                print 'Connection closed'
                break
            conn.sendall(reply)
            print('Request from ' + str(addr[0]) + ':' + str(addr[1]) + ':' + data)
        except socket.error as e:
            if e.errno == errno.WSAECONNRESET:
                print 'A player has left'
                quit()
        
    
    print('Connection closing')
    conn.close()
    
#main function
if __name__ == "__main__":

    host = ''
    port = 5555
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((host, port))
    except socket.error as e:
        print(str(e))

    s.listen(5)
    print('Waiting for a connection.')


    while True:

        conn, addr = s.accept()
        print('connected to: '+addr[0]+':'+str(addr[1]))

        start_new_thread(threaded_client,(conn,addr,))
            