"""
Modulo que define la entidad Plantacion.

Este modulo contiene la clase Plantacion, que representa una finca agricola
con cultivos y trabajadores en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/terrenos/plantacion.py
"""

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador

from python_forestacion.constantes import AGUA_INICIAL_PLANTACION


class Plantacion:
    """
    Entidad que representa una plantacion agricola.
    
    La Plantacion es una finca que contiene cultivos, trabajadores,
    controla la superficie ocupada vs disponible y gestiona el agua
    disponible para riego.
    
    Attributes:
        _nombre: Nombre identificatorio de la plantacion
        _superficie: Superficie maxima disponible en metros cuadrados
        _agua_disponible: Agua disponible para riego en litros
        _cultivos: Lista de cultivos plantados
        _trabajadores: Lista de trabajadores asignados
        _superficie_ocupada: Superficie actualmente ocupada por cultivos
    """
    
    def __init__(
        self,
        nombre: str,
        superficie: float,
        agua: int = AGUA_INICIAL_PLANTACION
    ):
        """
        Inicializa una Plantacion con nombre, superficie y agua inicial.
        
        Args:
            nombre: Nombre identificatorio de la plantacion
            superficie: Superficie maxima disponible en metros cuadrados
            agua: Agua inicial disponible en litros (default: AGUA_INICIAL_PLANTACION)
            
        Raises:
            ValueError: Si superficie <= 0 o agua < 0
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        
        self._nombre = nombre
        self._superficie = superficie
        self._agua_disponible = agua
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []
        self._superficie_ocupada = 0.0
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_nombre(self) -> str:
        """
        Obtiene el nombre de la plantacion.
        
        Returns:
            Nombre de la plantacion
        """
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre de la plantacion.
        
        Args:
            nombre: Nuevo nombre de la plantacion
        """
        self._nombre = nombre
    
    def get_superficie(self) -> float:
        """
        Obtiene la superficie maxima disponible.
        
        Returns:
            Superficie maxima en metros cuadrados
        """
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie maxima disponible.
        
        Args:
            superficie: Nueva superficie maxima en metros cuadrados
            
        Raises:
            ValueError: Si superficie <= 0
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie
    
    def get_agua_disponible(self) -> int:
        """
        Obtiene el agua disponible para riego.
        
        Returns:
            Agua disponible en litros
        """
        return self._agua_disponible
    
    def set_agua_disponible(self, agua: int) -> None:
        """
        Establece el agua disponible para riego.
        
        Args:
            agua: Nueva cantidad de agua disponible en litros
            
        Raises:
            ValueError: Si agua < 0
        """
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        self._agua_disponible = agua
    
    def get_cultivos(self) -> List['Cultivo']:
        """
        Obtiene la lista de cultivos plantados.
        
        Returns:
            Copia de la lista de cultivos (defensive copy)
        """
        return self._cultivos.copy()
    
    def set_cultivos(self, cultivos: List['Cultivo']) -> None:
        """
        Establece la lista de cultivos plantados.
        
        Args:
            cultivos: Nueva lista de cultivos
        """
        self._cultivos = cultivos.copy()
    
    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        """
        Agrega un cultivo a la plantacion.
        
        Args:
            cultivo: Cultivo a agregar
        """
        self._cultivos.append(cultivo)
        self._superficie_ocupada += cultivo.get_superficie()
    
    def eliminar_cultivo(self, cultivo: 'Cultivo') -> None:
        """
        Elimina un cultivo de la plantacion.
        
        Args:
            cultivo: Cultivo a eliminar
        """
        if cultivo in self._cultivos:
            self._cultivos.remove(cultivo)
            self._superficie_ocupada -= cultivo.get_superficie()
    
    def get_trabajadores(self) -> List['Trabajador']:
        """
        Obtiene la lista de trabajadores asignados.
        
        Returns:
            Copia de la lista de trabajadores (defensive copy)
        """
        return self._trabajadores.copy()
    
    def set_trabajadores(self, trabajadores: List['Trabajador']) -> None:
        """
        Establece la lista de trabajadores asignados.
        
        Args:
            trabajadores: Nueva lista de trabajadores
        """
        self._trabajadores = trabajadores.copy()
    
    def get_superficie_ocupada(self) -> float:
        """
        Obtiene la superficie actualmente ocupada por cultivos.
        
        Returns:
            Superficie ocupada en metros cuadrados
        """
        return self._superficie_ocupada
    
    def get_superficie_disponible(self) -> float:
        """
        Calcula la superficie disponible para nuevos cultivos.
        
        Returns:
            Superficie disponible en metros cuadrados
        """
        return self._superficie - self._superficie_ocupada