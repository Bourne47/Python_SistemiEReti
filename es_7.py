import turtle

lati = int(input("Inserisci il numero di lati: "))
lung = int(input("Inserisci la lunghezza del lato: "))
angolo = 360 / lati
finestra = turtle.Screen()
alice = turtle.Turtle()
alice.color('red', 'green')
alice.begin_fill()
for i in range(0, lati):
    alice.forward(lung)
    alice.left(angolo)
alice.end_fill()

finestra.mainloop()