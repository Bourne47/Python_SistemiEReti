#list comprehension
#lista con i primi 5 quadrati perfetti
import random
quadrati = [i*i for i in range(1, 6)]#i * i con i tra 1 e 6 escluso
numeri_interi =[i for i in range(1, 11)]
stringhe = ["computer", "cellulare", "laptop"]
stringhe_c = [parola for parola in stringhe if parola[0] == "c"]
print(quadrati)
print(numeri_interi)
print(stringhe_c)
voti = [random.randint(2, 10) for _ in range(10)]#underscore per utilizzare variabili delle quali non necessitiamo il valore
print(voti)
voti_insufficienti = [voto for voto in voti if voto < 6]
print(voti_insufficienti)