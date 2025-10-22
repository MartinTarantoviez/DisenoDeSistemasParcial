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