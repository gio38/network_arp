
def get_ip_list() -> list:
    with open("ip_address_list.txt") as ip_file:
        ip_list = ip_file.read().splitlines()
    return ip_list


def get_ip_from_arp_table(edit_arp_result: list) -> list:
    ip_list: list = []
    for i in edit_arp_result[5:-3]:
        a = i.split()
        # print(a[0])
        # print("------------- DC 01 ----------------")
        ip_list.append(a[0])

    return ip_list
