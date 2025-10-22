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