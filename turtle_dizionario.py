import turtle
def nord(alice, movimento):
    alice.seth(90)
    alice.forward(movimento)

def est(alice, movimento):
    alice.seth(0)
    alice.forward(movimento)

def sud(alice, movimento):
    alice.seth(270)
    alice.forward(movimento)

def ovest(alice, movimento):
    alice.seth(180)
    alice.forward(movimento)



def main():
    finestra = turtle.Screen()
    alice = turtle.Turtle()
    direzioni = {"n": nord, "e":est, "s":sud, "o":ovest}
    while True:
        operazione = input("n nord, e est, s sud, o ovest: ")
        if operazione in direzioni:
            movimento = int(input("Inserisci la lunghezza del movimento: "))
            direzioni[operazione](alice, movimento)
        else:
            break



if __name__ == "__main__":
    main()