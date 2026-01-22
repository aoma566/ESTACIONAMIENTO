class Vehiculo:
    """
    Representa un vehículo que ingresa al estacionamiento.
    Demuestra el uso de constructor y destructor.
    """

    def __init__(self, placa: str, propietario: str):
        """
        Constructor:
        Inicializa los atributos del vehículo.
        """
        self.placa = placa
        self.propietario = propietario
        print(f"[ENTRADA] Vehículo {self.placa} - Propietario: {self.propietario}")

    def __del__(self):
        """
        Destructor:
        Se ejecuta cuando el objeto es eliminado.
        """
        print(f"[SALIDA] Vehículo {self.placa} ha salido del estacionamiento")
