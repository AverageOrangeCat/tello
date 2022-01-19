#
#   project: tello_runtime.py
#   author: Noel Kueng
#

import sys
import socket
import select

local_address = ('0.0.0.0', 9000)
tello_address = ('192.168.10.1', 8889)

TMEOUT_MAX = 15.0

try:
    file_name = sys.argv[1]
except:
    print("Error: file_name parameter is required.")
    sys.exit(1)

try:
    file = open(file_name, "r")
except:
    print("Error: invalid file_name '" + file_name + "'.")
    sys.exit(1)
    
commands = file.readlines()

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(local_address)
    sock.setblocking(0)
except:
    print("Error: could not setup socket.")
    sys.exit(1)

print("Info: program is ready for execution.")

for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()
        sent = sock.sendto(command.encode(encoding="utf-8"), tello_address)
        
        print("Info: command '" + str(command.split("'")[0]) + "' has been sent.")
        
        ready = select.select([sock], [], [], TMEOUT_MAX)
        
        if ready[0]:
            try:
                data = sock.recv(1518)
            except:
                print("Error: something went wrong during the response time.")
                sys.exit(1)
        else:
            print("Error: timeout has been reached.")
            sys.exit(1)
                
        data = str(data.decode(encoding="utf-8").rstrip())
        
        if str(command).find("?") != -1:
            print("Info: response text '" + data + "'.")
        else:
            if data == "ok":
                print("Info: response text '" + data + "'.")
            else:
                print("Error: response error '" + data + "'.")
                sys.exit(1)
        
sock.close()
print("Info: program finished successfully.")
