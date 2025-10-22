"""
Archivo integrador generado automaticamente
Directorio: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos
Fecha: 2025-10-22 01:16:07
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/arbol.py
# ================================================================================

"""
Modulo que define la clase base Arbol.

Este modulo contiene la clase abstracta Arbol que sirve como base
para todos los cultivos arboreos del sistema (Pino, Olivo).

Ubicacion: python_forestacion/entidades/cultivos/arbol.py
"""

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

from python_forestacion.constantes import ALTURA_INICIAL_ARBOL


class Arbol(ABC):
    """
    Clase base para cultivos arboreos.
    
    Los arboles tienen caracteristicas especiales como altura y crecimiento.
    Esta clase hereda de Cultivo y agrega funcionalidad especifica de arboles.
    
    Attributes:
        _altura: Altura del arbol en metros
        _id: Identificador unico del arbol
    """
    
    _contador_id = 0
    """Contador estatico para generar IDs unicos."""
    
    def __init__(self, agua: int, superficie: float, altura: float = ALTURA_INICIAL_ARBOL):
        """
        Inicializa un arbol con agua, superficie y altura.
        
        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie ocupada en metros cuadrados
            altura: Altura inicial del arbol en metros (default: ALTURA_INICIAL_ARBOL)
            
        Raises:
            ValueError: Si altura <= 0
        """
        # Nota: No llamamos a super().__init__() porque Python usa MRO
        # Las subclases concretas (Pino, Olivo) llamaran a Cultivo.__init__()
        
        if altura <= 0:
            raise ValueError("La altura debe ser mayor a cero")
        
        self._altura = altura
        
        # Asignar ID unico
        Arbol._contador_id += 1
        self._id = Arbol._contador_id
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_altura(self) -> float:
        """
        Obtiene la altura del arbol.
        
        Returns:
            Altura en metros
        """
        return self._altura
    
    def set_altura(self, altura: float) -> None:
        """
        Establece la altura del arbol.
        
        Args:
            altura: Nueva altura en metros
            
        Raises:
            ValueError: Si altura <= 0
        """
        if altura <= 0:
            raise ValueError("La altura debe ser mayor a cero")
        self._altura = altura
    
    def get_id(self) -> int:
        """
        Obtiene el ID unico del arbol.
        
        Returns:
            ID del arbol
        """
        return self._id

# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/cultivo.py
# ================================================================================

"""
Modulo que define la interfaz base Cultivo.

Este modulo contiene la clase abstracta Cultivo que sirve como base
para todos los tipos de cultivos del sistema (arboles y hortalizas).

Ubicacion: python_forestacion/entidades/cultivos/cultivo.py
"""

from abc import ABC, abstractmethod


class Cultivo(ABC):
    """
    Interfaz base para todos los cultivos del sistema.
    
    Esta clase abstracta define los atributos y metodos comunes
    que deben implementar todos los cultivos (Pino, Olivo, Lechuga, Zanahoria).
    
    Attributes:
        _agua: Cantidad de agua almacenada en litros
        _superficie: Superficie ocupada por el cultivo en metros cuadrados
    """
    
    def __init__(self, agua: int, superficie: float):
        """
        Inicializa un cultivo con agua y superficie.
        
        Args:
            agua: Cantidad inicial de agua en litros (debe ser >= 0)
            superficie: Superficie ocupada en metros cuadrados (debe ser > 0)
            
        Raises:
            ValueError: Si agua < 0 o superficie <= 0
        """
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
            
        self._agua = agua
        self._superficie = superficie
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_agua(self) -> int:
        """
        Obtiene la cantidad de agua almacenada.
        
        Returns:
            Cantidad de agua en litros
        """
        return self._agua
    
    def set_agua(self, agua: int) -> None:
        """
        Establece la cantidad de agua almacenada.
        
        Args:
            agua: Nueva cantidad de agua en litros
            
        Raises:
            ValueError: Si agua < 0
        """
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        self._agua = agua
    
    def get_superficie(self) -> float:
        """
        Obtiene la superficie ocupada por el cultivo.
        
        Returns:
            Superficie en metros cuadrados
        """
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie ocupada por el cultivo.
        
        Args:
            superficie: Nueva superficie en metros cuadrados
            
        Raises:
            ValueError: Si superficie <= 0
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie
    
    # ========================================================================
    # METODOS ABSTRACTOS
    # ========================================================================
    
    @abstractmethod
    def __str__(self) -> str:
        """
        Representacion en cadena del cultivo.
        
        Returns:
            Nombre del tipo de cultivo
        """
        pass

# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/hortaliza.py
# ================================================================================

"""
Modulo que define la clase base Hortaliza.

Este modulo contiene la clase abstracta Hortaliza que sirve como base
para todos los cultivos horticolas del sistema (Lechuga, Zanahoria).

