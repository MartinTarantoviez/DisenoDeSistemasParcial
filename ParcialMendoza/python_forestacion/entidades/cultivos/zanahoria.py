"""
Modulo que define la entidad Zanahoria.

Este modulo contiene la clase Zanahoria, que representa una hortaliza de tipo zanahoria
en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/cultivos/zanahoria.py
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_ZANAHORIA,
    SUPERFICIE_ZANAHORIA
)


class Zanahoria(Cultivo, Hortaliza):
    """
    Entidad que representa una hortaliza de tipo Zanahoria.
    
    La Zanahoria es una hortaliza de raiz que se cultiva a campo abierto,
    requiere 0.15m² de superficie, comienza sin agua (0L) y absorbe agua
    de forma constante (2L).
    
    Attributes:
        _baby_carrot: Indica si es una baby carrot (True) o zanahoria regular (False)
    """
    
    def __init__(self, baby_carrot: bool = False):
        """
        Inicializa una Zanahoria especificando si es baby carrot.
        
        Args:
            baby_carrot: True si es baby carrot, False si es zanahoria regular
        """
        # Inicializar Cultivo (agua y superficie)
        Cultivo.__init__(self, AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA)
        
        # Inicializar Hortaliza (NO es de invernadero)
        Hortaliza.__init__(self, AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA, invernadero=False)
        
        # Atributos propios
        self._baby_carrot = baby_carrot
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def is_baby_carrot(self) -> bool:
        """
        Verifica si es una baby carrot.
        
        Returns:
            True si es baby carrot, False si es zanahoria regular
        """
        return self._baby_carrot
    
    def set_baby_carrot(self, baby_carrot: bool) -> None:
        """
        Establece si es una baby carrot.
        
        Args:
            baby_carrot: True para baby carrot, False para zanahoria regular
        """
        self._baby_carrot = baby_carrot
    
    # ========================================================================
    # METODOS HEREDADOS
    # ========================================================================
    
    def __str__(self) -> str:
        """
        Representacion en cadena de la zanahoria.
        
        Returns:
            Nombre del tipo de cultivo
        """
        return "Zanahoria"