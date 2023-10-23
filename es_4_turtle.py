#turtle che può andare avanti di 100, può girarsi a destra o a sinistra di 90 gradi (F, R, L)
import turtle
def print_list(l):
    print("La lista è:", end="")
    for elemento in l:
        print(elemento, end=" ")
    print('\n')

def main():
    lista = []
    comandiPossibili = ['F', 'R', 'L']
    num = 'F'
    while num in comandiPossibili:
        num = input("Scrivi un comando: (F avanti, R rotazione destra, L rotazione sinistra, -1 per interrompere): ")
        if num in comandiPossibili:
            lista.append(num)
    #print_list(lista)
    finestra = turtle.Screen()
    tartaruga = turtle.Turtle()
    tartaruga.shape('turtle')
    tartaruga.color('red')
    tartaruga.speed('slow')
    for comando in lista:
        if comando == 'F':
            tartaruga.forward(100)
        if comando == 'L':
            tartaruga.left(90)
        if comando == 'R':
            tartaruga.right(90)
    finestra.mainloop()
if __name__=="__main__":
    main()