Ubicacion: python_forestacion/entidades/cultivos/hortaliza.py
"""

from abc import ABC


class Hortaliza(ABC):
    """
    Clase base para cultivos horticolas.
    
    Las hortalizas tienen caracteristicas especiales como el cultivo
    en invernadero. Esta clase hereda de Cultivo y agrega funcionalidad
    especifica de hortalizas.
    
    Attributes:
        _invernadero: Indica si la hortaliza se cultiva en invernadero
    """
    
    def __init__(self, agua: int, superficie: float, invernadero: bool):
        """
        Inicializa una hortaliza con agua, superficie e invernadero.
        
        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie ocupada en metros cuadrados
            invernadero: True si se cultiva en invernadero, False en caso contrario
        """
        # Nota: No llamamos a super().__init__() porque Python usa MRO
        # Las subclases concretas (Lechuga, Zanahoria) llamaran a Cultivo.__init__()
        
        self._invernadero = invernadero
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def es_de_invernadero(self) -> bool:
        """
        Verifica si la hortaliza se cultiva en invernadero.
        
        Returns:
            True si es de invernadero, False en caso contrario
        """
        return self._invernadero
    
    def set_invernadero(self, invernadero: bool) -> None:
        """
        Establece si la hortaliza se cultiva en invernadero.
        
        Args:
            invernadero: True para invernadero, False para campo abierto
        """
        self._invernadero = invernadero

# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/lechuga.py
# ================================================================================

"""
Modulo que define la entidad Lechuga.

Este modulo contiene la clase Lechuga, que representa una hortaliza de tipo lechuga
en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/cultivos/lechuga.py
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_LECHUGA,
    SUPERFICIE_LECHUGA,
    VARIEDAD_LECHUGA_DEFAULT
)


class Lechuga(Cultivo, Hortaliza):
    """
    Entidad que representa una hortaliza de tipo Lechuga.
    
    La Lechuga es una hortaliza de hoja verde que se cultiva en invernadero,
    requiere 0.10m² de superficie y absorbe agua de forma constante (1L).
    
    Attributes:
        _variedad: Variedad de la lechuga (Crespa, Mantecosa, Morada, etc.)
    """
    
    def __init__(self, variedad: str = VARIEDAD_LECHUGA_DEFAULT):
        """
        Inicializa una Lechuga con variedad especifica.
        
        Args:
            variedad: Variedad de la lechuga (default: VARIEDAD_LECHUGA_DEFAULT)
        """
        # Inicializar Cultivo (agua y superficie)
        Cultivo.__init__(self, AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA)
        
        # Inicializar Hortaliza (siempre en invernadero)
        Hortaliza.__init__(self, AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA, invernadero=True)
        
        # Atributos propios
        self._variedad = variedad
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_variedad(self) -> str:
        """
        Obtiene la variedad de la lechuga.
        
        Returns:
            Variedad de la lechuga
        """
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        """
        Establece la variedad de la lechuga.
        
        Args:
            variedad: Nueva variedad de la lechuga
        """
        self._variedad = variedad
    
    # ========================================================================
    # METODOS HEREDADOS
    # ========================================================================
    
    def __str__(self) -> str:
        """
        Representacion en cadena de la lechuga.
        
        Returns:
            Nombre del tipo de cultivo
        """
        return "Lechuga"

# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/olivo.py
# ================================================================================

"""
Modulo que define la entidad Olivo.

Este modulo contiene la clase Olivo, que representa un arbol de tipo olivo
en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/cultivos/olivo.py
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import (
    AGUA_INICIAL_OLIVO,
    SUPERFICIE_OLIVO,
    ALTURA_INICIAL_OLIVO
)


class Olivo(Cultivo, Arbol):
    """
    Entidad que representa un arbol de tipo Olivo.
    
    El Olivo es un arbol frutal que produce aceitunas, requiere 3m² de superficie,
    crece en altura al recibir agua (mas lento que el pino) y absorbe agua
    de forma estacional.
    
    Attributes:
        _tipo_aceituna: Tipo de aceituna que produce (Arbequina, Picual, Manzanilla)
    """
    
    def __init__(self, tipo_aceituna: TipoAceituna = TipoAceituna.ARBEQUINA):
        """
        Inicializa un Olivo con tipo de aceituna especifico.
        
        Args:
            tipo_aceituna: Tipo de aceituna del olivo (default: TipoAceituna.ARBEQUINA)
        """
        # Inicializar Cultivo (agua y superficie)
        Cultivo.__init__(self, AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO)
        
        # Inicializar Arbol (altura - los olivos son mas bajos inicialmente)
        Arbol.__init__(self, AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO, ALTURA_INICIAL_OLIVO)
        
        # Atributos propios
        self._tipo_aceituna = tipo_aceituna
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_tipo_aceituna(self) -> TipoAceituna:
        """
        Obtiene el tipo de aceituna del olivo.
        
        Returns:
            Tipo de aceituna (enum)
        """
        return self._tipo_aceituna
    
    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        """
        Establece el tipo de aceituna del olivo.
        
        Args:
            tipo_aceituna: Nuevo tipo de aceituna
        """
        self._tipo_aceituna = tipo_aceituna
    
    # ========================================================================
    # METODOS HEREDADOS
    # ========================================================================
    
    def __str__(self) -> str:
        """
        Representacion en cadena del olivo.
        
        Returns:
            Nombre del tipo de cultivo
        """
        return "Olivo"

# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/pino.py
# ================================================================================

"""
Modulo que define la entidad Pino.

