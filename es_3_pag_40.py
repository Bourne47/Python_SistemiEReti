def main():
    operazione = int(input("Inserisci il tipo di operazione che vuoi fare (0: somma, 1: sottrazione, 2: moltiplicazione, 3: divisione): "))
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    if operazione == 0:
        print(f"{a+b}")
    elif operazione == 1:
        print(f"{a-b}")
    elif operazione == 2:
        if a != 0 and b != 0:
            print(f"{a*b}")
    elif operazione == 3:
        if a != 0 and b != 0:
            print(f"{a/b}")
if __name__ == "__main__":
    main()