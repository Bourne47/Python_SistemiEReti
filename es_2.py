a = float(input("Inserisci un numero: "))
print(f"Il tipo di a è {type(a)}")

if a > 5:
    print("a è maggiore di 5")
elif (a <= 5) and (a >= 0):
    print("a è maggiore o uguale a zero è minore o uguale a 5")
else:
    print("a è minore di zero")