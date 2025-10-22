"""
Archivo integrador generado automaticamente
Directorio: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos
Fecha: 2025-10-22 01:16:07
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

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


