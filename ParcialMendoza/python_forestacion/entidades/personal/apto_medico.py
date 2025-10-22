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