from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Siempre devuelve la misma cantidad de litros."""

    def __init__(self, cantidad_constante: int) -> None:
        self._cantidad = int(cantidad_constante)

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: object,
    ) -> int:
        return self._cantidad

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._cantidad})"
