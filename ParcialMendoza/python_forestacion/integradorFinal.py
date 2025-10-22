"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion
Fecha de generacion: 2025-10-22 01:16:07
Total de archivos integrados: 61
Total de directorios procesados: 19
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#
# DIRECTORIO: entidades/cultivos
#   4. __init__.py
#   5. arbol.py
#   6. cultivo.py
#   7. hortaliza.py
#   8. lechuga.py
#   9. olivo.py
#   10. pino.py
#   11. tipo_aceituna.py
#   12. zanahoria.py
#
# DIRECTORIO: entidades/personal
#   13. __init__.py
#   14. apto_medico.py
#   15. herramienta.py
#   16. tarea.py
#   17. trabajador.py
#
# DIRECTORIO: entidades/terrenos
#   18. __init__.py
#   19. plantacion.py
#   20. registro_forestal.py
#   21. tierra.py
#
# DIRECTORIO: excepciones
#   22. __init__.py
#   23. agua_agotada_exception.py
#   24. forestacion_exception.py
#   25. mensajes_exception.py
#   26. persistencia_exception.py
#   27. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   28. __init__.py
#
# DIRECTORIO: patrones/factory
#   29. __init__.py
#   30. cultivo_factory.py
#
# DIRECTORIO: patrones/observer
#   31. __init__.py
#   32. observable.py
#   33. observer.py
#
# DIRECTORIO: patrones/strategy
#   34. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   35. __init__.py
#   36. absorcion_constante_strategy.py
#   37. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   38. __init__.py
#
# DIRECTORIO: riego/control
#   39. __init__.py
#   40. control_riego_task.py
#
# DIRECTORIO: riego/sensores
#   41. __init__.py
#   42. humedad_reader_task.py
#   43. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   44. __init__.py
#
# DIRECTORIO: servicios/cultivos
#   45. __init__.py
#   46. arbol_service.py
#   47. cultivo_service.py
#   48. cultivo_service_registry.py
#   49. lechuga_service.py
#   50. olivo_service.py
#   51. pino_service.py
#   52. zanahoria_service.py
#
# DIRECTORIO: servicios/negocio
#   53. __init__.py
#   54. fincas_service.py
#   55. paquete.py
#
# DIRECTORIO: servicios/personal
#   56. __init__.py
#   57. trabajador_service.py
#
# DIRECTORIO: servicios/terrenos
#   58. __init__.py
#   59. plantacion_service.py
#   60. registro_forestal_service.py
#   61. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/61: __init__.py
# Directorio: .
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/61: constantes.py
# Directorio: .
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/constantes.py
# ==============================================================================

"""
Modulo de constantes centralizadas del sistema.

Este modulo contiene todas las constantes magicas del sistema, eliminando
valores hardcodeados y facilitando el mantenimiento.

Ubicacion: python_forestacion/constantes.py

Autor: Sistema de Gestion Forestal
Version: 1.0.0
"""

# ============================================================================
# CONSTANTES DE AGUA
# ============================================================================

AGUA_MINIMA = 10
"""Agua minima requerida para realizar un riego (litros)."""

AGUA_INICIAL_PLANTACION = 500
"""Agua disponible inicial en una plantacion (litros)."""

AGUA_CONSUMIDA_POR_RIEGO = 10
"""Cantidad de agua consumida en cada riego (litros)."""

# ============================================================================
# CONSTANTES DE CULTIVOS - PINO
# ============================================================================

SUPERFICIE_PINO = 2.0
"""Superficie requerida por pino (metros cuadrados)."""

AGUA_INICIAL_PINO = 2
"""Agua inicial de un pino (litros)."""

VARIEDAD_PINO_DEFAULT = "Parana"
"""Variedad por defecto de pino."""

# ============================================================================
# CONSTANTES DE CULTIVOS - OLIVO
# ============================================================================

SUPERFICIE_OLIVO = 3.0
"""Superficie requerida por olivo (metros cuadrados)."""

AGUA_INICIAL_OLIVO = 5
"""Agua inicial de un olivo (litros)."""

# ============================================================================
# CONSTANTES DE CULTIVOS - LECHUGA
# ============================================================================

SUPERFICIE_LECHUGA = 0.10
"""Superficie requerida por lechuga (metros cuadrados)."""

AGUA_INICIAL_LECHUGA = 1
"""Agua inicial de una lechuga (litros)."""

VARIEDAD_LECHUGA_DEFAULT = "Crespa"
"""Variedad por defecto de lechuga."""

# ============================================================================
# CONSTANTES DE CULTIVOS - ZANAHORIA
# ============================================================================

SUPERFICIE_ZANAHORIA = 0.15
"""Superficie requerida por zanahoria (metros cuadrados)."""

AGUA_INICIAL_ZANAHORIA = 0
"""Agua inicial de una zanahoria (litros)."""

# ============================================================================
# CONSTANTES DE ARBOLES
# ============================================================================

ALTURA_INICIAL_ARBOL = 1.0
"""Altura inicial de un arbol (metros)."""

CRECIMIENTO_PINO = 0.10
"""Crecimiento del pino por riego (metros)."""

CRECIMIENTO_OLIVO = 0.01
"""Crecimiento del olivo por riego (metros)."""

ALTURA_INICIAL_OLIVO = 0.5
"""Altura inicial de un olivo (metros)."""

# ============================================================================
# CONSTANTES DE ABSORCION DE AGUA
# ============================================================================

ABSORCION_SEASONAL_VERANO = 5
"""Absorcion de agua en verano para estrategia seasonal (litros)."""

ABSORCION_SEASONAL_INVIERNO = 2
"""Absorcion de agua en invierno para estrategia seasonal (litros)."""

ABSORCION_LECHUGA = 1
"""Absorcion constante de agua para lechugas (litros)."""

ABSORCION_ZANAHORIA = 2
"""Absorcion constante de agua para zanahorias (litros)."""

# ============================================================================
# CONSTANTES DE TEMPORADAS
# ============================================================================

MES_INICIO_VERANO = 3
"""Mes de inicio de verano (marzo = 3)."""

MES_FIN_VERANO = 8
"""Mes de fin de verano (agosto = 8)."""

# ============================================================================
# CONSTANTES DE SENSORES
# ============================================================================

INTERVALO_SENSOR_TEMPERATURA = 2.0
"""Intervalo de lectura del sensor de temperatura (segundos)."""

INTERVALO_SENSOR_HUMEDAD = 3.0
"""Intervalo de lectura del sensor de humedad (segundos)."""

SENSOR_TEMP_MIN = -25
"""Temperatura minima del sensor (grados Celsius)."""

SENSOR_TEMP_MAX = 50
"""Temperatura maxima del sensor (grados Celsius)."""

SENSOR_HUMEDAD_MIN = 0
"""Humedad minima del sensor (porcentaje)."""

SENSOR_HUMEDAD_MAX = 100
"""Humedad maxima del sensor (porcentaje)."""

