import threading
import time
from typing import Optional

from python_forestacion.constantes import (
    TEMP_MIN_RIEGO, TEMP_MAX_RIEGO, HUMEDAD_MAX_RIEGO, INTERVALO_CONTROL_RIEGO
)
from python_forestacion.patrones.observer.observer import Observer

class ControlRiegoTask(threading.Thread, Observer[float]):
    """Riega cuando 8°C ≤ temp ≤ 15°C y humedad < 50%."""

    def __init__(self, sensor_temperatura, sensor_humedad, plantacion, plantacion_service):
        threading.Thread.__init__(self, daemon=True)
        Observer.__init__(self)
        self._detener_event = threading.Event()
        self._temp: Optional[float] = None
        self._hum: Optional[float] = None
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service

        # Se registra a sí mismo como Observer
        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)

    def detener(self) -> None:
        self._detener_event.set()

    # Observer
    def actualizar(self, evento: float) -> None:
        # Heurística simple por rango (sirve para el demo)
        if -50.0 <= evento <= 80.0:
            self._temp = evento
        else:
            self._hum = evento

    def run(self) -> None:
        while not self._detener_event.is_set():
            if self._temp is not None and self._hum is not None:
                if (TEMP_MIN_RIEGO <= self._temp <= TEMP_MAX_RIEGO) and (self._hum < HUMEDAD_MAX_RIEGO):
                    try:
                        self._plantacion_service.regar(self._plantacion)
                        print(f"[AUTO-RIEGO] Temp={self._temp:.1f}°C  Hum={self._hum:.1f}% → RIEGO ACTIVADO")
                    except Exception as e:
                        print(f"[AVISO] No se pudo regar automáticamente: {e}")
            time.sleep(INTERVALO_CONTROL_RIEGO)
