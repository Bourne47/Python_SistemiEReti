def completa8bin(strbin):
    l = len(strbin)
    strbin = "0"*(8-l)+strbin
    return strbin

def main():
    #address = "10.172.14.4"
    address = (input("Inserisci l'indirizzo ip dividendo gli ottetti con dei punti: (xxx.xxx.xxx.xxx)"))
    subnet = int(input("Inserisci la subnet mask in notazione CIDR: (da 0 a 30)"))
    groups = address.split('.')
    groups = [int(group) for group in groups]
    print(groups)
    groups_bin = [bin(group) for group in groups]
    print(groups)
    groups_bin = [str(group) for group in groups_bin]
    groups_bin = [group[2:] for group in groups_bin]
    #groups_bin = [int(group) for group in groups_bin]
    print(groups_bin)
    #print(completa8bin(groups_bin[0]))
    #format(45, '08b') converte l'inteero in binario usando 8 bit e riempendo se necessario con degli 0
    groups_strbin = [completa8bin(group) for group in groups_bin]
    print(groups_strbin)
    groups_bin = [str(group) for group in groups_strbin]
    print(".".join(groups_strbin))
    print(groups_bin)
    groups_bin_str = ".".join(groups_bin)
    print(groups_bin_str)
    cont = 0
    ip_rete = ""
    ip_broadcast = ""
    print(subnet)
    for group in groups_bin:
        for i in range(0, 9):
            #if (groups_bin_str[cont] != "."):
            if (cont < subnet + 3):
                ip_rete = str(ip_rete)+groups_bin_str[cont]
                ip_broadcast = str(ip_broadcast)+groups_bin_str[cont]
            else:
                ip_rete = ip_rete+"0"
                ip_broadcast = ip_broadcast+"1"
            cont += 1
            #ip_rete = ip_rete+"."
            #ip_broadcast = ip_broadcast+"."
        
    ip_rete = ip_rete.split('.')
    ip_broadcast = ip_broadcast.split('.')
    print(ip_broadcast)
    print(ip_rete)

    print(ip_rete)
    print(ip_broadcast)
if __name__ == "__main__":
    main()