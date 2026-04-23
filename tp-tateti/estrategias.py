"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)


def minimax_max(tateti: Tateti, estado: List[List[str]]) -> float:
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)
    valor_max = float('-inf')

    for action in tateti.acciones(estado):
        new_state = tateti.resultado(estado, action)
        valor_max = max(valor_max, minimax_min(tateti, new_state))

    return valor_max

def minimax_min(tateti: Tateti, estado: List[List[str]]) -> float:
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)
    valor_min = float('+inf')

    for action in tateti.acciones(estado):
        new_state = tateti.resultado(estado, action)
        valor_min = min(valor_min, minimax_max(tateti, new_state))

    return valor_min

def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
     Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
    """
    # 1. Obtenemos quién juega (MAX o MIN)
    jugador_actual = tateti.jugador(estado)
    acciones = tateti.acciones(estado)
    
    if not acciones:
        raise ValueError("No hay acciones disponibles")

    sucs = {}
    
    # 2. Evaluamos cada acción posible
    if jugador_actual == JUGADOR_MAX:
        for action in acciones:
            new_state = tateti.resultado(estado, action)
            sucs[action] = minimax_min(tateti, new_state)
        # Buscamos la acción que da el valor máximo
        return min(sucs, key=lambda k: sucs[k])
    
    else:  # Es el turno de JUGADOR_MIN
        for action in acciones:
            new_state = tateti.resultado(estado, action)
            sucs[action] = minimax_max(tateti, new_state)
        # Buscamos la acción que da el valor mínimo
        return min(sucs, key=lambda k: sucs[k])


