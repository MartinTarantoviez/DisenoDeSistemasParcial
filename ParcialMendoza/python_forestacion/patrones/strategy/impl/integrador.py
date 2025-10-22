"""
Archivo integrador generado automaticamente
Directorio: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/strategy/impl
Fecha: 2025-10-22 01:16:07
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ================================================================================

from datetime import date
from python_forestacion.constantes import (
    MES_INICIO_VERANO,
    MES_FIN_VERANO,
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
)
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Verano: 5L, resto: 2L (según constantes)."""

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: object,
    ) -> int:
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        return ABSORCION_SEASONAL_INVIERNO


