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