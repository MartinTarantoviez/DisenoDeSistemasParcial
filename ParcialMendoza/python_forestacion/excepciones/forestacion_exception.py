"""
Excepción base del sistema forestal.

Todas las excepciones del dominio heredan de esta clase.
"""

# Standard library
from typing import Optional

# Local application
from python_forestacion.excepciones.mensajes_exception import MSG_FORESTACION_GENERICO


class ForestacionException(Exception):
    """
    Excepción base para el sistema de gestión forestal.
    
    Todas las excepciones específicas del dominio heredan de esta clase.
    Proporciona separación entre mensajes para usuario y técnicos.
    
    Attributes:
        _mensaje_usuario: Mensaje simple para mostrar al usuario final
        _mensaje_tecnico: Mensaje detallado para logs y debugging
        _causa: Excepción original que causó este error (opcional)
    """
    
    def __init__(
        self,
        mensaje_usuario: str = MSG_FORESTACION_GENERICO,
        mensaje_tecnico: str = "",
        causa: Optional[Exception] = None
    ):
        """
        Inicializa la excepción base.
        
        Args:
            mensaje_usuario: Mensaje simple para usuario final
            mensaje_tecnico: Mensaje detallado para técnicos
            causa: Excepción original (opcional)
        """
        super().__init__(mensaje_usuario)
        self._mensaje_usuario = mensaje_usuario
        self._mensaje_tecnico = mensaje_tecnico or mensaje_usuario
        self._causa = causa
    
    def get_user_message(self) -> str:
        """
        Obtiene mensaje para usuario final.
        
        Returns:
            Mensaje simple y claro
        """
        return self._mensaje_usuario
    
    def get_technical_message(self) -> str:
        """
        Obtiene mensaje técnico detallado.
        
        Returns:
            Mensaje con detalles técnicos
        """
        return self._mensaje_tecnico
    
    def get_causa(self) -> Optional[Exception]:
        """
        Obtiene la excepción original que causó este error.
        
        Returns:
            Excepción original o None
        """
        return self._causa
    
    def get_full_message(self) -> str:
        """
        Obtiene mensaje completo con toda la información.
        
        Returns:
            Mensaje usuario + técnico + causa
        """
        mensaje = f"{self._mensaje_usuario}\n{self._mensaje_tecnico}"
        
        if self._causa:
            mensaje += f"\nCausa: {str(self._causa)}"
        
        return mensaje