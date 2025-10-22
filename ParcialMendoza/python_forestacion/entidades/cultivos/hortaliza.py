"""
Modulo que define la clase base Hortaliza.

Este modulo contiene la clase abstracta Hortaliza que sirve como base
para todos los cultivos horticolas del sistema (Lechuga, Zanahoria).

Ubicacion: python_forestacion/entidades/cultivos/hortaliza.py
"""

from abc import ABC


class Hortaliza(ABC):
    """
    Clase base para cultivos horticolas.
    
    Las hortalizas tienen caracteristicas especiales como el cultivo
    en invernadero. Esta clase hereda de Cultivo y agrega funcionalidad
    especifica de hortalizas.
    
    Attributes:
        _invernadero: Indica si la hortaliza se cultiva en invernadero
    """
    
    def __init__(self, agua: int, superficie: float, invernadero: bool):
        """
        Inicializa una hortaliza con agua, superficie e invernadero.
        
        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie ocupada en metros cuadrados
            invernadero: True si se cultiva en invernadero, False en caso contrario
        """
        # Nota: No llamamos a super().__init__() porque Python usa MRO
        # Las subclases concretas (Lechuga, Zanahoria) llamaran a Cultivo.__init__()
        
        self._invernadero = invernadero
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def es_de_invernadero(self) -> bool:
        """
        Verifica si la hortaliza se cultiva en invernadero.
        
        Returns:
            True si es de invernadero, False en caso contrario
        """
        return self._invernadero
    
    def set_invernadero(self, invernadero: bool) -> None:
        """
        Establece si la hortaliza se cultiva en invernadero.
        
        Args:
            invernadero: True para invernadero, False para campo abierto
        """
        self._invernadero = invernadero