ip_addresses = ["192.168.222.0/27", "192.168.100.0/24", "192.168.200.0/28", "192.168.50.0/22"]
file = open("mask.txt", "w")
for ip_address in ip_addresses:
    ip, subnet_mask = ip_address.split("/")
    subnet_mask_int = int(subnet_mask)
    sm = ""
    for _ in range(subnet_mask_int):
        sm = sm + '1'
    for _ in range(32 - subnet_mask_int):
        sm = sm + '0'
    sm = [sm[:8] + '.' + sm[8:16] + '.' + sm[16:24] + '.' + sm[24:]]
    file.write(f"{ip} - Subnet Mask({subnet_mask}): {sm}\n")
file.close()
print(sm)