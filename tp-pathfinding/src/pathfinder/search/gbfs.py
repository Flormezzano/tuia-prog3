from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    
    @staticmethod
    def heuristic(pos: tuple[int, int], goal: tuple[int, int]) -> int:
        """Distancia Manhattan"""
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
    
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()

         # Agregar nodo inicial con prioridad heurística
        h = GreedyBestFirstSearch.heuristic(root.state, grid.end)
        frontier.add(root, h)

        while not frontier.is_empty():
            current = frontier.pop()

            # Objetivo
            if grid.objective_test(current.state):
                return Solution(current, reached)

            # Expandir
            for action in grid.actions(current.state):
                new_state = grid.result(current.state, action)
                new_cost = current.cost + grid.individual_cost(current.state, action)

                if new_state not in reached:
                    child = Node(
                        "",
                        state=new_state,
                        cost=new_cost,
                        parent=current,
                        action=action
                    )

                    reached[new_state] = new_cost

                    # CLAVE: solo heurística
                    h = GreedyBestFirstSearch.heuristic(new_state, grid.end)
                    frontier.add(child, h)

        return NoSolution(reached)