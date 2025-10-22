from typing import TYPE_CHECKING, Any

from python_forestacion.constantes import ABSORCION_LECHUGA
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import (
    AbsorcionConstanteStrategy,
)
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """Servicio para Lechuga (absorción constante). Tolerante a distintas APIs de la entidad."""

    def __init__(self) -> None:
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_LECHUGA))

    # -------------------------- Helpers internos --------------------------
    @staticmethod
    def _get_invernadero(cultivo: Any) -> Any:
        """
        Devuelve el valor de 'invernadero' sin asumir un contrato fijo.
        Prueba en orden: is_invernadero(), get_invernadero(), atributo _invernadero.
        """
        if hasattr(cultivo, "is_invernadero") and callable(getattr(cultivo, "is_invernadero")):
            return cultivo.is_invernadero()
        if hasattr(cultivo, "get_invernadero") and callable(getattr(cultivo, "get_invernadero")):
            return cultivo.get_invernadero()
        if hasattr(cultivo, "_invernadero"):
            return getattr(cultivo, "_invernadero")
        return None

    # ---------------------------- API pública ------------------------------
    def mostrar_datos(self, cultivo: "Lechuga") -> None:
        super().mostrar_datos(cultivo)

        # Variedad (si existe getter)
        try:
            print(f"Variedad: {cultivo.get_variedad()}")
        except AttributeError:
            pass

        # Invernadero con fallback robusto
        inv = self._get_invernadero(cultivo)
        if inv is not None:
            print(f"Invernadero: {inv}")

    def __repr__(self) -> str:
        return super().__repr__()
