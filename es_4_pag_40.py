def main():
    numero = 1
    for i in range(0, 200):
        quadrato = numero ** 2
        if (quadrato < 200):
            print(f"{numero}")
            numero += 1
        else:
            i = 200
if __name__ == "__main__":
    main()