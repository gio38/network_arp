from utils import get_ip_list
from utils import get_ip_from_arp_table
from netmiko import ConnectHandler
from credentials import *
from pprint import pprint as pp

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

dc01_arp_ip_list: list = list()
dc02_arp_ip_list: list = list()
same_ip: list = list()
ip_dc01_not_dc02: list = list()
ip_dc02_not_dc01: list = list()
# d = ConnectHandler()

try:
    ip_list = get_ip_list()

    for ip in ip_list:
        device = ConnectHandler(device_type="aruba_osswitch", ip=ip, username=username, password=password)

        arp_result = device.send_command("show arp")

        edit_arp_result: list = arp_result.splitlines()

        if len(dc01_arp_ip_list) == 0:
            print(f"------------------ Connected to DC 01 ip: {ip} ------------------")
            dc01_arp_ip_list = get_ip_from_arp_table(edit_arp_result)
        else:
            print(f"------------------ Connected to DC 02 ip: {ip} -------------------")
            dc02_arp_ip_list = get_ip_from_arp_table(edit_arp_result)

        print("------------------------ Disconnect -------------------------")
        device.disconnect()
finally:

    pp(sorted(dc01_arp_ip_list))
    print('\n ---------------------------- \n')
    pp(sorted(dc02_arp_ip_list))

    for ip in dc01_arp_ip_list:
        if ip in dc02_arp_ip_list:
            if ip not in same_ip:
                same_ip.append(ip)

    for ip in dc01_arp_ip_list:
        if ip not in dc02_arp_ip_list:
            ip_dc01_not_dc02.append(ip)

    for ip in dc02_arp_ip_list:
        if ip not in dc01_arp_ip_list:
            ip_dc02_not_dc01.append(ip)

    print("\n --------- SAME IP's ----------")
    pp(sorted(same_ip))

    print("\n --------- IP's in DC 01 not in  DC 02 --------")
    pp(sorted(ip_dc01_not_dc02))

    print("\n -------- IP's in DC 02 not in DC 01 ---------")
    pp(sorted(ip_dc02_not_dc01))

    # d.disconnect()