# ============================================================================
# CONSTANTES DE CONTROL DE RIEGO
# ============================================================================

TEMP_MIN_RIEGO = 8
"""Temperatura minima para activar riego (grados Celsius)."""

TEMP_MAX_RIEGO = 15
"""Temperatura maxima para activar riego (grados Celsius)."""

HUMEDAD_MAX_RIEGO = 50
"""Humedad maxima para activar riego (porcentaje)."""

INTERVALO_CONTROL_RIEGO = 2.5
"""Intervalo de evaluacion del control de riego (segundos)."""

# ============================================================================
# CONSTANTES DE THREADING
# ============================================================================

THREAD_JOIN_TIMEOUT = 2.0
"""Timeout para join de threads (segundos)."""

# ============================================================================
# CONSTANTES DE PERSISTENCIA
# ============================================================================

DIRECTORIO_DATA = "data"
"""Directorio donde se guardan los archivos de datos."""

EXTENSION_DATA = ".dat"
"""Extension de archivos de datos."""

# ============================================================================
# ALIASES DE COMPATIBILIDAD (para evitar romper imports existentes)
# ============================================================================

# Agua / riego
AGUA_RIEGO = AGUA_CONSUMIDA_POR_RIEGO
AGUA_MINIMA_RIEGO = AGUA_MINIMA

# Crecimiento de árboles (usado en servicios)
ALTURA_INCREMENTO_PINO = CRECIMIENTO_PINO
ALTURA_INCREMENTO_OLIVO = CRECIMIENTO_OLIVO



################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/61: __init__.py
# Directorio: entidades
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 4/61: __init__.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 5/61: arbol.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 6/61: cultivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 7/61: hortaliza.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 8/61: lechuga.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 9/61: olivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 10/61: pino.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/pino.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 11/61: tipo_aceituna.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 12/61: zanahoria.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 13/61: __init__.py
# Directorio: entidades/personal
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 14/61: apto_medico.py
# Directorio: entidades/personal
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 15/61: herramienta.py
# Directorio: entidades/personal
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/personal/herramienta.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 16/61: tarea.py
# Directorio: entidades/personal
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/personal/tarea.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 17/61: trabajador.py
# Directorio: entidades/personal
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/personal/trabajador.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 18/61: __init__.py
# Directorio: entidades/terrenos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 19/61: plantacion.py
# Directorio: entidades/terrenos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 20/61: registro_forestal.py
# Directorio: entidades/terrenos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 21/61: tierra.py
# Directorio: entidades/terrenos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 22/61: __init__.py
# Directorio: excepciones
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 23/61: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/excepciones/agua_agotada_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 24/61: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/excepciones/forestacion_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 25/61: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/excepciones/mensajes_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 26/61: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/excepciones/persistencia_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 27/61: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 28/61: __init__.py
# Directorio: patrones
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 29/61: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 30/61: cultivo_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================

"""
Modulo que define la Factory para creacion de cultivos.

Este modulo contiene la clase CultivoFactory que implementa el patron
Factory Method para crear cultivos sin exponer clases concretas.

Ubicacion: python_forestacion/patrones/factory/cultivo_factory.py

Patron: FACTORY METHOD
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoFactory:
    """
    Factory para creacion de cultivos.
    
    Encapsula la logica de creacion de diferentes tipos de cultivos
    sin que el cliente conozca las clases concretas.
    
    Patron de diseno: Factory Method
    
    Cultivos soportados:
        - Pino
        - Olivo
        - Lechuga
        - Zanahoria
    """
    
    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """
        Crea un cultivo segun la especie especificada.
        
        Este es el metodo factory principal. Usa un diccionario
        de factories (NO if/elif) para mejor extensibilidad.
        
        Args:
            especie: Nombre de la especie a crear ("Pino", "Olivo", etc.)
            
        Returns:
            Instancia de Cultivo (tipo base, no tipo concreto)
            
        Raises:
            ValueError: Si la especie no es reconocida
        """
        # Diccionario de factories (NO lambdas - usar metodos estaticos)
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }
        
        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")
        
        # Llamar al metodo factory apropiado
        return factories[especie]()
    
    # ========================================================================
    # METODOS FACTORY PRIVADOS (NO LAMBDAS)
    # ========================================================================
    
    @staticmethod
    def _crear_pino() -> 'Cultivo':
        """
        Crea una instancia de Pino con valores por defecto.
        
        Returns:
            Instancia de Pino
        """
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.constantes import VARIEDAD_PINO_DEFAULT
        return Pino(variedad=VARIEDAD_PINO_DEFAULT)
    
    @staticmethod
    def _crear_olivo() -> 'Cultivo':
        """
        Crea una instancia de Olivo con valores por defecto.
        
        Returns:
            Instancia de Olivo
        """
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)
    
    @staticmethod
    def _crear_lechuga() -> 'Cultivo':
        """
        Crea una instancia de Lechuga con valores por defecto.
        
        Returns:
            Instancia de Lechuga
        """
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.constantes import VARIEDAD_LECHUGA_DEFAULT
        return Lechuga(variedad=VARIEDAD_LECHUGA_DEFAULT)
    
    @staticmethod
    def _crear_zanahoria() -> 'Cultivo':
        """
        Crea una instancia de Zanahoria con valores por defecto.
        
        Returns:
            Instancia de Zanahoria
        """
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(baby_carrot=False)


################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 31/61: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 32/61: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/observer/observable.py
# ==============================================================================

from __future__ import annotations
from typing import Callable, Generic, List, TypeVar, Union

from python_forestacion.patrones.observer.observer import Observer

T = TypeVar("T")

# Tipo aceptado al registrar: Observer[T] o una función callback T -> None
Registrable = Union[Observer[T], Callable[[T], None]]


class _FunctionObserver(Observer[T]):
    """Adapter que envuelve un callback (callable) como Observer[T]."""

    def __init__(self, fn: Callable[[T], None]) -> None:
        self._fn = fn

    def actualizar(self, evento: T) -> None:
        self._fn(evento)


class Observable(Generic[T]):
    """Sujeto observable: mantiene y notifica observadores."""

    def __init__(self) -> None:
        self._observadores: List[Observer[T]] = []

    # -------------------- Gestión de observadores --------------------
    def agregar_observador(self, obs: Registrable[T]) -> None:
        """Acepta tanto Observer[T] como funciones T -> None."""
        if callable(obs):
            self._observadores.append(_FunctionObserver(obs))  # wrap
        else:
            self._observadores.append(obs)

    def eliminar_observador(self, obs: Registrable[T]) -> None:
        """Intenta eliminar el observer (o su wrapper si era función)."""
        if callable(obs):
            # remover primer wrapper que apunte a esa función
            for i, o in enumerate(self._observadores):
                if isinstance(o, _FunctionObserver) and getattr(o, "_fn", None) is obs:
                    del self._observadores[i]
                    return
        else:
            try:
                self._observadores.remove(obs)
            except ValueError:
                pass

    # -------------------------- Notificación -------------------------
    def notificar_observadores(self, evento: T) -> None:
        # Copia defensiva por si se modifica la lista durante la iteración
        for observador in list(self._observadores):
            observador.actualizar(evento)


# ==============================================================================
# ARCHIVO 33/61: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/observer/observer.py
# ==============================================================================

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Observer(ABC, Generic[T]):
    """Contrato del observador."""

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Recibe el evento/valor observado."""
        raise NotImplementedError



