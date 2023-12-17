class Quadrato():
    def __init__(self, lato):#costruttore
        self.lato = lato

    def calcolaArea(self):#obbligatorio passare self, possibilità di passare altri parametri
        return self.lato**2
    
    def calcolaPerimetro(self):#obbligatorio passare self, possibilità di passare altri parametri
        return abs(self.lato*4)
    
    def puntoInterno(self, x, y):
        if (x < self.lato and x > 0 and y < self.lato and y > 0):
            print("il punto è interno")
        else:
            print("Il punto è esterno")

def main():
    q = Quadrato(5)
    print(q.calcolaArea())
    print(q.calcolaPerimetro())
    q.puntoInterno(3, 4.9)

if __name__ == "__main__":
    main()
