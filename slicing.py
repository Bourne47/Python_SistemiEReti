# SLICING DI STRINGHE
s = "ciao come stai?"# c = 0 || c = -4 i = 1 || i = -3 ecc
print(s[0])
print(s[-1])
print(s[-2])
print(s[len(s)-1])#c -style da non usare

print(s[3:7]) #dal carattere 3 al 7 escluso
print(s[1:-1]) #esclude il primo e l'ultimo carattere
print(s[1:])#fino in fondo escludendo il primo
print(s[0:-1]) #fino all'ultimo carattere partendo dall'inizio
print(s[::-1])