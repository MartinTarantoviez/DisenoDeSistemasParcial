"""
Modulo de constantes centralizadas del sistema.

Este modulo contiene todas las constantes magicas del sistema, eliminando
valores hardcodeados y facilitando el mantenimiento.

Ubicacion: python_forestacion/constantes.py

Autor: Sistema de Gestion Forestal
Version: 1.0.0
"""

# ============================================================================
# CONSTANTES DE AGUA
# ============================================================================

AGUA_MINIMA = 10
"""Agua minima requerida para realizar un riego (litros)."""

AGUA_INICIAL_PLANTACION = 500
"""Agua disponible inicial en una plantacion (litros)."""

AGUA_CONSUMIDA_POR_RIEGO = 10
"""Cantidad de agua consumida en cada riego (litros)."""

# ============================================================================
# CONSTANTES DE CULTIVOS - PINO
# ============================================================================

SUPERFICIE_PINO = 2.0
"""Superficie requerida por pino (metros cuadrados)."""

AGUA_INICIAL_PINO = 2
"""Agua inicial de un pino (litros)."""

VARIEDAD_PINO_DEFAULT = "Parana"
"""Variedad por defecto de pino."""

# ============================================================================
# CONSTANTES DE CULTIVOS - OLIVO
# ============================================================================

SUPERFICIE_OLIVO = 3.0
"""Superficie requerida por olivo (metros cuadrados)."""

AGUA_INICIAL_OLIVO = 5
"""Agua inicial de un olivo (litros)."""

# ============================================================================
# CONSTANTES DE CULTIVOS - LECHUGA
# ============================================================================

SUPERFICIE_LECHUGA = 0.10
"""Superficie requerida por lechuga (metros cuadrados)."""

AGUA_INICIAL_LECHUGA = 1
"""Agua inicial de una lechuga (litros)."""

VARIEDAD_LECHUGA_DEFAULT = "Crespa"
"""Variedad por defecto de lechuga."""

# ============================================================================
# CONSTANTES DE CULTIVOS - ZANAHORIA
# ============================================================================

SUPERFICIE_ZANAHORIA = 0.15
"""Superficie requerida por zanahoria (metros cuadrados)."""

AGUA_INICIAL_ZANAHORIA = 0
"""Agua inicial de una zanahoria (litros)."""

# ============================================================================
# CONSTANTES DE ARBOLES
# ============================================================================

ALTURA_INICIAL_ARBOL = 1.0
"""Altura inicial de un arbol (metros)."""

CRECIMIENTO_PINO = 0.10
"""Crecimiento del pino por riego (metros)."""

CRECIMIENTO_OLIVO = 0.01
"""Crecimiento del olivo por riego (metros)."""

ALTURA_INICIAL_OLIVO = 0.5
"""Altura inicial de un olivo (metros)."""

# ============================================================================
# CONSTANTES DE ABSORCION DE AGUA
# ============================================================================

ABSORCION_SEASONAL_VERANO = 5
"""Absorcion de agua en verano para estrategia seasonal (litros)."""

ABSORCION_SEASONAL_INVIERNO = 2
"""Absorcion de agua en invierno para estrategia seasonal (litros)."""

ABSORCION_LECHUGA = 1
"""Absorcion constante de agua para lechugas (litros)."""

ABSORCION_ZANAHORIA = 2
"""Absorcion constante de agua para zanahorias (litros)."""

# ============================================================================
# CONSTANTES DE TEMPORADAS
# ============================================================================

MES_INICIO_VERANO = 3
"""Mes de inicio de verano (marzo = 3)."""

MES_FIN_VERANO = 8
"""Mes de fin de verano (agosto = 8)."""

# ============================================================================
# CONSTANTES DE SENSORES
# ============================================================================

INTERVALO_SENSOR_TEMPERATURA = 2.0
"""Intervalo de lectura del sensor de temperatura (segundos)."""

INTERVALO_SENSOR_HUMEDAD = 3.0
"""Intervalo de lectura del sensor de humedad (segundos)."""

SENSOR_TEMP_MIN = -25
"""Temperatura minima del sensor (grados Celsius)."""

SENSOR_TEMP_MAX = 50
"""Temperatura maxima del sensor (grados Celsius)."""

SENSOR_HUMEDAD_MIN = 0
"""Humedad minima del sensor (porcentaje)."""

SENSOR_HUMEDAD_MAX = 100
"""Humedad maxima del sensor (porcentaje)."""

# ============================================================================
# CONSTANTES DE CONTROL DE RIEGO
# ============================================================================

TEMP_MIN_RIEGO = 8
"""Temperatura minima para activar riego (grados Celsius)."""

TEMP_MAX_RIEGO = 15
"""Temperatura maxima para activar riego (grados Celsius)."""

HUMEDAD_MAX_RIEGO = 50
"""Humedad maxima para activar riego (porcentaje)."""

INTERVALO_CONTROL_RIEGO = 2.5
"""Intervalo de evaluacion del control de riego (segundos)."""

# ============================================================================
# CONSTANTES DE THREADING
# ============================================================================

THREAD_JOIN_TIMEOUT = 2.0
"""Timeout para join de threads (segundos)."""

# ============================================================================
# CONSTANTES DE PERSISTENCIA
# ============================================================================

DIRECTORIO_DATA = "data"
"""Directorio donde se guardan los archivos de datos."""

EXTENSION_DATA = ".dat"
"""Extension de archivos de datos."""

# ============================================================================
# ALIASES DE COMPATIBILIDAD (para evitar romper imports existentes)
# ============================================================================

# Agua / riego
AGUA_RIEGO = AGUA_CONSUMIDA_POR_RIEGO
AGUA_MINIMA_RIEGO = AGUA_MINIMA

# Crecimiento de árboles (usado en servicios)
ALTURA_INCREMENTO_PINO = CRECIMIENTO_PINO
ALTURA_INCREMENTO_OLIVO = CRECIMIENTO_OLIVO
