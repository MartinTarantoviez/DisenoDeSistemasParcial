# Standard library
from datetime import date
from typing import TYPE_CHECKING, Optional
from abc import ABC

# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import (
    AbsorcionAguaStrategy,
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService(ABC):
    """
    Servicio base para cualquier Cultivo.
    Orquesta la absorción delegando el cálculo a la Strategy inyectada.
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy) -> None:
        self._estrategia_absorcion = estrategia_absorcion

    # --------------------------- API pública ----------------------------
    def absorver_agua(
        self,
        cultivo: "Cultivo",
        fecha: Optional[date] = None,
        temperatura: float = 0.0,
        humedad: float = 0.0,
    ) -> int:
        """Actualiza el agua del cultivo según la Strategy y ejecuta el post-hook."""
        fecha = fecha or date.today()
        litros = self._estrategia_absorcion.calcular_absorcion(
            fecha=fecha,
            temperatura=temperatura,
            humedad=humedad,
            cultivo=cultivo,
        )
        cultivo.set_agua(cultivo.get_agua() + litros)
        self._post_absorcion(cultivo, litros)
        return litros

    def mostrar_datos(self, cultivo: "Cultivo") -> None:
        print(f"Cultivo: {type(cultivo).__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")

    # --------------------------- Hooks ----------------------------------
    def _post_absorcion(self, cultivo: "Cultivo", litros_absorbidos: int) -> None:
        """Hook para subclases (p.ej., crecimiento en árboles)."""
        return

    # ---------------------- Representación por defecto -------------------
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(strategy={self._estrategia_absorcion})"
