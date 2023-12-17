class Robot():
    def __init__(self, nome, massa, tipologia):
        self.nome = nome
        self.massa = massa
        self.tipologia = tipologia
    def stampaNome(self):
        print(f"Il nome del robot è {self.nome}")
    def pericolosità(self):
        return (self.massa > 100 and self.tipologia == "umanoide")

def main():
    robot = Robot("Mario", 1000, "umanoide")
    robot.stampaNome()
    if robot.pericolosità():
        print(f"{robot.nome} è un robot {robot.tipologia}, è pericoloso perché pesa {robot.massa}")
    else:
        print(f"{robot.nome} è un robot {robot.tipologia}, non è pericoloso")

if __name__ == "__main__":
    main()