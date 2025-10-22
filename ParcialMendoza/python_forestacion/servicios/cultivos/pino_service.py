from typing import TYPE_CHECKING

from python_forestacion.constantes import ALTURA_INCREMENTO_PINO
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import (
    AbsorcionSeasonalStrategy,
)
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """Servicio específico para Pino (estrategia estacional + crecimiento)."""

    def __init__(self) -> None:
        super().__init__(AbsorcionSeasonalStrategy())

    def _post_absorcion(self, cultivo: "Pino", litros_absorbidos: int) -> None:
        self._crecer(cultivo, ALTURA_INCREMENTO_PINO)

    def mostrar_datos(self, cultivo: "Pino") -> None:
        super().mostrar_datos(cultivo)
        print(f"ID: {cultivo.get_id()}")
        print(f"Altura: {cultivo.get_altura()} m")
        print(f"Variedad: {cultivo.get_variedad()}")

    def __repr__(self) -> str:
        return super().__repr__()