################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 34/61: absorcion_agua_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

from abc import ABC, abstractmethod
from datetime import date

class AbsorcionAguaStrategy(ABC):
    """Contrato para calcular cuánta agua absorbe un cultivo en un riego."""

    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: object,  # evitamos imports circulares
    ) -> int:
        """Devuelve litros absorbidos."""
        raise NotImplementedError



################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 35/61: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/61: absorcion_constante_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ==============================================================================

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Siempre devuelve la misma cantidad de litros."""

    def __init__(self, cantidad_constante: int) -> None:
        self._cantidad = int(cantidad_constante)

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: object,
    ) -> int:
        return self._cantidad

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._cantidad})"


# ==============================================================================
# ARCHIVO 37/61: absorcion_seasonal_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ==============================================================================

from datetime import date
from python_forestacion.constantes import (
    MES_INICIO_VERANO,
    MES_FIN_VERANO,
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
)
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Verano: 5L, resto: 2L (según constantes)."""

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: object,
    ) -> int:
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        return ABSORCION_SEASONAL_INVIERNO



################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 38/61: __init__.py
# Directorio: riego
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/riego/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: riego/control
################################################################################

# ==============================================================================
# ARCHIVO 39/61: __init__.py
# Directorio: riego/control
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/riego/control/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 40/61: control_riego_task.py
# Directorio: riego/control
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/riego/control/control_riego_task.py
# ==============================================================================

import threading
import time
from typing import Optional

from python_forestacion.constantes import (
    TEMP_MIN_RIEGO, TEMP_MAX_RIEGO, HUMEDAD_MAX_RIEGO, INTERVALO_CONTROL_RIEGO
)
from python_forestacion.patrones.observer.observer import Observer

class ControlRiegoTask(threading.Thread, Observer[float]):
    """Riega cuando 8°C ≤ temp ≤ 15°C y humedad < 50%."""

    def __init__(self, sensor_temperatura, sensor_humedad, plantacion, plantacion_service):
        threading.Thread.__init__(self, daemon=True)
        Observer.__init__(self)
        self._detener_event = threading.Event()
        self._temp: Optional[float] = None
        self._hum: Optional[float] = None
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service

        # Se registra a sí mismo como Observer
        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)

    def detener(self) -> None:
        self._detener_event.set()

    # Observer
    def actualizar(self, evento: float) -> None:
        # Heurística simple por rango (sirve para el demo)
        if -50.0 <= evento <= 80.0:
            self._temp = evento
        else:
            self._hum = evento

    def run(self) -> None:
        while not self._detener_event.is_set():
            if self._temp is not None and self._hum is not None:
                if (TEMP_MIN_RIEGO <= self._temp <= TEMP_MAX_RIEGO) and (self._hum < HUMEDAD_MAX_RIEGO):
                    try:
                        self._plantacion_service.regar(self._plantacion)
                        print(f"[AUTO-RIEGO] Temp={self._temp:.1f}°C  Hum={self._hum:.1f}% → RIEGO ACTIVADO")
                    except Exception as e:
                        print(f"[AVISO] No se pudo regar automáticamente: {e}")
            time.sleep(INTERVALO_CONTROL_RIEGO)



################################################################################
# DIRECTORIO: riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 41/61: __init__.py
# Directorio: riego/sensores
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/riego/sensores/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 42/61: humedad_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================

import threading
import random
import time

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    SENSOR_HUMEDAD_MIN,
    SENSOR_HUMEDAD_MAX,
)

class HumedadReaderTask(threading.Thread, Observable[float]):
    def __init__(self) -> None:
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._stop_event = threading.Event()  # ¡no usar _stop!

    def detener(self) -> None:
        self._stop_event.set()

    def run(self) -> None:
        while not self._stop_event.is_set():
            valor = float(random.uniform(SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX))
            self.notificar_observadores(valor)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)


# ==============================================================================
# ARCHIVO 43/61: temperatura_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

import threading
import random
import time

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    SENSOR_TEMP_MIN,
    SENSOR_TEMP_MAX,
)

class TemperaturaReaderTask(threading.Thread, Observable[float]):
    def __init__(self) -> None:
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._stop_event = threading.Event()  # ¡no usar _stop!

    def detener(self) -> None:
        self._stop_event.set()

    def run(self) -> None:
        while not self._stop_event.is_set():
            valor = float(random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX))
            self.notificar_observadores(valor)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 44/61: __init__.py
# Directorio: servicios
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 45/61: __init__.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 46/61: arbol_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """Base para servicios de árboles. Provee utilidades de crecimiento."""

    def _crecer(self, arbol: "Arbol", delta_altura: float) -> None:
        arbol.set_altura(arbol.get_altura() + delta_altura)

    def __repr__(self) -> str:
        return super().__repr__()


# ==============================================================================
# ARCHIVO 47/61: cultivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

# Standard library
from datetime import date
from typing import TYPE_CHECKING, Optional
from abc import ABC

# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import (
    AbsorcionAguaStrategy,
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService(ABC):
    """
    Servicio base para cualquier Cultivo.
    Orquesta la absorción delegando el cálculo a la Strategy inyectada.
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy) -> None:
        self._estrategia_absorcion = estrategia_absorcion

    # --------------------------- API pública ----------------------------
    def absorver_agua(
        self,
        cultivo: "Cultivo",
        fecha: Optional[date] = None,
        temperatura: float = 0.0,
        humedad: float = 0.0,
    ) -> int:
        """Actualiza el agua del cultivo según la Strategy y ejecuta el post-hook."""
        fecha = fecha or date.today()
        litros = self._estrategia_absorcion.calcular_absorcion(
            fecha=fecha,
            temperatura=temperatura,
            humedad=humedad,
            cultivo=cultivo,
        )
        cultivo.set_agua(cultivo.get_agua() + litros)
        self._post_absorcion(cultivo, litros)
        return litros

    def mostrar_datos(self, cultivo: "Cultivo") -> None:
        print(f"Cultivo: {type(cultivo).__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")

    # --------------------------- Hooks ----------------------------------
    def _post_absorcion(self, cultivo: "Cultivo", litros_absorbidos: int) -> None:
        """Hook para subclases (p.ej., crecimiento en árboles)."""
        return

    # ---------------------- Representación por defecto -------------------
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(strategy={self._estrategia_absorcion})"


# ==============================================================================
# ARCHIVO 48/61: cultivo_service_registry.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

"""
Modulo que define el Registry de servicios de cultivos.

