from netmiko import ConnectHandler
from credentials import *


# Establish SSH connection to device
def connect_to_device(ip: str):
    device = ConnectHandler(device_type="aruba_osswitch", ip=ip, username=username, password=password)
    return device


def get_arp_table(device) -> str:
    arp_result = device.send_command("show arp")
    return arp_result
