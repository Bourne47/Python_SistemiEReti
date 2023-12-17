#il dizionario è una collezione di coppie chiave:valore
#il dizionario non ha indici, ma si indicizza per chiave che deve essere univoca e di un solo tipo per tutto il dizionario

dizionario = {"nome": "Mario", "cognome": "Rossi"}
#lista = ["Mario", "Rossi"]
print(dizionario)
print(dizionario["cognome"])
print(dizionario["nome"])

#aggiunge due elementi nuovi
dizionario["data nascita"] = "01/01/1900"
dizionario["età"] = 123
print(dizionario)

#sovrascrivere l'elemento con chiave "nome"
dizionario["nome"] = "Luca"
print(dizionario)

#ciclo for su dizionario 1
for chiave in dizionario:
    print(f"Chiave: {chiave} - valore : {dizionario[chiave]}")

rubrica_telefonica = {38189192: "Mario Rossi", 348039013:"Alice Verdi", 32193991: "Luca Gialli"}