Este modulo contiene la clase CultivoServiceRegistry que implementa
los patrones SINGLETON y REGISTRY para gestionar servicios de cultivos.

Ubicacion: python_forestacion/servicios/cultivos/cultivo_service_registry.py

Patrones: SINGLETON + REGISTRY
"""

from threading import Lock
from datetime import date
from typing import TYPE_CHECKING, Dict, Callable

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService


class CultivoServiceRegistry:
    """
    Registry Singleton de servicios de cultivos.
    
    Implementa dos patrones de diseno:
        1. SINGLETON: Garantiza una unica instancia compartida
        2. REGISTRY: Despacho polimorfico sin isinstance()
    
    Elimina cascadas de isinstance() usando diccionarios de handlers.
    Thread-safe con double-checked locking.
    """
    
    # ========================================================================
    # PATRON SINGLETON
    # ========================================================================
    
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        """
        Controla la instanciacion para garantizar instancia unica.
        
        Implementa double-checked locking para thread-safety.
        
        Returns:
            La unica instancia de CultivoServiceRegistry
        """
        if cls._instance is None:
            with cls._lock:  # Thread-safe
                if cls._instance is None:  # Double-checked
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance
    
    @classmethod
    def get_instance(cls):
        """
        Obtiene la instancia unica del registry.
        
        Returns:
            La unica instancia de CultivoServiceRegistry
        """
        if cls._instance is None:
            cls()
        return cls._instance
    
    # ========================================================================
    # INICIALIZACION
    # ========================================================================
    
    def _inicializar_servicios(self) -> None:
        """
        Inicializa los servicios y registros de handlers.
        
        Este metodo se llama una sola vez al crear la instancia.
        """
        # Crear instancias de servicios
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()
        
        # ====================================================================
        # PATRON REGISTRY: Diccionarios de handlers (NO lambdas)
        # ====================================================================
        
        # Registry para absorber_agua
        self._absorber_agua_handlers: Dict[type, Callable] = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }
        
        # Registry para mostrar_datos
        self._mostrar_datos_handlers: Dict[type, Callable] = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }
    
    # ========================================================================
    # METODOS PUBLICOS (Dispatch polimorfico)
    # ========================================================================
    
    def absorber_agua(
        self,
        cultivo: 'Cultivo',
        fecha: date = None,
        temperatura: float = 20.0,
        humedad: float = 50.0
    ) -> int:
        """
        Hace que el cultivo absorba agua usando dispatch polimorfico.
        
        Args:
            cultivo: Cultivo que va a absorber agua
            fecha: Fecha del riego
            temperatura: Temperatura ambiente
            humedad: Humedad ambiente
            
        Returns:
            Cantidad de agua absorbida
            
        Raises:
            ValueError: Si el tipo de cultivo no esta registrado
        """
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo de cultivo no registrado: {tipo}")
        
        # Dispatch polimorfico (NO isinstance)
        return self._absorber_agua_handlers[tipo](cultivo, fecha, temperatura, humedad)
    
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra los datos del cultivo usando dispatch polimorfico.
        
        Args:
            cultivo: Cultivo a mostrar
            
        Raises:
            ValueError: Si el tipo de cultivo no esta registrado
        """
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo de cultivo no registrado: {tipo}")
        
        # Dispatch polimorfico (NO isinstance)
        self._mostrar_datos_handlers[tipo](cultivo)
    
    # ========================================================================
    # HANDLERS PRIVADOS (NO lambdas)
    # ========================================================================
    
    def _absorber_agua_pino(self, cultivo, fecha, temperatura, humedad):
        return self._pino_service.absorver_agua(cultivo, fecha, temperatura, humedad)
    
    def _absorber_agua_olivo(self, cultivo, fecha, temperatura, humedad):
        return self._olivo_service.absorver_agua(cultivo, fecha, temperatura, humedad)
    
    def _absorber_agua_lechuga(self, cultivo, fecha, temperatura, humedad):
        return self._lechuga_service.absorver_agua(cultivo, fecha, temperatura, humedad)
    
    def _absorber_agua_zanahoria(self, cultivo, fecha, temperatura, humedad):
        return self._zanahoria_service.absorver_agua(cultivo, fecha, temperatura, humedad)
    
    def _mostrar_datos_pino(self, cultivo):
        self._pino_service.mostrar_datos(cultivo)
    
    def _mostrar_datos_olivo(self, cultivo):
        self._olivo_service.mostrar_datos(cultivo)
    
    def _mostrar_datos_lechuga(self, cultivo):
        self._lechuga_service.mostrar_datos(cultivo)
    
    def _mostrar_datos_zanahoria(self, cultivo):
        self._zanahoria_service.mostrar_datos(cultivo)
    
    # ========================================================================
    # METODOS DE SERVICIO ESPECIFICOS
    # ========================================================================
    
    def crecer_arbol(self, arbol) -> None:
        """
        Hace crecer un arbol (solo para Pino y Olivo).
        
        Args:
            arbol: Arbol a hacer crecer
        """
        tipo = type(arbol)
        if tipo == Pino:
            self._pino_service.crecer(arbol)
        elif tipo == Olivo:
            self._olivo_service.crecer(arbol)

# ==============================================================================
# ARCHIVO 49/61: lechuga_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================

from typing import TYPE_CHECKING, Any

from python_forestacion.constantes import ABSORCION_LECHUGA
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import (
    AbsorcionConstanteStrategy,
)
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """Servicio para Lechuga (absorción constante). Tolerante a distintas APIs de la entidad."""

    def __init__(self) -> None:
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_LECHUGA))

    # -------------------------- Helpers internos --------------------------
    @staticmethod
    def _get_invernadero(cultivo: Any) -> Any:
        """
        Devuelve el valor de 'invernadero' sin asumir un contrato fijo.
        Prueba en orden: is_invernadero(), get_invernadero(), atributo _invernadero.
        """
        if hasattr(cultivo, "is_invernadero") and callable(getattr(cultivo, "is_invernadero")):
            return cultivo.is_invernadero()
        if hasattr(cultivo, "get_invernadero") and callable(getattr(cultivo, "get_invernadero")):
            return cultivo.get_invernadero()
        if hasattr(cultivo, "_invernadero"):
            return getattr(cultivo, "_invernadero")
        return None

    # ---------------------------- API pública ------------------------------
    def mostrar_datos(self, cultivo: "Lechuga") -> None:
        super().mostrar_datos(cultivo)

        # Variedad (si existe getter)
        try:
            print(f"Variedad: {cultivo.get_variedad()}")
        except AttributeError:
            pass

        # Invernadero con fallback robusto
        inv = self._get_invernadero(cultivo)
        if inv is not None:
            print(f"Invernadero: {inv}")

    def __repr__(self) -> str:
        return super().__repr__()


# ==============================================================================
# ARCHIVO 50/61: olivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================

from typing import TYPE_CHECKING

