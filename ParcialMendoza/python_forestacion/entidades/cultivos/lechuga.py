"""
Modulo que define la entidad Lechuga.

Este modulo contiene la clase Lechuga, que representa una hortaliza de tipo lechuga
en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/cultivos/lechuga.py
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_LECHUGA,
    SUPERFICIE_LECHUGA,
    VARIEDAD_LECHUGA_DEFAULT
)


class Lechuga(Cultivo, Hortaliza):
    """
    Entidad que representa una hortaliza de tipo Lechuga.
    
    La Lechuga es una hortaliza de hoja verde que se cultiva en invernadero,
    requiere 0.10m² de superficie y absorbe agua de forma constante (1L).
    
    Attributes:
        _variedad: Variedad de la lechuga (Crespa, Mantecosa, Morada, etc.)
    """
    
    def __init__(self, variedad: str = VARIEDAD_LECHUGA_DEFAULT):
        """
        Inicializa una Lechuga con variedad especifica.
        
        Args:
            variedad: Variedad de la lechuga (default: VARIEDAD_LECHUGA_DEFAULT)
        """
        # Inicializar Cultivo (agua y superficie)
        Cultivo.__init__(self, AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA)
        
        # Inicializar Hortaliza (siempre en invernadero)
        Hortaliza.__init__(self, AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA, invernadero=True)
        
        # Atributos propios
        self._variedad = variedad
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_variedad(self) -> str:
        """
        Obtiene la variedad de la lechuga.
        
        Returns:
            Variedad de la lechuga
        """
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        """
        Establece la variedad de la lechuga.
        
        Args:
            variedad: Nueva variedad de la lechuga
        """
        self._variedad = variedad
    
    # ========================================================================
    # METODOS HEREDADOS
    # ========================================================================
    
    def __str__(self) -> str:
        """
        Representacion en cadena de la lechuga.
        
        Returns:
            Nombre del tipo de cultivo
        """
        return "Lechuga"