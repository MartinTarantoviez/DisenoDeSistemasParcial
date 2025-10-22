import os
import pickle
from typing import TYPE_CHECKING

from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_DATA
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal

class RegistroForestalService:
    """Persistencia y presentación del Registro Forestal."""

    def __init__(self) -> None:
        self._registry = CultivoServiceRegistry.get_instance()

    def persistir(self, registro: "RegistroForestal") -> None:
        os.makedirs(DIRECTORIO_DATA, exist_ok=True)
        ruta = os.path.join(DIRECTORIO_DATA, f"{registro.get_propietario()}{EXTENSION_DATA}")
        with open(ruta, "wb") as f:
            pickle.dump(registro, f)
        print(f"Registro de {registro.get_propietario()} persistido exitosamente en {ruta}")

    @staticmethod
    def leer_registro(propietario: str) -> "RegistroForestal":
        if not propietario:
            raise ValueError("El nombre del propietario no puede ser nulo o vacío")
        ruta = os.path.join(DIRECTORIO_DATA, f"{propietario}{EXTENSION_DATA}")
        if not os.path.exists(ruta):
            from python_forestacion.excepciones.persistencia_exception import PersistenciaException
            raise PersistenciaException("Archivo no encontrado", ruta)
        with open(ruta, "rb") as f:
            return pickle.load(f)

    def mostrar_datos(self, registro: "RegistroForestal") -> None:
        print("\nREGISTRO FORESTAL\n=================")
        print(f"Padron:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo()}")
        print(f"Domicilio:   {registro.get_tierra().get_domicilio()}")
        print(f"Superficie:  {registro.get_tierra().get_superficie()}")
        cultivos = registro.get_plantacion().get_cultivos()
        print(f"Cantidad de cultivos plantados: {len(cultivos)}")
        print("Listado de Cultivos plantados\n____________________________\n")
        for c in cultivos:
            self._registry.mostrar_datos(c)
            print()
