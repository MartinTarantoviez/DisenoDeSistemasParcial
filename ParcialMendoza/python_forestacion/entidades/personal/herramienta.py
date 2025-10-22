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