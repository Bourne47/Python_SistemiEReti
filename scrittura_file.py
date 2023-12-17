def ricerca(dizionario):
    c = -1
    numeri = "0123456789"
    a = input("Inserisci il nome o il numero che vuoi cercare: ")
    if (a[0] in numeri):
        #print("numero")
        for x in dizionario:
            if(x == int(a)):
                print(dizionario[x])
                c = 0
    else:
        #print("lettera")
        for x in dizionario:
            if (dizionario[x] == a):
                print(x)
                c = 0
    if (c == -1):
        print("Nome o numero non trovato")

def main():
    dizionario = {}
    file = open("rubrica.txt", "r")
    for x in file:
        diz = x.split(", ")
        diz[1] = int(diz[1].replace("\n", ""))
        dizionario[diz[1]] = diz[0]
    print(dizionario)
    file.close()
    ricerca(dizionario)

if __name__ == "__main__":
    main()