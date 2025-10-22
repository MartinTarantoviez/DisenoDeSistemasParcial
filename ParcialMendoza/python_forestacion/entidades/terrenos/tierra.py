"""
Modulo que define la entidad Tierra.

Este modulo contiene la clase Tierra, que representa un terreno catastral
en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/terrenos/tierra.py
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:
    """
    Entidad que representa un terreno catastral.
    
    La Tierra es un terreno registrado con padron catastral unico,
    superficie y domicilio. Puede tener una plantacion (finca) asociada.
    
    Attributes:
        _id_padron_catastral: Numero de padron catastral unico
        _superficie: Superficie del terreno en metros cuadrados
        _domicilio: Domicilio de ubicacion del terreno
        _finca: Plantacion asociada al terreno (opcional)
    """
    
    def __init__(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        finca: 'Plantacion' = None
    ):
        """
        Inicializa una Tierra con sus datos catastrales.
        
        Args:
            id_padron_catastral: Numero de padron catastral (debe ser positivo)
            superficie: Superficie en metros cuadrados (debe ser > 0)
            domicilio: Domicilio de ubicacion
            finca: Plantacion asociada (opcional)
            
        Raises:
            ValueError: Si id_padron_catastral <= 0 o superficie <= 0
        """
        if id_padron_catastral <= 0:
            raise ValueError("El padron catastral debe ser un numero positivo")
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        
        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca = finca
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_id_padron_catastral(self) -> int:
        """
        Obtiene el numero de padron catastral.
        
        Returns:
            Numero de padron catastral
        """
        return self._id_padron_catastral
    
    def set_id_padron_catastral(self, id_padron_catastral: int) -> None:
        """
        Establece el numero de padron catastral.
        
        Args:
            id_padron_catastral: Nuevo numero de padron catastral
            
        Raises:
            ValueError: Si id_padron_catastral <= 0
        """
        if id_padron_catastral <= 0:
            raise ValueError("El padron catastral debe ser un numero positivo")
        self._id_padron_catastral = id_padron_catastral
    
    def get_superficie(self) -> float:
        """
        Obtiene la superficie del terreno.
        
        Returns:
            Superficie en metros cuadrados
        """
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie del terreno.
        
        Args:
            superficie: Nueva superficie en metros cuadrados
            
        Raises:
            ValueError: Si superficie <= 0
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie
    
    def get_domicilio(self) -> str:
        """
        Obtiene el domicilio del terreno.
        
        Returns:
            Domicilio de ubicacion
        """
        return self._domicilio
    
    def set_domicilio(self, domicilio: str) -> None:
        """
        Establece el domicilio del terreno.
        
        Args:
            domicilio: Nuevo domicilio de ubicacion
        """
        self._domicilio = domicilio
    
    def get_finca(self) -> 'Plantacion':
        """
        Obtiene la plantacion asociada al terreno.
        
        Returns:
            Plantacion asociada o None si no tiene
        """
        return self._finca
    
    def set_finca(self, finca: 'Plantacion') -> None:
        """
        Establece la plantacion asociada al terreno.
        
        Args:
            finca: Plantacion a asociar
        """
        self._finca = finca