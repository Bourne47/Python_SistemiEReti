# Crea la tavola pitagorica con una list comprehension
def   main():
    tavola_pitagorica = [[i * j for j in range(1, 11)] for i in range(1, 11)]
    #print(tavola_pitagorica)
    for k, tabellina in enumerate(tavola_pitagorica):
        #tabellina è una lista, tavola_pitagorica è una lista di liste
        #enumerate numera le liste e ritorna indice ed elemento
        print(f"Tabellina del {k+1}: {tabellina}")
    file = open("tavola_pitagorica.txt", "w")

    for tabellina in tavola_pitagorica:
        file.write(f"{tabellina}\n")

    file.close()

if __name__ == "__main__":
    main()
# Stampa la tavola pitagorica
#for riga in tavola_pitagorica:
    #print("\t".join(riga))

# Salva la tavola pitagorica su un file
#with open("tavola_pitagorica.txt", "w") as file:
    #for riga in tavola_pitagorica:
        #file.write("\t".join(riga) + "\n")

#print("Tavola pitagorica salvata su 'tavola_pitagorica.txt'.")