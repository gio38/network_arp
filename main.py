from utils import get_ip_list
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

dc01_arp_ip_list = list()
dc02_arp_ip_list = list()

# d = ConnectHandler()

try:
    ip_list = get_ip_list()

    for ip in ip_list:
        device = ConnectHandler(device_type="aruba_osswitch", ip=ip, username=username, password=password)
        d = device
        arp_result = device.send_command("show arp")

        edit_arp_result = arp_result.splitlines()

        print(edit_arp_result)
        print("\n\n")

        pp(edit_arp_result)

        # for i in edit_arp_result[5:-1]:
        #     a = i.split()
        #     # print(a[0])
        #     arp_ip_list.append(a[0])

        device.disconnect()

finally:

    print('pass \n ---------------------------- \n')
    # print(sorted(arp_ip_list))
    # d.disconnect()





