def main():
    numero1 = float(input("Inserisci il primo numero: "))
    numero2 = float(input("Inserisci il secondo numero: "))
    somma_quadrati = numero1**2 + numero2**2
    quadrato_somma = (numero1 + numero2)**2
    differenza_quadrati = numero1**2 - numero2**2
    quadrato_differenza = (numero1 - numero2)**2
    risultati = [somma_quadrati, quadrato_somma, differenza_quadrati, quadrato_differenza]
    print(f"Risultati: {risultati}")
if __name__ == "__main__":
    main()