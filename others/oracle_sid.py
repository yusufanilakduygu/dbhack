import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('192.200.11.9', 1521))
print('Connection Result  >> ' , result)
 

send_msg= bytearray ([0x00,0xa8, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 
0x01, 0x34, 0x01, 0x2c, 0x00, 0x00, 0x08, 0x00, 
0x7f, 0xff, 0x4f, 0x98, 0x00, 0x00, 0x00, 0x01, 
0x00, 0x86, 0x00, 0x22, 0x00, 0x00, 0x00, 0x00, 
0x01, 0x01, 0x28, 0x44, 0x45, 0x53, 0x43, 0x52, 
0x49, 0x50, 0x54, 0x49, 0x4f, 0x4e, 0x3d, 0x28, 
0x43, 0x4f, 0x4e, 0x4e, 0x45, 0x43, 0x54, 0x5f, 
0x44, 0x41, 0x54, 0x41, 0x3d, 0x28, 0x53, 0x49, 
0x44, 0x3d, 

0x4f, 0x45, 0x4d, 0x52, 0x45, 0x50, 

0x0d, 0x29, 0x28, 0x43, 0x49, 0x44, 0x3d, 0x28, 0x50, 0x52,
0x4f, 0x47, 0x52, 0x41, 0x4d, 0x3d, 0x29, 0x28, 
0x48, 0x4f, 0x53, 0x54, 0x3d, 0x5f, 0x5f, 0x6a, 
0x64, 0x62, 0x63, 0x5f, 0x5f, 0x29, 0x28, 0x55, 
0x53, 0x45, 0x52, 0x3d, 0x29, 0x29, 0x29, 0x28,
0x41, 0x44, 0x44, 0x52, 0x45, 0x53, 0x53, 0x3d, 
0x28, 0x50, 0x52, 0x4f, 0x54, 0x4f, 0x43, 0x4f, 
0x4c, 0x3d, 0x74, 0x63, 0x70, 0x29, 0x28, 0x48, 
0x4f, 0x53, 0x54, 0x3d, 0x31, 0x39, 0x32, 0x2e, 
0x32, 0x30, 0x30, 0x2e, 0x31, 0x31, 0x2e, 0x39, 
0x29, 0x28, 0x50, 0x4f, 0x52, 0x54, 0x3d, 0x31,
0x35, 0x32, 0x31, 0x29, 0x29, 0x29  ] )

sock.send(send_msg)
msg = sock.recv(2048)
sock.close()
print('FULL RETURNED MESSAGE')
print ('Received  >> ',msg )



