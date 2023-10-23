import math
def main():
    #a = [i*i for i in range(int(math.sqrt(200))+1) if i*i % 2 == 1]
    a = [i*i for i in range(1000) if i*i < 200 and (i*i % 2 == 1) and (i*i < 200)]
    print(a)

if __name__ == "__main__":
    main()