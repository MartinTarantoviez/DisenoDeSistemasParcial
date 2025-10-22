"""
Archivo integrador generado automaticamente
Directorio: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/excepciones
Fecha: 2025-10-22 01:16:07
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/excepciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/excepciones/agua_agotada_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/excepciones/forestacion_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/excepciones/mensajes_exception.py
# ================================================================================

"""
Mensajes centralizados para excepciones.

Todos los mensajes de error están aquí para facilitar
internacionalización y mantenimiento.
"""

# Mensajes de ForestacionException
MSG_FORESTACION_GENERICO = "Ha ocurrido un error en el sistema forestal"

# Mensajes de SuperficieInsuficienteException
MSG_SUPERFICIE_INSUFICIENTE_USER = "No hay suficiente superficie disponible para plantar"
MSG_SUPERFICIE_INSUFICIENTE_TECH = "Superficie requerida excede la disponible"

# Mensajes de AguaAgotadaException
MSG_AGUA_AGOTADA_USER = "No hay suficiente agua disponible para regar"
MSG_AGUA_AGOTADA_TECH = "Agua disponible insuficiente para operación de riego"

# Mensajes de PersistenciaException
MSG_PERSISTENCIA_ESCRITURA_USER = "No se pudo guardar el archivo"
MSG_PERSISTENCIA_LECTURA_USER = "No se pudo leer el archivo"
MSG_PERSISTENCIA_TECH = "Error de entrada/salida durante operación de persistencia"

# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/excepciones/persistencia_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ================================================================================

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

