def main():
    a = int(input("Inserisci un numero: "))
    c = 0
    if a % 2 == 0:
        print("è divisibile per 2")
        c = c + 1
    if a % 3 == 0:
        print("è divisibile per 3")
        c = c + 1
    if a % 5 == 0:
        print("è divisibile per 5")
        c = c + 1
    if c == 0:
        print("non è divisibile per due, tre e cinque")
if __name__ == "__main__":
    main()
