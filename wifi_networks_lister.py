import subprocess, platform
import sys
import platform

os_name = platform.system()
if os_name == 'Windows':
    list_networks_command = 'netsh wlan show networks'
    output = subprocess.check_output(list_networks_command, shell=True, text=True)
    print(output)
else:
    print("This script currently supports only Windows OS.")

