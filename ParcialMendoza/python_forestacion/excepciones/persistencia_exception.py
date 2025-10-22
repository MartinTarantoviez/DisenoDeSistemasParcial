"""
Excepción lanzada durante operaciones de persistencia.

Cubre errores de lectura/escritura de archivos con Pickle.
"""

# Standard library
from enum import Enum
from typing import Optional

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_PERSISTENCIA_ESCRITURA_USER,
    MSG_PERSISTENCIA_LECTURA_USER,
    MSG_PERSISTENCIA_TECH
)


class TipoOperacion(Enum):
    """
    Tipo de operación de persistencia que falló.
    """
    LECTURA = "lectura"
    ESCRITURA = "escritura"


class PersistenciaException(ForestacionException):
    """
    Excepción lanzada durante operaciones de persistencia.
    
    Proporciona información específica sobre:
    - Tipo de operación (lectura/escritura)
    - Nombre del archivo afectado
    - Causa técnica del error
    
    Attributes:
        _nombre_archivo: Nombre del archivo involucrado
        _tipo_operacion: Tipo de operación que falló
    """
    
    def __init__(
        self,
        nombre_archivo: str,
        tipo_operacion: TipoOperacion,
        mensaje_usuario: str = "",
        mensaje_tecnico: str = MSG_PERSISTENCIA_TECH,
        causa: Optional[Exception] = None
    ):
        """
        Inicializa la excepción de persistencia.
        
        Args:
            nombre_archivo: Nombre del archivo
            tipo_operacion: Tipo de operación (lectura/escritura)
            mensaje_usuario: Mensaje personalizado para usuario
            mensaje_tecnico: Mensaje técnico detallado
            causa: Excepción original
        """
        # Determinar mensaje de usuario por defecto
        if not mensaje_usuario:
            if tipo_operacion == TipoOperacion.ESCRITURA:
                mensaje_usuario = MSG_PERSISTENCIA_ESCRITURA_USER
            else:
                mensaje_usuario = MSG_PERSISTENCIA_LECTURA_USER
        
        # Enriquecer mensaje técnico
        mensaje_tecnico_completo = (
            f"{mensaje_tecnico} - "
            f"Archivo: {nombre_archivo}, "
            f"Operación: {tipo_operacion.value}"
        )
        
        super().__init__(
            mensaje_usuario=mensaje_usuario,
            mensaje_tecnico=mensaje_tecnico_completo,
            causa=causa
        )
        
        self._nombre_archivo = nombre_archivo
        self._tipo_operacion = tipo_operacion
    
    def get_nombre_archivo(self) -> str:
        """
        Obtiene el nombre del archivo involucrado.
        
        Returns:
            Nombre del archivo
        """
        return self._nombre_archivo
    
    def get_tipo_operacion(self) -> TipoOperacion:
        """
        Obtiene el tipo de operación que falló.
        
        Returns:
            Tipo de operación (lectura/escritura)
        """
        return self._tipo_operacion