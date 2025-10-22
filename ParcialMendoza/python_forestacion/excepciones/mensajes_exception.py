"""
Mensajes centralizados para excepciones.

Todos los mensajes de error están aquí para facilitar
internacionalización y mantenimiento.
"""

# Mensajes de ForestacionException
MSG_FORESTACION_GENERICO = "Ha ocurrido un error en el sistema forestal"

# Mensajes de SuperficieInsuficienteException
MSG_SUPERFICIE_INSUFICIENTE_USER = "No hay suficiente superficie disponible para plantar"
MSG_SUPERFICIE_INSUFICIENTE_TECH = "Superficie requerida excede la disponible"

# Mensajes de AguaAgotadaException
MSG_AGUA_AGOTADA_USER = "No hay suficiente agua disponible para regar"
MSG_AGUA_AGOTADA_TECH = "Agua disponible insuficiente para operación de riego"

# Mensajes de PersistenciaException
MSG_PERSISTENCIA_ESCRITURA_USER = "No se pudo guardar el archivo"
MSG_PERSISTENCIA_LECTURA_USER = "No se pudo leer el archivo"
MSG_PERSISTENCIA_TECH = "Error de entrada/salida durante operación de persistencia"