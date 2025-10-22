"""
Excepción lanzada cuando no hay suficiente superficie para plantar.
"""

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_SUPERFICIE_INSUFICIENTE_USER,
    MSG_SUPERFICIE_INSUFICIENTE_TECH
)


class SuperficieInsuficienteException(ForestacionException):
    """
    Excepción lanzada cuando la superficie requerida excede la disponible.
    
    Proporciona información específica sobre superficie requerida vs disponible.
    
    Attributes:
        _superficie_requerida: Superficie necesaria en m²
        _superficie_disponible: Superficie disponible en m²
    """
    
    def __init__(
        self,
        superficie_requerida: float,
        superficie_disponible: float
    ):
        """
        Inicializa la excepción con datos de superficie.
        
        Args:
            superficie_requerida: m² necesarios
            superficie_disponible: m² disponibles
        """
        mensaje_tecnico = (
            f"{MSG_SUPERFICIE_INSUFICIENTE_TECH} - "
            f"Requerida: {superficie_requerida} m², "
            f"Disponible: {superficie_disponible} m²"
        )
        
        super().__init__(
            mensaje_usuario=MSG_SUPERFICIE_INSUFICIENTE_USER,
            mensaje_tecnico=mensaje_tecnico
        )
        
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible
    
    def get_superficie_requerida(self) -> float:
        """
        Obtiene la superficie requerida.
        
        Returns:
            Superficie requerida en m²
        """
        return self._superficie_requerida
    
    def get_superficie_disponible(self) -> float:
        """
        Obtiene la superficie disponible.
        
        Returns:
            Superficie disponible en m²
        """
        return self._superficie_disponible