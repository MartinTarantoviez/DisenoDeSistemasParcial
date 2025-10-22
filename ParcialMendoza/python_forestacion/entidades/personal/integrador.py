"""
Archivo integrador generado automaticamente
Directorio: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/personal
Fecha: 2025-10-22 01:16:07
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

"""
Modulo que define la entidad AptoMedico.

Este modulo contiene la clase AptoMedico, que representa una certificacion
medica laboral en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/personal/apto_medico.py
"""

from datetime import date


class AptoMedico:
    """
    Entidad que representa un apto medico laboral.
    
    El AptoMedico es una certificacion medica que indica si un trabajador
    esta apto para realizar tareas agricolas. Incluye fecha de emision
    y observaciones medicas opcionales.
    
    Attributes:
        _apto: Estado de aptitud (True si esta apto, False en caso contrario)
        _fecha_emision: Fecha en que se emitio el apto medico
        _observaciones: Observaciones medicas adicionales (opcional)
    """
    
    def __init__(self, apto: bool, fecha_emision: date, observaciones: str = ""):
        """
        Inicializa un AptoMedico con estado, fecha y observaciones.
        
        Args:
            apto: True si el trabajador esta apto, False en caso contrario
            fecha_emision: Fecha de emision del apto medico
            observaciones: Observaciones medicas adicionales (default: "")
        """
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def esta_apto(self) -> bool:
        """
        Verifica si el trabajador esta apto.
        
        Returns:
            True si esta apto, False en caso contrario
        """
        return self._apto
    
    def set_apto(self, apto: bool) -> None:
        """
        Establece el estado de aptitud.
        
        Args:
            apto: True para apto, False para no apto
        """
        self._apto = apto
    
    def get_fecha_emision(self) -> date:
        """
        Obtiene la fecha de emision del apto medico.
        
        Returns:
            Fecha de emision
        """
        return self._fecha_emision
    
    def set_fecha_emision(self, fecha_emision: date) -> None:
        """
        Establece la fecha de emision del apto medico.
        
        Args:
            fecha_emision: Nueva fecha de emision
        """
        self._fecha_emision = fecha_emision
    
    def get_observaciones(self) -> str:
        """
        Obtiene las observaciones medicas.
        
        Returns:
            Observaciones medicas
        """
        return self._observaciones
    
    def set_observaciones(self, observaciones: str) -> None:
        """
        Establece las observaciones medicas.
        
        Args:
            observaciones: Nuevas observaciones medicas
        """
        self._observaciones = observaciones

# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/personal/herramienta.py
# ================================================================================

"""
Modulo que define la entidad Herramienta.

Este modulo contiene la clase Herramienta, que representa una herramienta
de trabajo agricola en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/personal/herramienta.py
"""


class Herramienta:
    """
    Entidad que representa una herramienta de trabajo agricola.
    
    Una Herramienta es un utensilio usado por trabajadores para realizar
    tareas agricolas. Debe tener certificacion de higiene y seguridad (H&S).
    
    Attributes:
        _id_herramienta: Identificador unico de la herramienta
        _nombre: Nombre de la herramienta
        _certificado_hys: Indica si tiene certificado de higiene y seguridad
    """
    
    def __init__(self, id_herramienta: int, nombre: str, certificado_hys: bool):
        """
        Inicializa una Herramienta con ID, nombre y certificacion.
        
        Args:
            id_herramienta: Identificador unico de la herramienta
            nombre: Nombre de la herramienta
            certificado_hys: True si tiene certificado H&S, False en caso contrario
            
        Raises:
            ValueError: Si id_herramienta <= 0 o nombre esta vacio
        """
        if id_herramienta <= 0:
            raise ValueError("El ID de la herramienta debe ser un numero positivo")
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        
        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_id_herramienta(self) -> int:
        """
        Obtiene el ID de la herramienta.
        
        Returns:
            ID de la herramienta
        """
        return self._id_herramienta
    
    def set_id_herramienta(self, id_herramienta: int) -> None:
        """
        Establece el ID de la herramienta.
        
        Args:
            id_herramienta: Nuevo ID de la herramienta
            
        Raises:
            ValueError: Si id_herramienta <= 0
        """
        if id_herramienta <= 0:
            raise ValueError("El ID de la herramienta debe ser un numero positivo")
        self._id_herramienta = id_herramienta
    
    def get_nombre(self) -> str:
        """
        Obtiene el nombre de la herramienta.
        
        Returns:
            Nombre de la herramienta
        """
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre de la herramienta.
        
        Args:
            nombre: Nuevo nombre de la herramienta
            
        Raises:
            ValueError: Si nombre esta vacio
        """
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = nombre
    
    def tiene_certificado_hys(self) -> bool:
        """
        Verifica si la herramienta tiene certificado H&S.
        
        Returns:
            True si tiene certificado, False en caso contrario
        """
        return self._certificado_hys
    
    def set_certificado_hys(self, certificado_hys: bool) -> None:
        """
        Establece si la herramienta tiene certificado H&S.
        
        Args:
            certificado_hys: True si tiene certificado, False en caso contrario
        """
        self._certificado_hys = certificado_hys

# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/personal/tarea.py
# ================================================================================

"""
Modulo que define la entidad Tarea.

Este modulo contiene la clase Tarea, que representa una tarea agricola
asignada a un trabajador en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/personal/tarea.py
"""

from datetime import date


class Tarea:
    """
    Entidad que representa una tarea agricola.
    
    Una Tarea es una actividad asignada a un trabajador con fecha programada
    y descripcion. Puede estar pendiente o completada.
    
    Attributes:
        _id: Identificador unico de la tarea
        _fecha: Fecha programada para realizar la tarea
        _descripcion: Descripcion de la tarea a realizar
        _completada: Estado de la tarea (True si esta completada)
    """
    
    def __init__(self, id_tarea: int, fecha: date, descripcion: str):
        """
        Inicializa una Tarea con ID, fecha y descripcion.
        
        Args:
            id_tarea: Identificador unico de la tarea
            fecha: Fecha programada para la tarea
            descripcion: Descripcion de la tarea
            
        Raises:
            ValueError: Si id_tarea <= 0 o descripcion esta vacia
        """
        if id_tarea <= 0:
            raise ValueError("El ID de la tarea debe ser un numero positivo")
        if not descripcion or descripcion.strip() == "":
            raise ValueError("La descripcion no puede estar vacia")
        
        self._id = id_tarea
        self._fecha = fecha
        self._descripcion = descripcion
        self._completada = False
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_id(self) -> int:
        """
        Obtiene el ID de la tarea.
        
        Returns:
            ID de la tarea
        """
        return self._id
    
    def set_id(self, id_tarea: int) -> None:
        """
        Establece el ID de la tarea.
        
        Args:
            id_tarea: Nuevo ID de la tarea
            
        Raises:
            ValueError: Si id_tarea <= 0
        """
        if id_tarea <= 0:
            raise ValueError("El ID de la tarea debe ser un numero positivo")
        self._id = id_tarea
    
    def get_fecha(self) -> date:
        """
        Obtiene la fecha programada de la tarea.
        
        Returns:
            Fecha de la tarea
        """
        return self._fecha
    
    def set_fecha(self, fecha: date) -> None:
        """
        Establece la fecha programada de la tarea.
        
        Args:
            fecha: Nueva fecha de la tarea
        """
        self._fecha = fecha
    
    def get_descripcion(self) -> str:
        """
        Obtiene la descripcion de la tarea.
        
        Returns:
            Descripcion de la tarea
        """
        return self._descripcion
    
    def set_descripcion(self, descripcion: str) -> None:
        """
        Establece la descripcion de la tarea.
        
        Args:
            descripcion: Nueva descripcion de la tarea
            
        Raises:
            ValueError: Si descripcion esta vacia
        """
        if not descripcion or descripcion.strip() == "":
            raise ValueError("La descripcion no puede estar vacia")
        self._descripcion = descripcion
    
    def esta_completada(self) -> bool:
        """
        Verifica si la tarea esta completada.
        
        Returns:
            True si la tarea esta completada, False en caso contrario
        """
        return self._completada
    
    def marcar_completada(self) -> None:
        """
        Marca la tarea como completada.
        """
        self._completada = True
    
    def marcar_pendiente(self) -> None:
        """
        Marca la tarea como pendiente.
        """
        self._completada = False

# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

"""
Modulo que define la entidad Trabajador.

Este modulo contiene la clase Trabajador, que representa un trabajador agricola
en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/personal/trabajador.py
"""

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.tarea import Tarea
    from python_forestacion.entidades.personal.apto_medico import AptoMedico


class Trabajador:
    """
    Entidad que representa un trabajador agricola.
    
    Un Trabajador es una persona asignada a realizar tareas agricolas en
    una plantacion. Tiene DNI unico, nombre, lista de tareas asignadas
    y certificacion de apto medico.
    
    Attributes:
        _dni: Documento Nacional de Identidad (unico)
        _nombre: Nombre completo del trabajador
        _tareas: Lista de tareas asignadas al trabajador
        _apto_medico: Certificacion medica del trabajador (opcional)
    """
    
    def __init__(self, dni: int, nombre: str, tareas: List['Tarea']):
        """
        Inicializa un Trabajador con DNI, nombre y tareas.
        
        Args:
            dni: Documento Nacional de Identidad (debe ser positivo)
            nombre: Nombre completo del trabajador
            tareas: Lista de tareas asignadas
            
        Raises:
            ValueError: Si dni <= 0 o nombre esta vacio
        """
        if dni <= 0:
            raise ValueError("El DNI debe ser un numero positivo")
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas.copy()  # Defensive copy
        self._apto_medico: 'AptoMedico' = None
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_dni(self) -> int:
        """
        Obtiene el DNI del trabajador.
        
        Returns:
            DNI del trabajador
        """
        return self._dni
    
    def set_dni(self, dni: int) -> None:
        """
        Establece el DNI del trabajador.
        
        Args:
            dni: Nuevo DNI del trabajador
            
        Raises:
            ValueError: Si dni <= 0
        """
        if dni <= 0:
            raise ValueError("El DNI debe ser un numero positivo")
        self._dni = dni
    
    def get_nombre(self) -> str:
        """
        Obtiene el nombre del trabajador.
        
        Returns:
            Nombre completo del trabajador
        """
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre del trabajador.
        
        Args:
            nombre: Nuevo nombre del trabajador
            
        Raises:
            ValueError: Si nombre esta vacio
        """
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = nombre
    
    def get_tareas(self) -> List['Tarea']:
        """
        Obtiene la lista de tareas asignadas.
        
        Returns:
            Copia de la lista de tareas (defensive copy)
        """
        return self._tareas.copy()
    
    def set_tareas(self, tareas: List['Tarea']) -> None:
        """
        Establece la lista de tareas asignadas.
        
        Args:
            tareas: Nueva lista de tareas
        """
        self._tareas = tareas.copy()
    
    def agregar_tarea(self, tarea: 'Tarea') -> None:
        """
        Agrega una tarea a la lista del trabajador.
        
        Args:
            tarea: Tarea a agregar
        """
        self._tareas.append(tarea)
    
    def get_apto_medico(self) -> 'AptoMedico':
        """
        Obtiene el apto medico del trabajador.
        
        Returns:
            AptoMedico o None si no tiene
        """
        return self._apto_medico
    
    def set_apto_medico(self, apto_medico: 'AptoMedico') -> None:
        """
        Establece el apto medico del trabajador.
        
        Args:
            apto_medico: Nueva certificacion medica
        """
        self._apto_medico = apto_medico

