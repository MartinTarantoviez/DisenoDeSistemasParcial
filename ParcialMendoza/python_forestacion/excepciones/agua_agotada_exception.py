"""
Excepción lanzada cuando no hay suficiente agua para regar.
"""

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_AGUA_AGOTADA_USER,
    MSG_AGUA_AGOTADA_TECH
)
from python_forestacion.constantes import AGUA_MINIMA


class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando el agua disponible es insuficiente.
    
    Se lanza cuando se intenta regar con menos de 10L disponibles.
    
    Attributes:
        _agua_disponible: Litros de agua disponible
    """
    
    def __init__(self, agua_disponible: int):
        """
        Inicializa la excepción con datos de agua.
        
        Args:
            agua_disponible: Litros de agua disponible
        """
        mensaje_tecnico = (
            f"{MSG_AGUA_AGOTADA_TECH} - "
            f"Disponible: {agua_disponible}L, "
            f"Mínimo requerido: {AGUA_MINIMA}L"
        )
        
        super().__init__(
            mensaje_usuario=MSG_AGUA_AGOTADA_USER,
            mensaje_tecnico=mensaje_tecnico
        )
        
        self._agua_disponible = agua_disponible
    
    def get_agua_disponible(self) -> int:
        """
        Obtiene el agua disponible.
        
        Returns:
            Litros de agua disponible
        """
        return self._agua_disponible