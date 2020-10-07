from datetime import datetime
import os
import socket
import subprocess
import sys

cmdLineClear = 'clear'
if os.name == 'nt':
  cmdLineClear = 'cls'

subprocess.call(cmdLineClear, shell=True)


# Ask which host to scan
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print some decoration
print('-' * 60)
print("Please wait, scanning remote host", remoteServerIP)
print('-' * 60)

t1 = datetime.now

try:
  for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("{}..".format(port), end='')
    result = sock.connect_ex((remoteServerIP, port))
    if result == 0:
      print("")
      print("Port {}: Open".format(port))
    
    sock.close

except KeyboardInterrupt:
  print("Cancelled.")
  sys.exit()

except socket.gaierror:
  print("Error: Hostname could not be resolved.")
  sys.exit()

except socket.error:
  print("Error: Couldn't connect to server.")
  sys.exit()

t2 = datetime.now
total = t2 - t1
print("Scanning completed in: ", total)