from python_forestacion.constantes import ALTURA_INCREMENTO_OLIVO
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import (
    AbsorcionSeasonalStrategy,
)
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """Servicio específico para Olivo (estacional + crecimiento menor)."""

    def __init__(self) -> None:
        super().__init__(AbsorcionSeasonalStrategy())

    def _post_absorcion(self, cultivo: "Olivo", litros_absorbidos: int) -> None:
        self._crecer(cultivo, ALTURA_INCREMENTO_OLIVO)

    def mostrar_datos(self, cultivo: "Olivo") -> None:
        super().mostrar_datos(cultivo)
        print(f"ID: {cultivo.get_id()}")
        print(f"Altura: {cultivo.get_altura()} m")
        print(f"Tipo de aceituna: {cultivo.get_tipo_aceituna().name}")

    def __repr__(self) -> str:
        return super().__repr__()


# ==============================================================================
# ARCHIVO 51/61: pino_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================

from typing import TYPE_CHECKING

from python_forestacion.constantes import ALTURA_INCREMENTO_PINO
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import (
    AbsorcionSeasonalStrategy,
)
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """Servicio específico para Pino (estrategia estacional + crecimiento)."""

    def __init__(self) -> None:
        super().__init__(AbsorcionSeasonalStrategy())

    def _post_absorcion(self, cultivo: "Pino", litros_absorbidos: int) -> None:
        self._crecer(cultivo, ALTURA_INCREMENTO_PINO)

    def mostrar_datos(self, cultivo: "Pino") -> None:
        super().mostrar_datos(cultivo)
        print(f"ID: {cultivo.get_id()}")
        print(f"Altura: {cultivo.get_altura()} m")
        print(f"Variedad: {cultivo.get_variedad()}")

    def __repr__(self) -> str:
        return super().__repr__()


# ==============================================================================
# ARCHIVO 52/61: zanahoria_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================

from typing import TYPE_CHECKING

from python_forestacion.constantes import ABSORCION_ZANAHORIA
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import (
    AbsorcionConstanteStrategy,
)
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """Servicio para Zanahoria (absorción constante)."""

    def __init__(self) -> None:
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_ZANAHORIA))

    def mostrar_datos(self, cultivo: "Zanahoria") -> None:
        super().mostrar_datos(cultivo)
        print(f"Es baby carrot: {cultivo.is_baby_carrot()}")

    def __repr__(self) -> str:
        return super().__repr__()



################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 53/61: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/negocio/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 54/61: fincas_service.py
# Directorio: servicios/negocio
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/negocio/fincas_service.py
# ==============================================================================

"""
Servicio de alto nivel para gestión de múltiples fincas.

Orquesta operaciones complejas sobre múltiples registros forestales.
"""

# Standard library
from typing import TYPE_CHECKING, Dict, Type

# Local application
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.negocio.paquete import Paquete

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class FincasService:
    """
    Servicio de alto nivel para gestión de múltiples fincas.
    
    Orquesta operaciones sobre múltiples registros forestales:
    - Gestión de colección de fincas
    - Fumigación masiva
    - Cosecha y empaquetado por tipo
    
    Attributes:
        _fincas: Diccionario de registros forestales por ID de padrón
        _plantacion_service: Servicio de plantación inyectado
    """
    
    def __init__(self):
        """
        Inicializa el servicio de fincas.
        
        Crea diccionario interno para almacenar fincas.
        """
        self._fincas: Dict[int, 'RegistroForestal'] = {}
        self._plantacion_service = PlantacionService()
    
    def add_finca(self, registro: 'RegistroForestal') -> None:
        """
        Agrega una finca al registro.
        
        Args:
            registro: Registro forestal a agregar
        """
        id_padron = registro.get_id_padron()
        self._fincas[id_padron] = registro
        print(f"Finca con padrón {id_padron} agregada al sistema")
    
    def buscar_finca(self, id_padron: int) -> 'RegistroForestal':
        """
        Busca una finca por ID de padrón.
        
        Args:
            id_padron: ID catastral de la finca
            
        Returns:
            Registro forestal encontrado
            
        Raises:
            KeyError: Si la finca no existe
        """
        if id_padron not in self._fincas:
            raise KeyError(f"No se encontró finca con padrón {id_padron}")
        
        return self._fincas[id_padron]
    
    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """
        Fumiga una finca específica.
        
        Args:
            id_padron: ID de la finca a fumigar
            plaguicida: Tipo de plaguicida a aplicar
            
        Raises:
            KeyError: Si la finca no existe
        """
        finca = self.buscar_finca(id_padron)
        plantacion = finca.get_plantacion()
        
        self._plantacion_service.fumigar(plantacion, plaguicida)
    
    def cosechar_yempaquetar(self, tipo_cultivo: Type['Cultivo']) -> Paquete:
        """
        Cosecha todos los cultivos de un tipo específico y los empaqueta.
        
        Busca en TODAS las fincas del sistema, cosecha los cultivos
        del tipo especificado y los empaqueta en un contenedor genérico.
        
        Args:
            tipo_cultivo: Clase del tipo de cultivo a cosechar
                         (ej: Pino, Olivo, Lechuga, Zanahoria)
            
        Returns:
            Paquete genérico con los cultivos cosechados
            
        Example:
            from python_forestacion.entidades.cultivos.lechuga import Lechuga
            caja_lechugas = fincas_service.cosechar_yempaquetar(Lechuga)
        """
        cultivos_cosechados = []
        
        # Iterar sobre todas las fincas
        for registro in self._fincas.values():
            plantacion = registro.get_plantacion()
            cultivos = plantacion.get_cultivos()
            
            # Filtrar cultivos del tipo especificado
            cultivos_filtrados = [
                c for c in cultivos 
                if isinstance(c, tipo_cultivo)
            ]
            
            # Agregar a cosecha
            cultivos_cosechados.extend(cultivos_filtrados)
            
            # Remover cultivos cosechados de la plantación
            cultivos_restantes = [
                c for c in cultivos 
                if not isinstance(c, tipo_cultivo)
            ]
            plantacion.set_cultivos(cultivos_restantes)
        
        print(f"\nCOSECHANDO {len(cultivos_cosechados)} unidades de {tipo_cultivo}")
        
        # Crear paquete genérico tipo-seguro
        paquete = Paquete(cultivos_cosechados)
        
        return paquete

# ==============================================================================
# ARCHIVO 55/61: paquete.py
# Directorio: servicios/negocio
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/negocio/paquete.py
# ==============================================================================

"""
Clase para empaquetado genérico de cultivos.

Implementa un contenedor tipo-seguro usando Generics.
"""

# Standard library
from typing import Generic, TypeVar, List

# Local application
from python_forestacion.entidades.cultivos.cultivo import Cultivo

# TypeVar para tipo-seguridad
T = TypeVar('T', bound=Cultivo)


