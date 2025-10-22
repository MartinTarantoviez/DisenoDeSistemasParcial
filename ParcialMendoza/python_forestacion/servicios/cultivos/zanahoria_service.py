from typing import TYPE_CHECKING

from python_forestacion.constantes import ABSORCION_ZANAHORIA
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import (
    AbsorcionConstanteStrategy,
)
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """Servicio para Zanahoria (absorción constante)."""

    def __init__(self) -> None:
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_ZANAHORIA))

    def mostrar_datos(self, cultivo: "Zanahoria") -> None:
        super().mostrar_datos(cultivo)
        print(f"Es baby carrot: {cultivo.is_baby_carrot()}")

    def __repr__(self) -> str:
        return super().__repr__()
