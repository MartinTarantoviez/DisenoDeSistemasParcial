from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """Base para servicios de árboles. Provee utilidades de crecimiento."""

    def _crecer(self, arbol: "Arbol", delta_altura: float) -> None:
        arbol.set_altura(arbol.get_altura() + delta_altura)

    def __repr__(self) -> str:
        return super().__repr__()
