"""
Archivo integrador generado automaticamente
Directorio: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/riego/sensores
Fecha: 2025-10-22 01:16:07
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/riego/sensores/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/riego/sensores/humedad_reader_task.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: /home/martin/Escritorio/Diseño de sistemas/Parcial/ParcialMendoza/python_forestacion/riego/sensores/temperatura_reader_task.py
# ================================================================================

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


