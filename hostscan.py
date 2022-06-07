import sys
import socket
from datetime import datetime
import ipaddress
  
### TIMEOUT FOR TCP CONNECTION
timeout = 2
### TCP PORT
port = 22
### IP ADDRESSES
targets = """
172.18.100.1
172.18.100.2
172.18.100.3
172.18.100.4
172.18.100.5
172.18.100.6
172.18.100.7
172.18.100.8
172.18.100.9
"""
targetList = targets.splitlines()

print("-" * 50)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)
for target in targetList:
    target = target.strip()
    if not len(target):
        continue
    try:
        ip = ipaddress.ip_address(target)
    except ValueError:
        print(f'{target} is an invalid address!')
        continue    

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
           
        # returns an error indicator
        result = s.connect((target,port))
        print(f"{target}: Port {port} is OPEN!")
        s.close()
            
    except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()
    except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
    except socket.timeout:
            print(f"{target}: Port {port} is timed out")
    except socket.error:
            print(f"{target}: Port {port} is rejected")
