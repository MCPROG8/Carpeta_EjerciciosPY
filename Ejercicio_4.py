class Ejercicioo_4:

    #Edad para Alberto
    @staticmethod
    def Calcular_edad_alberto(Edad_juan):
        Edad_alberto = int((2/3) * Edad_juan) 
        return Edad_alberto
    
    #Edad para Ana
    @staticmethod
    def Calcular_edad_ana(Edad_juan):
        Edad_ana = int((4/3) * Edad_juan)
        return Edad_ana
    
    #Edad para Mamá
    @staticmethod
    def Calcular_edad_mama(Edad_alberto, Edad_ana, Edad_juan):
        Edad_mama = Edad_alberto + Edad_ana + Edad_juan
        return Edad_mama
    


# Bloque principal
if __name__ == "__main__":
    while True:
        # Edad para Juan
        try:
            Edad_juan = int(input("Ingrese la edad de Juan:\n"))
            break
        except ValueError:
            print("La edad debe ser un número entero. Intenta de nuevo.\n")

    Edad_alberto = Ejercicioo_4.Calcular_edad_alberto(Edad_juan)
    Edad_ana = Ejercicioo_4.Calcular_edad_ana(Edad_juan)
    Edad_mama = Ejercicioo_4.Calcular_edad_mama(Edad_alberto, Edad_ana, Edad_juan)

    print(f"\nJuan: {Edad_juan} años")
    print(f"Alberto: {Edad_alberto} años")
    print(f"Ana: {Edad_ana} años")
    print(f"Mamá: {Edad_mama} años")
