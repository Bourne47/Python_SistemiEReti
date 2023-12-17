def main():
    ip_addresses = ["192.168.222.0/27", "192.168.100.0/24", "192.168.200.0/28", "192.168.50.0/22"]
    with open("mask.txt", "w") as file:
        for ip_address in ip_addresses:
            ip, subnet_mask = ip_address.split("/")
            subnet_mask_int = int(subnet_mask)#costruttore di interi
            subnet_mask_bin = '1'*subnet_mask_int+'0'*(32-subnet_mask_int)
            #subnet_mask_bin = subnet_mask_bin[:8] + '.' + subnet_mask_bin[8:16] + '.' + subnet_mask_bin[16:24] + '.' + subnet_mask_bin[24:]
            subnet_mask_bin ='.'.join([subnet_mask_bin[i:i+8] for i in range(0,32,8)])
            file.write(f"{ip} - Subnet Mask({subnet_mask}): {subnet_mask_bin}\n")

if __name__ == "__main__":
    main()