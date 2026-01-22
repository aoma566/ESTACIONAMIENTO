"""
Programa principal
Demuestra el uso de constructores y destructores
en un sistema de estacionamiento.
"""

from modelos.vehiculo import Vehiculo
from servicios.servicios_estacionamiento import EstacionamientoService

def main():
    estacionamiento = EstacionamientoService()

    vehiculo1 = Vehiculo("IW-723D", "Anderson")
    vehiculo2 = Vehiculo("MDO-759", "Viviana")

    estacionamiento.ingresar_vehiculo(vehiculo1)
    estacionamiento.ingresar_vehiculo(vehiculo2)

    estacionamiento.mostrar_vehiculos()

    estacionamiento.retirar_vehiculo("IW-723D")

    estacionamiento.mostrar_vehiculos()

if __name__ == "__main__":
    main()
