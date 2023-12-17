import turtle

class CodiceABarre:
    def __init__(self, stringa):
        self.stringa = stringa

    def codice_barre(self):
        turtle.penup()
        turtle.speed(100)
        turtle.color("black")
        turtle.pensize(4)
        turtle.goto(-200, 0)
        turtle.pendown()

        for carattere in self.stringa:
            bin_car = format(ord(carattere), '08b')
            for bit in bin_car:
                if bit == '1':
                    self.riga_nera()
                else:
                    self.riga_bianca()
        turtle.hideturtle()
        turtle.done()

    def riga_nera(self):
        turtle.seth(90)
        turtle.forward(100)
        turtle.penup()
        turtle.seth(270)
        turtle.forward(100)
        turtle.seth(0)
        turtle.forward(5)
        turtle.pendown()

    def riga_bianca(self):
        turtle.seth(0)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

def main():
    stringa = input("Inserisci la stringa lunga 8 caratteri: ")
    if len(stringa) != 8:
        print("La stringa deve essere lunga 8 caratteri.")
        return
    for carattere in stringa:
        if ord(carattere) > 255:
            print("Caratteri sbagliati. Assicurati che ogni carattere abbia un codice ASCII inferiore a 255.")
            return
    codice_a_barre = CodiceABarre(stringa)
    codice_a_barre.codice_barre()

if __name__ == "__main__":
    main()