class Paquete(Generic[T]):
    """
    Contenedor genérico tipo-seguro para cultivos.
    
    Permite empaquetar cultivos de un tipo específico
    garantizando tipo-seguridad en tiempo de compilación.
    
    Ejemplo:
        paquete_lechugas: Paquete[Lechuga] = Paquete(lechugas)
        paquete_pinos: Paquete[Pino] = Paquete(pinos)
    
    Attributes:
        _contenido: Lista de cultivos del tipo especificado
        _id_paquete: ID único del paquete
    """
    
    # Contador de clase para IDs únicos
    _contador_id = 0
    
    def __init__(self, contenido: List[T]):
        """
        Inicializa un paquete con cultivos.
        
        Args:
            contenido: Lista de cultivos del mismo tipo
        """
        self._contenido = contenido.copy()  # Defensive copy
        
        # Asignar ID único
        Paquete._contador_id += 1
        self._id_paquete = Paquete._contador_id
    
    def get_contenido(self) -> List[T]:
        """
        Obtiene el contenido del paquete.
        
        Returns:
            Copia de la lista de cultivos (inmutable)
        """
        return self._contenido.copy()
    
    def get_cantidad(self) -> int:
        """
        Obtiene la cantidad de cultivos en el paquete.
        
        Returns:
            Cantidad de cultivos
        """
        return len(self._contenido)
    
    def get_id_paquete(self) -> int:
        """
        Obtiene el ID del paquete.
        
        Returns:
            ID único del paquete
        """
        return self._id_paquete
    
    def mostrar_contenido_caja(self) -> None:
        """
        Muestra información del paquete.
        """
        if not self._contenido:
            print("Caja vacía")
            return
        
        # Obtener tipo del primer elemento
        tipo_cultivo = type(self._contenido[0]).__name__
        
        print("\nContenido de la caja:")
        print(f"  Tipo: {tipo_cultivo}")
        print(f"  Cantidad: {self.get_cantidad()}")
        print(f"  ID Paquete: {self._id_paquete}")


################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 56/61: __init__.py
# Directorio: servicios/personal
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 57/61: trabajador_service.py
# Directorio: servicios/personal
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================

"""
Servicio para gestión de trabajadores.

Proporciona operaciones de:
- Asignación de apto médico
- Ejecución de tareas con validación de certificación
"""

# Standard library
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.entidades.personal.apto_medico import AptoMedico

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.herramienta import Herramienta


class TrabajadorService:
    """
    Servicio para gestión de trabajadores.
    
    Responsabilidades:
    - Asignar certificación médica
    - Ejecutar tareas con validación de apto
    - Ordenar tareas por ID descendente
    """
    
    def asignar_apto_medico(
        self,
        trabajador: 'Trabajador',
        apto: bool,
        fecha_emision: date,
        observaciones: str = ""
    ) -> None:
        """
        Asigna un apto médico a un trabajador.
        
        Args:
            trabajador: Trabajador a certificar
            apto: True si está apto, False si no
            fecha_emision: Fecha de emisión del certificado
            observaciones: Observaciones médicas (opcional)
        """
        apto_medico = AptoMedico(
            apto=apto,
            fecha_emision=fecha_emision,
            observaciones=observaciones
        )
        
        trabajador.set_apto_medico(apto_medico)
        
        estado = "APTO" if apto else "NO APTO"
        print(f"Apto médico asignado a {trabajador.get_nombre()}: {estado}")
    
    def trabajar(
        self,
        trabajador: 'Trabajador',
        fecha: date,
        util: 'Herramienta'
    ) -> bool:
        """
        Ejecuta las tareas asignadas al trabajador.
        
        Validaciones:
        1. Verifica que tenga apto médico válido
        2. Filtra tareas de la fecha especificada
        3. Ordena tareas por ID descendente (sin lambdas)
        4. Ejecuta cada tarea con la herramienta asignada
        
        Args:
            trabajador: Trabajador que ejecuta las tareas
            fecha: Fecha de las tareas a ejecutar
            util: Herramienta a utilizar
            
        Returns:
            True si ejecutó tareas (tiene apto), False si no tiene apto
        """
        # Validar apto médico
        apto_medico = trabajador.get_apto_medico()
        
        if apto_medico is None or not apto_medico.esta_apto():
            print(f"{trabajador.get_nombre()} no puede trabajar: sin apto médico válido")
            return False
        
        # Obtener tareas de la fecha
        tareas = trabajador.get_tareas()
        tareas_del_dia = [t for t in tareas if t.get_fecha() == fecha]
        
        if not tareas_del_dia:
            print(f"{trabajador.get_nombre()} no tiene tareas para {fecha}")
            return True
        
        # Ordenar tareas por ID descendente (NO usar lambda)
        # Usar método estático como key function
        tareas_ordenadas = sorted(
            tareas_del_dia,
            key=self._obtener_id_tarea,
            reverse=True
        )
        
        # Ejecutar tareas
        for tarea in tareas_ordenadas:
            print(
                f"El trabajador {trabajador.get_nombre()} "
                f"realizo la tarea {tarea.get_id()} "
                f"{tarea.get_descripcion()} "
                f"con herramienta: {util.get_nombre()}"
            )
        
        return True
    
    @staticmethod
    def _obtener_id_tarea(tarea) -> int:
        """
        Función key para ordenar tareas por ID.
        
        Alternativa a lambda para cumplir con código limpio.
        
        Args:
            tarea: Tarea a extraer ID
            
        Returns:
            ID de la tarea
        """
        return tarea.get_id()


################################################################################
# DIRECTORIO: servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 58/61: __init__.py
# Directorio: servicios/terrenos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 59/61: plantacion_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================

from typing import TYPE_CHECKING, List
from datetime import date

