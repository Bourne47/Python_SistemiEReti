def main(): #definizione della funzione main    
    # questo è un commento
    #tab uguale a 4 spazi, indentazione neccessaria
    nome = input("Come ti chiami? ")
    anni = int(input("Quanti anni hai? "))
    anno_corrente = int(input("In quale anno siamo? "))
    print(f"Ciao {nome} e hai {anni} anni.") #f-string
    print(f"Sei nato nel {anno_corrente - anni}")
    print(type(anni))#stampa tipo variabile

if __name__ == "__main__":
    main()