import ipaddress

def main():
    indirizzo = input("Inserisci l'indirizzo ipv4: ")
    subnet = input("Inserisci la subnet mask: ")
    indirizzo_ip_completo = indirizzo + '/' + subnet
    try:
        indirizzo_ip = ipaddress.IPv4Address(indirizzo)
    except ValueError:
        print("Indirizzo IP non valido.")
        return
    
    if indirizzo_ip.is_private:
        print(f"{indirizzo} è privato")
    if indirizzo_ip.is_loopback:
        print(f"{indirizzo} è loopback")
    if indirizzo_ip.is_reserved:
        print(f"{indirizzo} è riservato")
        return 0
    else:
        print(f"{indirizzo} è libero")
    iprete = ipaddress.IPv4Network(indirizzo_ip_completo, strict=False)
    if indirizzo_ip_completo == str(iprete):
        print(f"è di rete perché l'indirizzo {indirizzo_ip_completo} è uguale a {iprete}")
        hosts = list(ipaddress.IPv4Network(indirizzo + "/" + subnet).hosts())
    else:
        print(f"Non è di rete perché l'indirizzo {indirizzo_ip_completo} è diverso a {iprete}")
        hosts = list(ipaddress.IPv4Network(indirizzo + "/" + subnet, strict=False).hosts())
    print(f"Il primo indirizzo ip utilizzabile è: {hosts[0]}")
    print(f"L'ultimo indirizzo ip utilizzabile è: {hosts[-1]}")
    '''for host in hosts:
        print(host)'''

if __name__ == "__main__":
    main()
