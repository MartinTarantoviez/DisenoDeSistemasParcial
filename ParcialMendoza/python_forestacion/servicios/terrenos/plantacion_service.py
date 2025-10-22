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
