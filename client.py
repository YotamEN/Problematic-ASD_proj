import socket
import time
import struct
from cli import CommandLineInterface

cli = CommandLineInterface()

@cli.command
def upload(address, user, thought):
    try:
    #create socket
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(ip_port_extract(address))
        #encode data by given protocol
        thought_size = len(thought)
        curr_time = int(time.time())
        data_packet = struct.pack(f'<QQi{thought_size}s', int(user), curr_time, thought_size, thought.encode())
        conn.sendall(data_packet)
        print('done')
    except Exception as e:
        print(f'Error: {e!r}')
    
    
    
def ip_port_extract(address):
    i = 0
    while address[i] != ':':
        i += 1
    ip = address[:i]
    port = int(address[i+1:])
    return(ip, port)



if __name__ == '__main__':
    cli.main()
    
