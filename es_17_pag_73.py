import math
def main():
    a = int(input("Inserisci un numero: "))
    esponente = int(math.log2(a))
    x = [2**i for i in range(esponente + 1) if 2**i <= a]
    print(x)

if __name__ == "__main__":
    main()