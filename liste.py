def print_list(l):
    print("La lista è:", end="")
    for elemento in l:
        print(elemento, end=" ")
    print('\n')

def main():
    #le liste
    #l = [1, 2, 3, 4, "c", 3.14, "python"]#non è detto che sono in locazioni di memoria vicine
    #r = [10, 11, 12]
    #print(l)
    #print(l[-1])
    #print(l[::-1])
    #print_list(l+r)#concatena le liste
    #print_list(3*r)#stampa 3 volte r concatenazione multipla

    #vogliamo permetter all'utente di caricare una lista
    lista = []
    num = 1
    while num > 0:
        num = int(input("Scrivi un numero: (-1 per interrompere): "))
        if num > 0:
            lista.append(num)
    print_list(lista)

if __name__=="__main__":
    main()