"""
Modulo que define el enum TipoAceituna.

Este modulo contiene la enumeracion de tipos de aceitunas
disponibles para los olivos.

Ubicacion: python_forestacion/entidades/cultivos/tipo_aceituna.py
"""

from enum import Enum


class TipoAceituna(Enum):
    """
    Enumeracion de tipos de aceitunas.
    
    Define los tipos de aceitunas que pueden tener los olivos.
    """
    
    ARBEQUINA = "Arbequina"
    """Aceituna tipo Arbequina."""
    
    PICUAL = "Picual"
    """Aceituna tipo Picual."""
    
    MANZANILLA = "Manzanilla"
    """Aceituna tipo Manzanilla."""