
def get_ip_list() -> list:
    with open("ip_address_list.txt") as ip_file:
        ip_list = ip_file.read().splitlines()
    return ip_list

