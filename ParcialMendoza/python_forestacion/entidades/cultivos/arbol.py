"""
Modulo que define la clase base Arbol.

Este modulo contiene la clase abstracta Arbol que sirve como base
para todos los cultivos arboreos del sistema (Pino, Olivo).

Ubicacion: python_forestacion/entidades/cultivos/arbol.py
"""

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

from python_forestacion.constantes import ALTURA_INICIAL_ARBOL


class Arbol(ABC):
    """
    Clase base para cultivos arboreos.
    
    Los arboles tienen caracteristicas especiales como altura y crecimiento.
    Esta clase hereda de Cultivo y agrega funcionalidad especifica de arboles.
    
    Attributes:
        _altura: Altura del arbol en metros
        _id: Identificador unico del arbol
    """
    
    _contador_id = 0
    """Contador estatico para generar IDs unicos."""
    
    def __init__(self, agua: int, superficie: float, altura: float = ALTURA_INICIAL_ARBOL):
        """
        Inicializa un arbol con agua, superficie y altura.
        
        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie ocupada en metros cuadrados
            altura: Altura inicial del arbol en metros (default: ALTURA_INICIAL_ARBOL)
            
        Raises:
            ValueError: Si altura <= 0
        """
        # Nota: No llamamos a super().__init__() porque Python usa MRO
        # Las subclases concretas (Pino, Olivo) llamaran a Cultivo.__init__()
        
        if altura <= 0:
            raise ValueError("La altura debe ser mayor a cero")
        
        self._altura = altura
        
        # Asignar ID unico
        Arbol._contador_id += 1
        self._id = Arbol._contador_id
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_altura(self) -> float:
        """
        Obtiene la altura del arbol.
        
        Returns:
            Altura en metros
        """
        return self._altura
    
    def set_altura(self, altura: float) -> None:
        """
        Establece la altura del arbol.
        
        Args:
            altura: Nueva altura en metros
            
        Raises:
            ValueError: Si altura <= 0
        """
        if altura <= 0:
            raise ValueError("La altura debe ser mayor a cero")
        self._altura = altura
    
    def get_id(self) -> int:
        """
        Obtiene el ID unico del arbol.
        
        Returns:
            ID del arbol
        """
        return self._id