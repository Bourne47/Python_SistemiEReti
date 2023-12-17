def main():
    numero1 = float(input("Inserisci il primo numero: "))
    numero2 = float(input("Inserisci il secondo numero: "))
    risultati = {"Media aritmetica": (numero1 + numero2) / 2, "Media geometrica": (numero1 * numero2)**0.5}
    print(risultati)
if __name__ == "__main__":
    main()