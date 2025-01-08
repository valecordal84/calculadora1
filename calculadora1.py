def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2 

operaciones = {
    "+":suma,
    "-":resta,
    "*":multiplicacion,
    "/":division,
}

repeticion = True
num1 = float(input("Cual es el primer número?: "))

while repeticion:
    for simbolo in operaciones:
        print (simbolo)
    operacion= input("Que operación quieres hacer?: ")
    num2 = float(input("Cual es el segundo número?: "))
    respuesta = operaciones[operacion](num1,num2)
    print(f"{num1}{operacion}{num2} = {respuesta}")

    eleccion = input (f"Escribe 'c' para continuar los calculos con {respuesta}, o escribe 'n' para comenzar de nuevo")

    if eleccion == "c":
        num1 = respuesta
    else:
        repeticion = False
        print("\n" * 50) 
    