import math 

class Ejercicio_14:
    @staticmethod

    #Calculo del cuadrado de un número
    def calcular_cuadrado(numero):
        cuadrado_numero = math.pow(numero, 2)
        return cuadrado_numero
    
    @staticmethod

    #Calculo del cubo de un número
    def calcular_cubo(numero):
        cubo_numero = math.pow(numero, 3)
        return cubo_numero

#Bloque principal
if __name__ == "__main__":
    #Condicionales y bucles para una respuesta esperada
    while True:
        try:
            numero = float(input("Ingresa un número:\n"))

            if numero > 0:
                cuadrado = Ejercicio_14.calcular_cuadrado(numero)
                cubo = Ejercicio_14.calcular_cubo(numero)

                print(f"\nEl cuadrado del número es: {cuadrado}")
                print(f"El cubo del número es: {cubo}")
                break
            else:
                print("El número debe ser mayor que 0\n")

        except ValueError:
            print("\nPor favor, ingrese un número válido\n")