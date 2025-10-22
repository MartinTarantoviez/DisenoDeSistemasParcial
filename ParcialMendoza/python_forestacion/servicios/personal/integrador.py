"""
Archivo integrador generado automaticamente
Directorio: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/personal
Fecha: 2025-10-22 01:16:07
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/servicios/personal/trabajador_service.py
# ================================================================================

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

