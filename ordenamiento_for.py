#for for para entender el buble sort

def ordenar(numeros):
    n = len(numeros)
    for i in range(n):
        for j in range(n - i - 1):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
    print(numeros)

def main():
    entrada = [3, 5, 8, 9, 2, 7, 37]
    ordenar(entrada)

main() 