from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Observer(ABC, Generic[T]):
    """Contrato del observador."""

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Recibe el evento/valor observado."""
        raise NotImplementedError
