lista_voti = []
k = 0

while True:
    voto = int(input("Inserisci un voto: (-1 per interrompere dopo che hai inserito almeno 6 voti)"))
    if (voto < 0 and k >= 6):
        break
    lista_voti.append(voto)
    k += 1
print(lista_voti[1:-1])
lista_voti[3] = 10
print(lista_voti[0 : 3])
print(lista_voti[3])