def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    if len(pila) == 0:
        x = None
    else:
        x = pila.pop()
    return x

def main():
    parentesi_aperte = ['{', '[', '(']
    parentesi_chiuse = ['}', ']', ')']
    apertura_parentesi = []
    apertura_parentesi_posizione = []
    dizionario = {'{': '}', '[': ']', '(': ')'}
    stringa = "{(1+[2+3]*5}"
    errore = False
    pila = []
    cont = -1
    for carattere in stringa:
        cont += 1
        if carattere in parentesi_aperte:
            parentesi = pop(pila)
            if parentesi == carattere:
                errore = True
                posizione_errore = cont
            else:
                push(pila, parentesi)
                push(pila, carattere)
                apertura_parentesi.append(carattere)
                apertura_parentesi_posizione.append(cont)
        if carattere in parentesi_chiuse:
            parentesi = pop(pila)
            if parentesi != None:
                if dizionario[parentesi] != carattere:
                    errore = True
                    posizione_errore = cont
                    break
                else:
                    apertura_parentesi.pop()
                    apertura_parentesi_posizione.pop()
            else:
                errore = True
                posizione_errore = cont
                break
    print(pila)
    if len(pila) > 1 and pila[1] != None:
        #print(len(pila))
        errore = True
        posizione_errore = apertura_parentesi_posizione[-1]   
    if errore:
        print(f"Errore nella posizione: {posizione_errore}")
        #print("Errore")
    else:
        print("Corretto")

if __name__ == "__main__":
    main()