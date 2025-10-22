"""
Modulo que define la entidad Olivo.

Este modulo contiene la clase Olivo, que representa un arbol de tipo olivo
en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/cultivos/olivo.py
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import (
    AGUA_INICIAL_OLIVO,
    SUPERFICIE_OLIVO,
    ALTURA_INICIAL_OLIVO
)


class Olivo(Cultivo, Arbol):
    """
    Entidad que representa un arbol de tipo Olivo.
    
    El Olivo es un arbol frutal que produce aceitunas, requiere 3m² de superficie,
    crece en altura al recibir agua (mas lento que el pino) y absorbe agua
    de forma estacional.
    
    Attributes:
        _tipo_aceituna: Tipo de aceituna que produce (Arbequina, Picual, Manzanilla)
    """
    
    def __init__(self, tipo_aceituna: TipoAceituna = TipoAceituna.ARBEQUINA):
        """
        Inicializa un Olivo con tipo de aceituna especifico.
        
        Args:
            tipo_aceituna: Tipo de aceituna del olivo (default: TipoAceituna.ARBEQUINA)
        """
        # Inicializar Cultivo (agua y superficie)
        Cultivo.__init__(self, AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO)
        
        # Inicializar Arbol (altura - los olivos son mas bajos inicialmente)
        Arbol.__init__(self, AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO, ALTURA_INICIAL_OLIVO)
        
        # Atributos propios
        self._tipo_aceituna = tipo_aceituna
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_tipo_aceituna(self) -> TipoAceituna:
        """
        Obtiene el tipo de aceituna del olivo.
        
        Returns:
            Tipo de aceituna (enum)
        """
        return self._tipo_aceituna
    
    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        """
        Establece el tipo de aceituna del olivo.
        
        Args:
            tipo_aceituna: Nuevo tipo de aceituna
        """
        self._tipo_aceituna = tipo_aceituna
    
    # ========================================================================
    # METODOS HEREDADOS
    # ========================================================================
    
    def __str__(self) -> str:
        """
        Representacion en cadena del olivo.
        
        Returns:
            Nombre del tipo de cultivo
        """
        return "Olivo"