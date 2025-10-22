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