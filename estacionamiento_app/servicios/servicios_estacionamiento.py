from modelos.vehiculo import Vehiculo

class EstacionamientoService:
    """
    Servicio que gestiona los vehículos del estacionamiento.
    """

    def __init__(self):
        """
        Constructor del servicio.
        Inicializa la lista de vehículos.
        """
        self.vehiculos = []

    def ingresar_vehiculo(self, vehiculo: Vehiculo):
        """
        Agrega un vehículo al estacionamiento.
        """
        self.vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        """
        Muestra todos los vehículos estacionados.
        """
        print("\nVehículos en el estacionamiento:")
        for v in self.vehiculos:
            print(f"- {v.placa} | {v.propietario}")

    def retirar_vehiculo(self, placa: str):
        """
        Retira un vehículo según la placa.
        """
        for v in self.vehiculos:
            if v.placa == placa:
                self.vehiculos.remove(v)
                del v  # Aquí se ejecuta el destructor
                break
