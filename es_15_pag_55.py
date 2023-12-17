def main():
    nome = input("Inserisci il tuo nome: ")
    if len(nome) > 0:
        maschera_nome = nome[0] + '*' * (len(nome) - 1)
        print(f"Il tuo nome mascherato è: {maschera_nome}")
    else:
        print("Inserisci almeno un carattere nel nome.")
if __name__ == "__main__":
    main()
