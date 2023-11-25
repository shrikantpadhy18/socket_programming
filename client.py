import socket
import time

TCP_IP = '15.207.253.199'
#TCP_IP = 'localhost'
TCP_PORT = 14011
#UDP_PORT = 10019


UDP_IP ='15.207.253.199'
UDP_PORT = 10019

BUFFER_SIZE = 1024
MESSAGE = "1^*^fouser1^*^64^5^ 25-08-2022~13:16:31~Intraday Calls$N-17|fouser1~Q~7078122~hilll^6"

#for udp packets
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((UDP_IP, UDP_PORT))



#for tcp packets
TCP_IP ='15.207.253.199'
TCP_PORT = 14026
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


#s.connect((UDP_IP, UDP_PORT))

#MESSAGE = "1^*^SYS^*^198^5^141220220000001 14-12-2022~14:21:11~Intraday Calls$N-18|10-Nov-2021~14-Dec-2022~150~~NIFTY NAKED~NFO~F~I~NIFTY ~27-Jan-2022~E~*~0~B~1720000~0~0~0~0~0~0~1760000~0~1700000~99999999900~12519200~1~D~^6"

#msg = bytes(MESSAGE, 'utf-8')
#s.send(msg)

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
count = 0
start = time.time()
#for _ in range(20000):
msg = bytes(MESSAGE, 'utf-8')
s.send(msg)
#time.sleep(1)
count+=1
end = time.time()
print("total time:",end - start)
s.close()

#print("Total sent:",count)
