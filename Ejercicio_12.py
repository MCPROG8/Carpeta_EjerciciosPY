class Ejercicio_12:

    @staticmethod
    def calcular_salario_bruto(horas_laboradas, valor_hora):
        salario_bruto= horas_laboradas * valor_hora
        return salario_bruto

    @staticmethod
    def calcular_porcentaje_retencion(retencion):
        return retencion / 100

    @staticmethod
    def calcular_valor_retencion_fuente(porcentaje_retencion, salario_bruto):
        return porcentaje_retencion * salario_bruto

    @staticmethod
    def calcular_salario_neto(salario_bruto, valor_retencion_fuente):
        return salario_bruto - valor_retencion_fuente



if __name__ == "__main__":
    #Validación de horas
    while True:
        try:
             horas = float(input("¿Cuántas horas trabaja a la semana? \n"))
             break
        except ValueError:
            print("\nError,debe ser un número.\n")

    # Validación de valor de hora
    while True:
        try:
         valor_hora = float(input("¿Cuál es el valor de cada hora trabajada?\n "))
         break
        except ValueError:
            print("\nError,debe ser un número.\n")

    # Validación de retencion
    while True:
        try:
          retencion = float(input("¿De cuánto es la retención? \n "))
          break 
        except ValueError:
            print("\nError,debe ser un número.\n")

#Llamada al metodo

    salario_bruto = Ejercicio_12.calcular_salario_bruto(horas, valor_hora)
    porcentaje = Ejercicio_12.calcular_porcentaje_retencion(retencion)
    retencion_fuente = Ejercicio_12.calcular_valor_retencion_fuente(porcentaje, salario_bruto)
    salario_neto = Ejercicio_12.calcular_salario_neto(salario_bruto, retencion_fuente)

    print("\n--- DIAN ---\n")
    print(f"Salario Bruto: $ {salario_bruto:,.2f}")
    print(f"Retención en la fuente: $ {retencion_fuente:,.2f}")
    print(f"Salario Neto: $ {salario_neto:,.2f}\n")
