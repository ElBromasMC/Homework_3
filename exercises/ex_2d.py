import numpy as np
import math

class CampoResultante3D:
    def __init__(self, x, y, z) -> None:
        self.pos = (x, y, z)
        self.modulo = np.sqrt(x**2 + y**2 + z**2)
        self.direc_angle = (0,0,0)                        

    def direcAngles(self):
       alpha = math.degrees(math.acos(self.pos[0]/self.modulo))
       betha = math.degrees(math.acos(self.pos[1]/self.modulo))
       phi   = math.degrees(math.acos(self.pos[2]/self.modulo))
       self.direc_angle = (alpha, betha, phi)

     
class Carga:
    def __init__(self, carga=1.602e-19, x=0, y=0, z=0) -> None:
        self.q = carga
        self.pos = (x, y, z)
        self.campo = (0, 0, 0) 

    # Calcula el campo que hay entre la carga y el punto (x,y)
    
    def calc_Er(self, pos):
        k = 9e9
        r = np.sqrt((pos[0] - self.pos[0])**2 + (pos[1] - self.pos[1])**2 + (pos[2] - self.pos[2])**2)
        temp = (k * abs(self.q)) / r**3
        # Si la particula es un electron o proton
        if self.q > 0:
            self.campo = (temp * (pos[0] - self.pos[0]), temp * (pos[1] - self.pos[1]), temp * (pos[2] - self.pos[2]))
        else:
            self.campo = (temp * (self.pos[0] - pos[0]), temp * (self.pos[1] - pos[1]), temp * (self.pos[2] - pos[2]))

# Devulve la suma de todos los campos
def resultante(list_carga):
    Er = (0, 0, 0) 

    for i in list_carga:
        Er = (Er[0] + i.campo[0], Er[1] + i.campo[1], Er[2] + i.campo[2])  

    return Er

if __name__ == "__main__":
    try:
        # Cantidad de Cargas electricas en el Plano
        n = int(input("Enter the number of charges to input: "))
        list_carga = []

        #Aviso de uso de Notacion Cientifica
        print("Recuerda poner en notacion cientifica (nem es n x 10^{m})")

        # Guardando los datos de cada carga en el Plano
        for i in range(n):
            carga_input = input(f"\nEnter the electric charge for the charge. {i + 1}\n(default 1.602e-19, press Enter for default): ")
            carga = float(carga_input) if carga_input else 1.602e-19
            x = float(input(f"Enter the X-coordinate for the charge {i + 1}: "))
            y = float(input(f"Enter the Y-coordinate for the charge {i + 1}: "))
            z = float(input(f"Enter the Z-coordinate for the charge {i + 1}: "))
            if carga >=0 :
                list_carga.append(Carga(carga, x, y, z))
            else: list_carga.append(Carga(abs(carga), -x, -y, -z))
        
        # Posicion en donde se calculara el Campo Electrico
        print("\nNow you will enter the coordinates where you want to calculate the Electric Field.")
        pos_x = float(input("Enter the X-coordinate: "))
        pos_y = float(input("Enter the Y-coordinate: "))
        pos_z = float(input("Enter the Z-coordinate: "))
        pos = (pos_x, pos_y, pos_z)

        # Hallan el Campo que hay entre el punto y la carga
        for carga in list_carga:
            carga.calc_Er(pos)
        
        # Suma de los Campos electricos
        resultado = resultante(list_carga)
        # Creando un Objeto Campo para guardar los datos
        Er = CampoResultante3D(resultado[0], resultado[1], resultado[2])
        Er.direcAngles()

        # Imprimiendo resultados
        if Er.pos[1]>= 0 and Er.pos[0] >= 0:
            print(f"\nThe vector notation of the electric field is {Er.pos[0]:.2e}i + {Er.pos[1]:.2e}j + {Er.pos[2]:.2e}k")
        elif Er.pos[1] < 0 and Er.pos[0] >= 0:
            print(f"\nThe vector notation of the electric field is {Er.pos[0]:.2e}i - {-Er.pos[1]:.2e}j + {Er.pos[2]:.2e}k")
        elif Er.pos[1] >= 0 and Er.pos[0] < 0:
            print(f"\nThe vector notation of the electric field is {Er.pos[0]:.2e}i + {Er.pos[1]:.2e}j - {-Er.pos[2]:.2e}k")
        else:
            print(f"\nThe vector notation of the electric field is {Er.pos[0]:.2e}i - {-Er.pos[1]:.2e}j - {-Er.pos[2]:.2e}k")

        print(f"The magnitude of the electric field is {Er.modulo:.2e}")
        print(f"The inclination angle on the:\nX-axis: {Er.direc_angle[0]:.2f}°\nY-axis: {Er.direc_angle[1]:.2f}°\nZ-axis: {Er.direc_angle[2]:.2f}°")

    # ValueError: Si la cadena de texto ingresada no se puede convertir en un número válido.
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

    # ZeroDivisionError: Si la distancia entre la carga y el punto es cero
    except ZeroDivisionError:
        print("Division by zero occurred. Please check your input values.")
