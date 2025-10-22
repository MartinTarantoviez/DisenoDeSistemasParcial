"""
Modulo que define la interfaz base Cultivo.

Este modulo contiene la clase abstracta Cultivo que sirve como base
para todos los tipos de cultivos del sistema (arboles y hortalizas).

Ubicacion: python_forestacion/entidades/cultivos/cultivo.py
"""

from abc import ABC, abstractmethod


class Cultivo(ABC):
    """
    Interfaz base para todos los cultivos del sistema.
    
    Esta clase abstracta define los atributos y metodos comunes
    que deben implementar todos los cultivos (Pino, Olivo, Lechuga, Zanahoria).
    
    Attributes:
        _agua: Cantidad de agua almacenada en litros
        _superficie: Superficie ocupada por el cultivo en metros cuadrados
    """
    
    def __init__(self, agua: int, superficie: float):
        """
        Inicializa un cultivo con agua y superficie.
        
        Args:
            agua: Cantidad inicial de agua en litros (debe ser >= 0)
            superficie: Superficie ocupada en metros cuadrados (debe ser > 0)
            
        Raises:
            ValueError: Si agua < 0 o superficie <= 0
        """
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
            
        self._agua = agua
        self._superficie = superficie
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_agua(self) -> int:
        """
        Obtiene la cantidad de agua almacenada.
        
        Returns:
            Cantidad de agua en litros
        """
        return self._agua
    
    def set_agua(self, agua: int) -> None:
        """
        Establece la cantidad de agua almacenada.
        
        Args:
            agua: Nueva cantidad de agua en litros
            
        Raises:
            ValueError: Si agua < 0
        """
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        self._agua = agua
    
    def get_superficie(self) -> float:
        """
        Obtiene la superficie ocupada por el cultivo.
        
        Returns:
            Superficie en metros cuadrados
        """
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie ocupada por el cultivo.
        
        Args:
            superficie: Nueva superficie en metros cuadrados
            
        Raises:
            ValueError: Si superficie <= 0
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie
    
    # ========================================================================
    # METODOS ABSTRACTOS
    # ========================================================================
    
    @abstractmethod
    def __str__(self) -> str:
        """
        Representacion en cadena del cultivo.
        
        Returns:
            Nombre del tipo de cultivo
        """
        pass