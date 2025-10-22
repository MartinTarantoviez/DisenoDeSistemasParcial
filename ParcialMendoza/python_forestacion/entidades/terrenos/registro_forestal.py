"""
Modulo que define la entidad RegistroForestal.

Este modulo contiene la clase RegistroForestal, que representa un registro
catastral completo que vincula tierra, plantacion, propietario y avaluo.

Ubicacion: python_forestacion/entidades/terrenos/registro_forestal.py
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:
    """
    Entidad que representa un registro forestal completo.
    
    El RegistroForestal vincula un terreno (Tierra) con su plantacion (Plantacion),
    propietario y avaluo fiscal. Es la entidad principal que se persiste en disco.
    
    Attributes:
        _id_padron: Numero de padron catastral del registro
        _tierra: Terreno catastral asociado
        _plantacion: Plantacion agricola asociada
        _propietario: Nombre del propietario del terreno
        _avaluo: Avaluo fiscal del terreno
    """
    
    def __init__(
        self,
        id_padron: int,
        tierra: 'Tierra',
        plantacion: 'Plantacion',
        propietario: str,
        avaluo: float
    ):
        """
        Inicializa un RegistroForestal con todos sus datos.
        
        Args:
            id_padron: Numero de padron catastral
            tierra: Terreno catastral
            plantacion: Plantacion agricola
            propietario: Nombre del propietario
            avaluo: Avaluo fiscal del terreno
            
        Raises:
            ValueError: Si id_padron <= 0, avaluo < 0 o propietario esta vacio
        """
        if id_padron <= 0:
            raise ValueError("El padron debe ser un numero positivo")
        if avaluo < 0:
            raise ValueError("El avaluo no puede ser negativo")
        if not propietario or propietario.strip() == "":
            raise ValueError("El propietario no puede estar vacio")
        
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_id_padron(self) -> int:
        """
        Obtiene el numero de padron catastral.
        
        Returns:
            Numero de padron
        """
        return self._id_padron
    
    def set_id_padron(self, id_padron: int) -> None:
        """
        Establece el numero de padron catastral.
        
        Args:
            id_padron: Nuevo numero de padron
            
        Raises:
            ValueError: Si id_padron <= 0
        """
        if id_padron <= 0:
            raise ValueError("El padron debe ser un numero positivo")
        self._id_padron = id_padron
    
    def get_tierra(self) -> 'Tierra':
        """
        Obtiene el terreno catastral.
        
        Returns:
            Terreno asociado
        """
        return self._tierra
    
    def set_tierra(self, tierra: 'Tierra') -> None:
        """
        Establece el terreno catastral.
        
        Args:
            tierra: Nuevo terreno
        """
        self._tierra = tierra
    
    def get_plantacion(self) -> 'Plantacion':
        """
        Obtiene la plantacion agricola.
        
        Returns:
            Plantacion asociada
        """
        return self._plantacion
    
    def set_plantacion(self, plantacion: 'Plantacion') -> None:
        """
        Establece la plantacion agricola.
        
        Args:
            plantacion: Nueva plantacion
        """
        self._plantacion = plantacion
    
    def get_propietario(self) -> str:
        """
        Obtiene el nombre del propietario.
        
        Returns:
            Nombre del propietario
        """
        return self._propietario
    
    def set_propietario(self, propietario: str) -> None:
        """
        Establece el nombre del propietario.
        
        Args:
            propietario: Nuevo nombre del propietario
            
        Raises:
            ValueError: Si propietario esta vacio
        """
        if not propietario or propietario.strip() == "":
            raise ValueError("El propietario no puede estar vacio")
        self._propietario = propietario
    
    def get_avaluo(self) -> float:
        """
        Obtiene el avaluo fiscal.
        
        Returns:
            Avaluo fiscal
        """
        return self._avaluo
    
    def set_avaluo(self, avaluo: float) -> None:
        """
        Establece el avaluo fiscal.
        
        Args:
            avaluo: Nuevo avaluo fiscal
            
        Raises:
            ValueError: Si avaluo < 0
        """
        if avaluo < 0:
            raise ValueError("El avaluo no puede ser negativo")
        self._avaluo = avaluo