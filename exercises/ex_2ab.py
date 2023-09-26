import numpy as np
import math

class CampoResultante:
    def __init__(self, x, y) -> None:
        self.pos = (x, y)
        self.modulo = np.sqrt(x**2 + y**2)
        self.angle = 0
        self.angleX = 0

    #Calcula la direccion del Campo
    def calcAngle(self):
        if self.pos[0] == 0:
            if self.pos[1] > 0:
                self.angle = 90.0
            elif self.pos[1] < 0:
                self.angle = 270.0
            else:
                self.angle = 0.0
        elif self.pos[1] == 0:
            if self.pos[0] > 0:
                self.angle = 0.0
            else:
                self.angle = 180.0
        else:
            self.angle = math.degrees(math.atan2(self.pos[1], self.pos[0]))
        
        self.calcAngleX()

    # Calcula el angulo que forma el campo con el Eje X
    def calcAngleX(self):
        if self.angle > 0 and self.angle < 90:
            self.angleX = self.angle
        elif self.angle > 90 and self.angle < 180:
            self.angleX = 180.0 - self.angle
        elif self.angle > 180 and self.angle < 270:
            self.angleX = 270.0 - self.angle
        else:
            self.angleX = 360.0 - self.angle

        

class Particula:
    def __init__(self, carga=1.6e-19, x=0, y=0) -> None:
        self.q = carga
        self.pos = (x, y)
        self.campo = (0, 0) 

    # Calcula el campo que hay entre la carga y el punto (x,y)
    def calc_Er(self, pos):
        k = 9e9
        r = np.sqrt((pos[0] - self.pos[0])**2 + (pos[1] - self.pos[1])**2)
        temp = (k * abs(self.q)) / r**3
        
        #Si la particula es un electron o proton
        if self.q > 0:
            self.campo = (temp * (pos[0] - self.pos[0]), temp * (pos[1] - self.pos[1]))
        else:
            self.campo = (temp * (self.pos[0] - pos[0]), temp * (self.pos[1] - pos[1]))

# Devulve la suma de todos los campos
def resultante(list_carga):
    Er = (0, 0) 

    for i in list_carga:
        Er = (Er[0] + i.campo[0], Er[1] + i.campo[1])  

    return Er

if __name__ == "__main__":
    try:
        # Cantidad de Cargas electricas en el Plano
        n = int(input("Enter the number of charges to input: "))
        list_carga = []

        #Aviso de uso de Notacion Cientifica
        print("Recuerda poner en notacion cientifica (nem <> n x 10^{m})")

        # Guardando los datos de cada carga en el Plano
        for i in range(n):
            carga_input = input(f"\nEnter the electric charge for the charge. {i + 1}\n(default 1.6e-19, press Enter for default): ")
            carga = float(carga_input) if carga_input else 1.6e-19
            x = float(input(f"Enter the X-coordinate for the charge {i + 1}: "))
            y = float(input(f"Enter the Y-coordinate for the charge {i + 1}: "))
            list_carga.append(Particula(carga, x, y))
        
        # Posicion en donde se calculara el Campo Electrico
        print("\nNow you will enter the coordinates where you want to calculate the Electric Field.")
        pos_x = float(input("Enter the X-coordinate: "))
        pos_y = float(input("Enter the Y-coordinate: "))
        pos = (pos_x, pos_y)

        # Hallan el Campo que hay entre el punto y la carga
        for particula in list_carga:
            particula.calc_Er(pos)
        
        # Suma de los Campos electricos
        resultado = resultante(list_carga)
        # Creando un Objeto Campo para guardar los datos
        Er = CampoResultante(resultado[0], resultado[1])
        Er.calcAngle()

        # Imprimiendo resultados
        if Er.pos[1]>= 0:
            print(f"\nThe vector notation of the electric field is {Er.pos[0]:.2e}i + {Er.pos[1]:.2e}j")
        else: 
            print(f"\nThe vector notation of the electric field is {Er.pos[0]:.2e}i - {-Er.pos[1]:.2e}j")
        print(f"The magnitude of the electric field is {Er.modulo:.2e}")
        print(f"The direction of the electric field is  {Er.angle:.2f}")

    # ValueError: Si la cadena de texto ingresada no se puede convertir en un número válido.
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

    # ZeroDivisionError: Si la distancia entre la carga y el punto es cero
    except ZeroDivisionError:
        print("Division by zero occurred. Please check your input values.")