from python_forestacion.constantes import AGUA_MINIMA, AGUA_RIEGO
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class PlantacionService:
    """Operaciones sobre una Plantación (plantar, regar, fumigar, etc.)."""

    def __init__(self) -> None:
        self._registry = CultivoServiceRegistry.get_instance()

    # -------------------------- Plantar --------------------------
    def plantar(self, plantacion: "Plantacion", especie: str, cantidad: int) -> None:
        nuevos: List["Cultivo"] = []
        for _ in range(int(cantidad)):
            cultivo = CultivoFactory.crear_cultivo(especie)  # Factory Method
            # Control de superficie disponible
            superficie_usada = sum(c.get_superficie() for c in plantacion.get_cultivos())
            if superficie_usada + cultivo.get_superficie() > plantacion.get_superficie():
                from python_forestacion.excepciones.superficie_insuficiente_exception import (
                    SuperficieInsuficienteException,
                )
                raise SuperficieInsuficienteException(
                    "No hay superficie disponible para plantar más cultivos"
                )
            nuevos.append(cultivo)

        # añadir todos juntos
        tmp = plantacion.get_cultivos()
        tmp.extend(nuevos)
        plantacion.set_cultivos(tmp)

    # --------------------------- Riego ---------------------------
    def regar(
        self,
        plantacion: "Plantacion",
        fecha: date | None = None,
        temperatura: float = 0.0,
        humedad: float = 0.0,
    ) -> None:
        """
        Resta AGUA_RIEGO del estanque de la plantación y hace que cada cultivo
        absorba agua según su Strategy (vía Registry).
        """
        if plantacion.get_agua_disponible() < AGUA_MINIMA:
            from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
            raise AguaAgotadaException("No hay agua suficiente en la plantación")

        # consumir agua del estanque de la plantación
        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - AGUA_RIEGO)

        # cada cultivo absorbe según su Strategy (usamos el Registry para despachar)
        for cultivo in plantacion.get_cultivos():
            self._registry.absorber_agua(cultivo)

    # -------------------------- Fumigar --------------------------
    def fumigar(self, plantacion: "Plantacion", plaguicida: str) -> None:
        """
        Aplica una fumigación a toda la plantación (demo: solo loguea la acción).
        """
        if not plaguicida or not plaguicida.strip():
            raise ValueError("El nombre del plaguicida no puede ser vacío")

        cant = len(plantacion.get_cultivos())
        try:
            nombre = plantacion.get_nombre()
        except AttributeError:
            nombre = "Plantación"

        print(f"[FUMIGACION] Aplicando '{plaguicida}' a {cant} cultivos en {nombre}")

    # ------------------------- Utilidades ------------------------
    def mostrar_cultivos(self, plantacion: "Plantacion") -> None:
        for c in plantacion.get_cultivos():
            self._registry.mostrar_datos(c)


# ==============================================================================
# ARCHIVO 60/61: registro_forestal_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ==============================================================================

import os
import pickle
from typing import TYPE_CHECKING

from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_DATA
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal

class RegistroForestalService:
    """Persistencia y presentación del Registro Forestal."""

    def __init__(self) -> None:
        self._registry = CultivoServiceRegistry.get_instance()

    def persistir(self, registro: "RegistroForestal") -> None:
        os.makedirs(DIRECTORIO_DATA, exist_ok=True)
        ruta = os.path.join(DIRECTORIO_DATA, f"{registro.get_propietario()}{EXTENSION_DATA}")
        with open(ruta, "wb") as f:
            pickle.dump(registro, f)
        print(f"Registro de {registro.get_propietario()} persistido exitosamente en {ruta}")

    @staticmethod
    def leer_registro(propietario: str) -> "RegistroForestal":
        if not propietario:
            raise ValueError("El nombre del propietario no puede ser nulo o vacío")
        ruta = os.path.join(DIRECTORIO_DATA, f"{propietario}{EXTENSION_DATA}")
        if not os.path.exists(ruta):
            from python_forestacion.excepciones.persistencia_exception import PersistenciaException
            raise PersistenciaException("Archivo no encontrado", ruta)
        with open(ruta, "rb") as f:
            return pickle.load(f)

    def mostrar_datos(self, registro: "RegistroForestal") -> None:
        print("\nREGISTRO FORESTAL\n=================")
        print(f"Padron:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo()}")
        print(f"Domicilio:   {registro.get_tierra().get_domicilio()}")
        print(f"Superficie:  {registro.get_tierra().get_superficie()}")
        cultivos = registro.get_plantacion().get_cultivos()
        print(f"Cantidad de cultivos plantados: {len(cultivos)}")
        print("Listado de Cultivos plantados\n____________________________\n")
        for c in cultivos:
            self._registry.mostrar_datos(c)
            print()


# ==============================================================================
# ARCHIVO 61/61: tierra_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION

class TierraService:
    """Crea Tierra y su Plantación asociada."""

    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str,
    ) -> Tierra:
        tierra = Tierra(id_padron_catastral, superficie, domicilio)
        plantacion = Plantacion(nombre_plantacion, superficie, AGUA_INICIAL_PLANTACION)
        tierra.set_finca(plantacion)
        return tierra



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 61
# Generado: 2025-10-22 01:16:07
################################################################################
"""
Sistema de Gestion Forestal - Punto de Entrada Principal

Demostracion completa del sistema que incluye:
- PATRON SINGLETON: CultivoServiceRegistry
- PATRON FACTORY: CultivoFactory
- PATRON OBSERVER: Sensores y eventos
- PATRON STRATEGY: Algoritmos de absorcion de agua
- PATRON REGISTRY: Dispatch polimorfico

Operaciones demostradas:
1. Creacion de terreno con plantacion
2. Plantacion de 4 tipos de cultivos
3. Sistema de riego automatizado con threads
4. Gestion de trabajadores con apto medico
5. Cosecha y empaquetado por tipo
6. Persistencia con Pickle
7. Recuperacion desde disco
"""

# Standard library
import time
from datetime import date

# Local application
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.pino import Pino

from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

from python_forestacion.constantes import THREAD_JOIN_TIMEOUT


# --- Join seguro que evita chocar con Thread._stop() ---
def _join_seguro(*threads, timeout: float | None = None) -> None:
    for t in threads:
        # Si existe un atributo _stop no-invocable (Event), lo removemos
        _stop_attr = getattr(t, "_stop", None)
        if _stop_attr is not None and not callable(_stop_attr):
            try:
                delattr(t, "_stop")
            except Exception:
                pass
        t.join(timeout=timeout)


def mostrar_encabezado():
    """Muestra encabezado del sistema."""
    print("=" * 70)
    print("         SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print("=" * 70)


def mostrar_seccion(titulo):
    """Muestra titulo de seccion."""
    print(f"\n{'-' * 70}")
    print(f"  {titulo}")
    print("-" * 70)


def demo_singleton():
    """
    Demuestra PATRON SINGLETON.
    
    Verifica que multiples instancias del registry
    retornan la misma instancia unica.
    """
    mostrar_seccion("PATRON SINGLETON: Inicializando servicios")
    
    # Crear dos instancias
    registry1 = CultivoServiceRegistry()
    registry2 = CultivoServiceRegistry.get_instance()
    
    # Verificar que son la misma instancia
    if registry1 is registry2:
        print("[OK] Todos los servicios comparten la misma instancia del Registry")
    else:
        print("[ERROR] Singleton no funciona correctamente")
    
    return registry1


def demo_terrenos_y_plantacion():
    """
    Demuestra creacion de terreno con plantacion.
    
    Returns:
        Tupla (terreno, plantacion, plantacion_service)
    """
    mostrar_seccion("Creando terreno con plantacion")
    
    tierra_service = TierraService()
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )
    
    plantacion = terreno.get_finca()
    plantacion_service = PlantacionService()
    
    print(f"Terreno creado: Padron {terreno.get_id_padron_catastral()}")
    print(f"Superficie: {terreno.get_superficie()} m2")
    print(f"Plantacion: {plantacion.get_nombre()}")
    
    return terreno, plantacion, plantacion_service


