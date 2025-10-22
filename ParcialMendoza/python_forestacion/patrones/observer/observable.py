from __future__ import annotations
from typing import Callable, Generic, List, TypeVar, Union

from python_forestacion.patrones.observer.observer import Observer

T = TypeVar("T")

# Tipo aceptado al registrar: Observer[T] o una función callback T -> None
Registrable = Union[Observer[T], Callable[[T], None]]


class _FunctionObserver(Observer[T]):
    """Adapter que envuelve un callback (callable) como Observer[T]."""

    def __init__(self, fn: Callable[[T], None]) -> None:
        self._fn = fn

    def actualizar(self, evento: T) -> None:
        self._fn(evento)


class Observable(Generic[T]):
    """Sujeto observable: mantiene y notifica observadores."""

    def __init__(self) -> None:
        self._observadores: List[Observer[T]] = []

    # -------------------- Gestión de observadores --------------------
    def agregar_observador(self, obs: Registrable[T]) -> None:
        """Acepta tanto Observer[T] como funciones T -> None."""
        if callable(obs):
            self._observadores.append(_FunctionObserver(obs))  # wrap
        else:
            self._observadores.append(obs)

    def eliminar_observador(self, obs: Registrable[T]) -> None:
        """Intenta eliminar el observer (o su wrapper si era función)."""
        if callable(obs):
            # remover primer wrapper que apunte a esa función
            for i, o in enumerate(self._observadores):
                if isinstance(o, _FunctionObserver) and getattr(o, "_fn", None) is obs:
                    del self._observadores[i]
                    return
        else:
            try:
                self._observadores.remove(obs)
            except ValueError:
                pass

    # -------------------------- Notificación -------------------------
    def notificar_observadores(self, evento: T) -> None:
        # Copia defensiva por si se modifica la lista durante la iteración
        for observador in list(self._observadores):
            observador.actualizar(evento)
