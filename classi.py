class Quadrato():
    def __init__(self, lato):#costruttore
        self.lato = lato

    def calcolaArea(self):#obbligatorio passare self, possibilità di passare altri parametri
        return self.lato**2
    
    def stampaLato(self):
        print(f"Il lato è {self.lato}")
    
def main():
    q = Quadrato(4)#il nome della classe si irferisce al costruttore
    print(f"L'area del quadrato è {q.calcolaArea()}")
    q.stampaLato()
    print(q.lato)
    q.lato = 5
    q.stampaLato()
    print(q.lato)
    print(f"L'area del quadrato è {q.calcolaArea()}")

if __name__ == "__main__":
    main()