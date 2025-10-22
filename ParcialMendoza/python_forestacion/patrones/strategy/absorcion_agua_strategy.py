from abc import ABC, abstractmethod
from datetime import date

class AbsorcionAguaStrategy(ABC):
    """Contrato para calcular cuánta agua absorbe un cultivo en un riego."""

    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: object,  # evitamos imports circulares
    ) -> int:
        """Devuelve litros absorbidos."""
        raise NotImplementedError
