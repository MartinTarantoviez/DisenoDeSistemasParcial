"""
Archivo integrador generado automaticamente
Directorio: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/factory
Fecha: 2025-10-22 01:16:07
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/factory/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/patrones/factory/cultivo_factory.py
# ================================================================================

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

