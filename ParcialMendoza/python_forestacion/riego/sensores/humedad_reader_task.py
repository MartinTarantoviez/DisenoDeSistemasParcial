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
