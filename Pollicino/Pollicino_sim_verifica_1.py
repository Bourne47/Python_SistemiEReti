import random
numeri = [-1, 1]
def movimento():
    return random.choice(numeri)
def main():
    spostamento = 0
    spost = [movimento() for _ in range(0, 432000)]
    for num in spost:
        spostamento += num
    print(spostamento)
if __name__ == "__main__":
    main()