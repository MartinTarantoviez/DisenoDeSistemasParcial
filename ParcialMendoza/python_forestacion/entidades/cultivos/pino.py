"""
Modulo que define la entidad Pino.

Este modulo contiene la clase Pino, que representa un arbol de tipo pino
en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/cultivos/pino.py
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import (
    AGUA_INICIAL_PINO,
    SUPERFICIE_PINO,
    ALTURA_INICIAL_ARBOL,
    VARIEDAD_PINO_DEFAULT
)


class Pino(Cultivo, Arbol):
    """
    Entidad que representa un arbol de tipo Pino.
    
    El Pino es un arbol maderable que requiere 2m² de superficie,
    crece en altura al recibir agua y absorbe agua de forma estacional.
    
    Attributes:
        _variedad: Variedad del pino (Parana, Elliott, Taeda, etc.)
    """
    
    def __init__(self, variedad: str = VARIEDAD_PINO_DEFAULT):
        """
        Inicializa un Pino con variedad especifica.
        
        Args:
            variedad: Variedad del pino (default: VARIEDAD_PINO_DEFAULT)
        """
        # Inicializar Cultivo (agua y superficie)
        Cultivo.__init__(self, AGUA_INICIAL_PINO, SUPERFICIE_PINO)
        
        # Inicializar Arbol (altura)
        Arbol.__init__(self, AGUA_INICIAL_PINO, SUPERFICIE_PINO, ALTURA_INICIAL_ARBOL)
        
        # Atributos propios
        self._variedad = variedad
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_variedad(self) -> str:
        """
        Obtiene la variedad del pino.
        
        Returns:
            Variedad del pino
        """
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        """
        Establece la variedad del pino.
        
        Args:
            variedad: Nueva variedad del pino
        """
        self._variedad = variedad
    
    # ========================================================================
    # METODOS HEREDADOS
    # ========================================================================
    
    def __str__(self) -> str:
        """
        Representacion en cadena del pino.
        
        Returns:
            Nombre del tipo de cultivo
        """
        return "Pino"