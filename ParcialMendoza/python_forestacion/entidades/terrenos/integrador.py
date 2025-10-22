"""
Archivo integrador generado automaticamente
Directorio: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/terrenos
Fecha: 2025-10-22 01:16:07
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/terrenos/plantacion.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/terrenos/registro_forestal.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/terrenos/tierra.py
# ================================================================================

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

