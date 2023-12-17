def main():
    a = int(input("Inserisci un numero cdr: "))
    if (a > 30 or a < 1):
        print("deve essere maggiore di 0 e minore di 31")
    else: 
        subnet = ("1"*a+("0"*(32-a)))
        print(subnet)
        group1 = subnet[:8]
        group2 = subnet[8: 16]
        group3 = subnet[16:24]
        group4 = subnet[24:]
        group1 = int(group1, 2)
        group2 = int(group2, 2)
        group3 = int(group3, 2)
        group4 = int(group4, 2)
        subnet_string = f"{group1}.{group2}.{group3}.{group4}"
        print(subnet_string)

if __name__ == "__main__":
    main()
    