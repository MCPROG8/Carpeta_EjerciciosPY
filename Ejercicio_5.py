import math  

class Ejercicio_5:
    @staticmethod
    def calcular_suma(suma,x):
        suma = suma + x
        return suma
    
    @staticmethod
    def calcular_X(x,y):
         x = x + math.pow(y, 2)  
         return x
    
    @staticmethod
    def calcular_SumaFinal(suma,x,y):
         suma = suma + x / y
         return suma

# Bloque principal
if __name__ == "__main__":

    # Validación de Suma
    while True:
        try:
            suma = int(input("Ingresa el número de suma:\n"))
            break
        except ValueError:
            print("\nError, Suma debe ser un número entero.\n")

    # Validación de X
    while True:
        try:
            x = int(input("\nIngresa el número de X:\n"))
            break
        except ValueError:
            print("\nError, X debe ser un número entero.\n")

    # Validación de Y
    while True:
        try:
            y = int(input("\nIngresa el número de Y:\n"))
            if y == 0:
                print("\nNo es posible dividir sobre 0. Ingresa otro número.\n")
            else:
                break 
        except ValueError:
            print("\nError, Y debe ser un número entero.")

    # Llamada al método 
    suma = Ejercicio_5.calcular_suma(suma, x)
    x = Ejercicio_5.calcular_X(x, y)
    Resultado = Ejercicio_5.calcular_SumaFinal(suma, x, y)

    print(f"\nEl resultado es: {round(Resultado,2)}")
