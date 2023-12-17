def main():
    a = int(input("Inserisci un numero: "))
    b = int(input("Inserisci un numero: "))
    if a < b:
        a, b = b, a#scambio di variabili
        #a, b = 5, 7 assegnamento multiplo
    print(f"Il numero maggiore è {a} e il minore è {b}")

if __name__ == "__main__":
    main()