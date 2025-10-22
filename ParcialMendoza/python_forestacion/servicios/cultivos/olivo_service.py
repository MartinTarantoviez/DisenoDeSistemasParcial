from typing import TYPE_CHECKING

from python_forestacion.constantes import ALTURA_INCREMENTO_OLIVO
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import (
    AbsorcionSeasonalStrategy,
)
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """Servicio específico para Olivo (estacional + crecimiento menor)."""

    def __init__(self) -> None:
        super().__init__(AbsorcionSeasonalStrategy())

    def _post_absorcion(self, cultivo: "Olivo", litros_absorbidos: int) -> None:
        self._crecer(cultivo, ALTURA_INCREMENTO_OLIVO)

    def mostrar_datos(self, cultivo: "Olivo") -> None:
        super().mostrar_datos(cultivo)
        print(f"ID: {cultivo.get_id()}")
        print(f"Altura: {cultivo.get_altura()} m")
        print(f"Tipo de aceituna: {cultivo.get_tipo_aceituna().name}")

    def __repr__(self) -> str:
        return super().__repr__()
