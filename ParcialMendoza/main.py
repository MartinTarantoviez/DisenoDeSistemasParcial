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
