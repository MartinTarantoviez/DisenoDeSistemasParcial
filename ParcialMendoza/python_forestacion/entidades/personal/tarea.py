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