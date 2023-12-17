import random
def calcolaSpostamenti(sec=432000, lista=[1, -1]):#parametri con valore di default
    spostamento = 0
    spost = [random.choice(lista) for _ in range(0, sec)]
    for num in spost:
        spostamento += num
    print(spostamento)
def main():
    #calcolaSpostamenti(lista=[2,-2])
    calcolaSpostamenti(1000, [3,-3])#passaggio di parametri con valore di default
if __name__ == "__main__":
    main()