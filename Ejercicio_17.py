import math 

class Ejercicio_17:
    @staticmethod
    def calcular_area(radio):
        area=math.pow(radio,2) *math.pi
        return area
    
    @staticmethod
    def calcular_longitud_circulo(radio):
        longitud=2 *math.pi *radio
        return longitud
    

# Llamada al método 
if __name__ == "__main__":
    while True:
        try:
             radio = float(input("Ingresa el radio del círculo:\n"))
             if radio <= 0:
                  print("\nPor favor,ingresa un número mayor que 0.\n")
             else:
                  area = Ejercicio_17.calcular_area(radio)
                  longitud = Ejercicio_17.calcular_longitud_circulo(radio)

                  print(f"\nEl área es: {round(area,2)}")
                  print(f"La longitud del círculo es: {round(longitud,2)}")
                  break
        except ValueError:
             print("\nPor favor,ingresa un número válido.\n")