Este modulo contiene la clase Pino, que representa un arbol de tipo pino
en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/cultivos/pino.py
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import (
    AGUA_INICIAL_PINO,
    SUPERFICIE_PINO,
    ALTURA_INICIAL_ARBOL,
    VARIEDAD_PINO_DEFAULT
)


class Pino(Cultivo, Arbol):
    """
    Entidad que representa un arbol de tipo Pino.
    
    El Pino es un arbol maderable que requiere 2m² de superficie,
    crece en altura al recibir agua y absorbe agua de forma estacional.
    
    Attributes:
        _variedad: Variedad del pino (Parana, Elliott, Taeda, etc.)
    """
    
    def __init__(self, variedad: str = VARIEDAD_PINO_DEFAULT):
        """
        Inicializa un Pino con variedad especifica.
        
        Args:
            variedad: Variedad del pino (default: VARIEDAD_PINO_DEFAULT)
        """
        # Inicializar Cultivo (agua y superficie)
        Cultivo.__init__(self, AGUA_INICIAL_PINO, SUPERFICIE_PINO)
        
        # Inicializar Arbol (altura)
        Arbol.__init__(self, AGUA_INICIAL_PINO, SUPERFICIE_PINO, ALTURA_INICIAL_ARBOL)
        
        # Atributos propios
        self._variedad = variedad
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def get_variedad(self) -> str:
        """
        Obtiene la variedad del pino.
        
        Returns:
            Variedad del pino
        """
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        """
        Establece la variedad del pino.
        
        Args:
            variedad: Nueva variedad del pino
        """
        self._variedad = variedad
    
    # ========================================================================
    # METODOS HEREDADOS
    # ========================================================================
    
    def __str__(self) -> str:
        """
        Representacion en cadena del pino.
        
        Returns:
            Nombre del tipo de cultivo
        """
        return "Pino"

# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ================================================================================

"""
Modulo que define el enum TipoAceituna.

Este modulo contiene la enumeracion de tipos de aceitunas
disponibles para los olivos.

Ubicacion: python_forestacion/entidades/cultivos/tipo_aceituna.py
"""

from enum import Enum


class TipoAceituna(Enum):
    """
    Enumeracion de tipos de aceitunas.
    
    Define los tipos de aceitunas que pueden tener los olivos.
    """
    
    ARBEQUINA = "Arbequina"
    """Aceituna tipo Arbequina."""
    
    PICUAL = "Picual"
    """Aceituna tipo Picual."""
    
    MANZANILLA = "Manzanilla"
    """Aceituna tipo Manzanilla."""

# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/zanahoria.py
# ================================================================================

"""
Modulo que define la entidad Zanahoria.

Este modulo contiene la clase Zanahoria, que representa una hortaliza de tipo zanahoria
en el sistema de gestion forestal.

Ubicacion: python_forestacion/entidades/cultivos/zanahoria.py
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_ZANAHORIA,
    SUPERFICIE_ZANAHORIA
)


class Zanahoria(Cultivo, Hortaliza):
    """
    Entidad que representa una hortaliza de tipo Zanahoria.
    
    La Zanahoria es una hortaliza de raiz que se cultiva a campo abierto,
    requiere 0.15m² de superficie, comienza sin agua (0L) y absorbe agua
    de forma constante (2L).
    
    Attributes:
        _baby_carrot: Indica si es una baby carrot (True) o zanahoria regular (False)
    """
    
    def __init__(self, baby_carrot: bool = False):
        """
        Inicializa una Zanahoria especificando si es baby carrot.
        
        Args:
            baby_carrot: True si es baby carrot, False si es zanahoria regular
        """
        # Inicializar Cultivo (agua y superficie)
        Cultivo.__init__(self, AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA)
        
        # Inicializar Hortaliza (NO es de invernadero)
        Hortaliza.__init__(self, AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA, invernadero=False)
        
        # Atributos propios
        self._baby_carrot = baby_carrot
    
    # ========================================================================
    # GETTERS Y SETTERS
    # ========================================================================
    
    def is_baby_carrot(self) -> bool:
        """
        Verifica si es una baby carrot.
        
        Returns:
            True si es baby carrot, False si es zanahoria regular
        """
        return self._baby_carrot
    
    def set_baby_carrot(self, baby_carrot: bool) -> None:
        """
        Establece si es una baby carrot.
        
        Args:
            baby_carrot: True para baby carrot, False para zanahoria regular
        """
        self._baby_carrot = baby_carrot
    
    # ========================================================================
    # METODOS HEREDADOS
    # ========================================================================
    
    def __str__(self) -> str:
        """
        Representacion en cadena de la zanahoria.
        
        Returns:
            Nombre del tipo de cultivo
        """
        return "Zanahoria"

