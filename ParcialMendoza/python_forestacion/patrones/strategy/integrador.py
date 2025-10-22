"""
Archivo integrador generado automaticamente
Directorio: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/strategy
Fecha: 2025-10-22 01:16:07
Total de archivos integrados: 1
"""

# ================================================================================
# ARCHIVO 1/1: absorcion_agua_strategy.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ================================================================================

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


