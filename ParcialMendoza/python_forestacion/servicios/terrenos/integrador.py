"""
Archivo integrador generado automaticamente
Directorio: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/terrenos
Fecha: 2025-10-22 01:16:07
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/terrenos/plantacion_service.py
# ================================================================================

from typing import TYPE_CHECKING, List
from datetime import date

from python_forestacion.constantes import AGUA_MINIMA, AGUA_RIEGO
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class PlantacionService:
    """Operaciones sobre una Plantación (plantar, regar, fumigar, etc.)."""

    def __init__(self) -> None:
        self._registry = CultivoServiceRegistry.get_instance()

    # -------------------------- Plantar --------------------------
    def plantar(self, plantacion: "Plantacion", especie: str, cantidad: int) -> None:
        nuevos: List["Cultivo"] = []
        for _ in range(int(cantidad)):
            cultivo = CultivoFactory.crear_cultivo(especie)  # Factory Method
            # Control de superficie disponible
            superficie_usada = sum(c.get_superficie() for c in plantacion.get_cultivos())
            if superficie_usada + cultivo.get_superficie() > plantacion.get_superficie():
                from python_forestacion.excepciones.superficie_insuficiente_exception import (
                    SuperficieInsuficienteException,
                )
                raise SuperficieInsuficienteException(
                    "No hay superficie disponible para plantar más cultivos"
                )
            nuevos.append(cultivo)

        # añadir todos juntos
        tmp = plantacion.get_cultivos()
        tmp.extend(nuevos)
        plantacion.set_cultivos(tmp)

    # --------------------------- Riego ---------------------------
    def regar(
        self,
        plantacion: "Plantacion",
        fecha: date | None = None,
        temperatura: float = 0.0,
        humedad: float = 0.0,
    ) -> None:
        """
        Resta AGUA_RIEGO del estanque de la plantación y hace que cada cultivo
        absorba agua según su Strategy (vía Registry).
        """
        if plantacion.get_agua_disponible() < AGUA_MINIMA:
            from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
            raise AguaAgotadaException("No hay agua suficiente en la plantación")

        # consumir agua del estanque de la plantación
        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - AGUA_RIEGO)

        # cada cultivo absorbe según su Strategy (usamos el Registry para despachar)
        for cultivo in plantacion.get_cultivos():
            self._registry.absorber_agua(cultivo)

    # -------------------------- Fumigar --------------------------
    def fumigar(self, plantacion: "Plantacion", plaguicida: str) -> None:
        """
        Aplica una fumigación a toda la plantación (demo: solo loguea la acción).
        """
        if not plaguicida or not plaguicida.strip():
            raise ValueError("El nombre del plaguicida no puede ser vacío")

        cant = len(plantacion.get_cultivos())
        try:
            nombre = plantacion.get_nombre()
        except AttributeError:
            nombre = "Plantación"

        print(f"[FUMIGACION] Aplicando '{plaguicida}' a {cant} cultivos en {nombre}")

    # ------------------------- Utilidades ------------------------
    def mostrar_cultivos(self, plantacion: "Plantacion") -> None:
        for c in plantacion.get_cultivos():
            self._registry.mostrar_datos(c)


# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/terrenos/tierra_service.py
# ================================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION

class TierraService:
    """Crea Tierra y su Plantación asociada."""

    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str,
    ) -> Tierra:
        tierra = Tierra(id_padron_catastral, superficie, domicilio)
        plantacion = Plantacion(nombre_plantacion, superficie, AGUA_INICIAL_PLANTACION)
        tierra.set_finca(plantacion)
        return tierra


