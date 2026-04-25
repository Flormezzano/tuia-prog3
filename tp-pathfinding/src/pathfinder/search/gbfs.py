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

        h = GreedyBestFirstSearch.heuristic(root.state, grid.end)
        frontier.add(root, h)

        while not frontier.is_empty():
            node = frontier.pop()
            
            if grid.objective_test(node.state):
                return Solution(node, reached)

            for action in grid.actions(node.state):
                new_state = grid.result(node.state, action)
                new_cost = node.cost + grid.individual_cost(node.state, action)

                if new_state not in reached or new_cost < reached[new_state]:
                    new_node = Node(
                        "",
                        state=new_state,
                        cost=new_cost,
                        parent=node,
                        action=action
                    )

                    reached[new_state] = new_cost
                    
                    h = GreedyBestFirstSearch.heuristic(new_state, grid.end)
                    frontier.add(new_node, h)

        return NoSolution(reached)