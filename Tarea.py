import csv

def hist():
    numero = 0
    frase = input("Ingrese 5 oraciones del Lorem Ipsum. No debe exceder 700 palabras\n>")

    limpio=''

    for i in frase:  
        if i!="." and i!="," and i!=" ":  
            limpio+=i

    limpio.lower()

    mapa = {}

    for letras in limpio:
        if letras in mapa:
            mapa[letras] += 1
        else:
            mapa[letras] = 1
        
    while numero <= 5:
        for valor in sorted(mapa):
            print(f'{valor}: {"*" * mapa[valor]}')
            numero += 1
    return True


def pali():
    lista = []
    soy = True
    n = 1

    with open('datos.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            lista.append(row)

    for j in lista:
        if n%2 == 0:
            for i in range(int(n/2)):  
                if lista[i]!=lista[n-i-1]:  
                    soy=False  
        else:   
            for i in range(int((n-1)/2)):  
                if lista[i]!=lista[n-i-1]:  
                    soy=False  

        if soy:
            print("Palindromo")
        else:
            print("No Palindromo")

    return True