def demo_factory_y_strategy(plantacion, plantacion_service):
    """
    Demuestra PATRON FACTORY y PATRON STRATEGY.
    
    Planta cultivos usando Factory Method y riega usando Strategy.
    """
    mostrar_seccion("PATRON FACTORY: Plantando cultivos")
    
    # PATRON FACTORY: Crear cultivos sin conocer clases concretas
    plantacion_service.plantar(plantacion, "Pino", 5)
    plantacion_service.plantar(plantacion, "Olivo", 5)
    plantacion_service.plantar(plantacion, "Lechuga", 5)
    plantacion_service.plantar(plantacion, "Zanahoria", 5)
    
    print(f"\nTotal cultivos plantados: {len(plantacion.get_cultivos())}")
    
    mostrar_seccion("PATRON STRATEGY: Regando cultivos")
    
    # PATRON STRATEGY: Cada cultivo absorbe segun su estrategia
    plantacion_service.regar(plantacion)


def demo_observer_riego_automatico(plantacion, plantacion_service):
    """
    Demuestra PATRON OBSERVER con sistema de riego automatizado.
    
    Crea threads daemon para sensores (Observable) y control (Observer).
    """
    mostrar_seccion("PATRON OBSERVER: Sistema de riego automatizado")
    
    print("\n[INFO] Iniciando sensores y control automatico...")
    print("[INFO] El sistema regara cuando:")
    print("       - Temperatura entre 8C y 15C, Y")
    print("       - Humedad menor a 50%")
    print()
    
    # Crear sensores (Observable)
    tarea_temp = TemperaturaReaderTask()
    tarea_hum = HumedadReaderTask()
    
    # Crear controlador (Observer)
    tarea_control = ControlRiegoTask(
        sensor_temperatura=tarea_temp,
        sensor_humedad=tarea_hum,
        plantacion=plantacion,
        plantacion_service=plantacion_service
    )
    
    # Iniciar threads daemon
    tarea_temp.start()
    tarea_hum.start()
    tarea_control.start()
    
    # Dejar funcionar el sistema por 20 segundos
    print("[INFO] Sistema funcionando por 20 segundos...")
    time.sleep(20)
    
    # Detener sistema (graceful shutdown)
    print("\n[INFO] Deteniendo sistema de riego...")
    tarea_temp.detener()
    tarea_hum.detener()
    tarea_control.detener()
    
    # Esperar finalizacion con timeout (join SEGURO)
    _join_seguro(tarea_temp, tarea_hum, tarea_control, timeout=THREAD_JOIN_TIMEOUT)
    
    print("[OK] Sistema de riego detenido correctamente")


def demo_trabajadores():
    """
    Demuestra gestion de trabajadores con apto medico.
    
    Returns:
        Lista de trabajadores
    """
    mostrar_seccion("Gestion de trabajadores")
    
    # Crear tareas
    tareas = [
        Tarea(1, date.today(), "Desmalezar"),
        Tarea(2, date.today(), "Abonar"),
        Tarea(3, date.today(), "Marcar surcos")
    ]
    
    # Crear trabajador
    trabajador = Trabajador(
        dni=43888734,
        nombre="Juan Perez",
        tareas=tareas.copy()
    )
    
    print(f"Trabajador creado: {trabajador.get_nombre()}")
    print(f"Tareas asignadas: {len(trabajador.get_tareas())}")
    
    # Asignar apto medico
    trabajador_service = TrabajadorService()
    trabajador_service.asignar_apto_medico(
        trabajador=trabajador,
        apto=True,
        fecha_emision=date.today(),
        observaciones="Estado de salud: excelente"
    )
    
    # Ejecutar tareas
    print("\nEjecutando tareas:")
    herramienta = Herramienta(1, "Pala", True)
    trabajador_service.trabajar(trabajador, date.today(), herramienta)
    
    return [trabajador]


def demo_registro_y_persistencia(terreno, plantacion, trabajadores):
    """
    Demuestra creacion de registro forestal y persistencia.
    
    Returns:
        RegistroForestal creado
    """
    mostrar_seccion("Creando registro forestal")
    
    # Asignar trabajadores a plantacion
    plantacion.set_trabajadores(trabajadores)
    
    # Crear registro forestal
    registro = RegistroForestal(
        id_padron=1,
        tierra=terreno,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )
    
    print(f"Registro forestal creado para: {registro.get_propietario()}")
    
    # Persistir
    mostrar_seccion("Persistiendo registro en disco")
    registro_service = RegistroForestalService()
    registro_service.persistir(registro)
    
    # Leer desde disco
    mostrar_seccion("Recuperando registro desde disco")
    registro_leido = RegistroForestalService.leer_registro("Juan Perez")
    registro_service.mostrar_datos(registro_leido)
    
    return registro


def demo_fincas_y_cosecha(registro):
    """
    Demuestra operaciones de alto nivel con FincasService.
    """
    mostrar_seccion("Operaciones de negocio - FincasService")
    
    fincas_service = FincasService()
    
    # Agregar finca
    fincas_service.add_finca(registro)
    
    # Fumigar
    fincas_service.fumigar(id_padron=1, plaguicida="insecto organico")
    
    # Cosechar y empaquetar por tipo
    print("\n[INFO] Cosechando cultivos por tipo...")
    
    caja_lechugas = fincas_service.cosechar_yempaquetar(Lechuga)
    caja_lechugas.mostrar_contenido_caja()
    
    caja_pinos = fincas_service.cosechar_yempaquetar(Pino)
    caja_pinos.mostrar_contenido_caja()


def mostrar_resumen_final():
    """Muestra resumen de patrolesdemostrados."""
    mostrar_seccion("RESUMEN DE PATRONES DEMOSTRADOS")
    
    print("[OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
    print("[OK] FACTORY     - Creacion de cultivos sin clases concretas")
    print("[OK] OBSERVER    - Sistema de sensores y eventos")
    print("[OK] STRATEGY    - Algoritmos de absorcion de agua")
    print("[OK] REGISTRY    - Dispatch polimorfico sin isinstance()")
    
    print("\n" + "=" * 70)
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)


def main():
    """
    Funcion principal que ejecuta todas las demostraciones.
    """
    try:
        # Mostrar encabezado
        mostrar_encabezado()
        
        # 1. SINGLETON
        registry = demo_singleton()
        
        # 2. Crear terreno y plantacion
        terreno, plantacion, plantacion_service = demo_terrenos_y_plantacion()
        
        # 3. FACTORY + STRATEGY
        demo_factory_y_strategy(plantacion, plantacion_service)
        
        # 4. OBSERVER (threads)
        demo_observer_riego_automatico(plantacion, plantacion_service)
        
        # 5. Trabajadores
        trabajadores = demo_trabajadores()
        
        # 6. Persistencia
        registro = demo_registro_y_persistencia(terreno, plantacion, trabajadores)
        
        # 7. Operaciones de alto nivel
        demo_fincas_y_cosecha(registro)
        
        # 8. Resumen final
        mostrar_resumen_final()
        
    except Exception as e:
        print(f"\n[ERROR] Ocurrio un error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
