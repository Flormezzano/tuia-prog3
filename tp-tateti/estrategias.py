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
        
    Raises:
        NotImplementedError: Hasta que el alumno implemente el algoritmo
    """

    if tateti.jugador(estado) == JUGADOR_MAX:
        sucs = {}
        for action in tateti.acciones(estado): 
            new_state = tateti.resultado(estado, action)
            sucs [action] = minimax_min(tateti, new_state)
        
        valor_max = max(sucs.values())
        for suc in sucs.keys():
            if sucs[suc] == valor_max:
                return suc
    
    if tateti.jugador(estado) == JUGADOR_MIN:
        sucs = {}
        for action in tateti.acciones(estado):
            new_state = tateti.resultado(estado, action)
            sucs[action] = minimax_max(tateti, new_state)

        valor_min = min(sucs.values())
        for suc in sucs.keys():
            if sucs[suc] == valor_min:
                return suc
    



    raise NotImplementedError(
        "\n" + "="*60 +
        "\n🚫 ALGORITMO MINIMAX NO IMPLEMENTADO" +
        "\n" + "="*60 +
        "\n\nPara usar la estrategia Minimax debe implementarla primero." +
        "\n\nInstrucciones:" +
        "\n1. Abra el archivo 'estrategias.py'" +
        "\n2. Busque la función 'estrategia_minimax()'" +
        "\n3. Elimine la línea 'raise NotImplementedError(...)'" +
        "\n4. Implemente el algoritmo minimax" +
        "\n\nMientras tanto, use la 'Estrategia Aleatoria'." +
        "\n" + "="*60
    )
