import turtle

punte = int(input("Inserisci il numero di punte: "))
lung = 80
finestra = turtle.Screen()
alice = turtle.Turtle()
alice.color('red')
angolo = 180/punte
for z in range (0, punte):
    alice.forward(lung)
    alice.left(180-angolo)

finestra.mainloop()