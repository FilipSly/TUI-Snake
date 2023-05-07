from collections import deque
from enum import Enum
from snake.game.grid import Position


class Food:
    position: Position

    def __init__(self, position: Position):
        """
        Initialise some food at the given position
        """
        self.position = position

    @staticmethod
    def display() -> str:
        """
        Returns the character
        """
        return '?'

    @staticmethod
    def value() -> int:
        """
        Returns the value of the food
        """
        return 0


class GreenApple(Food):
    @staticmethod
    def display() -> str:
        # TODO: how does a green apple look like?
        pass

    @staticmethod
    def value() -> int:
        # TODO: how much is a green apple worth?
        pass


# TODO: Implement a red apple


class Direction(Enum):
    """Enumeration of the snake's direction."""
    UNKNOWN = 0
    """The snake is stationary."""
    LEFT = 1
    """The snake is going left."""
    RIGHT = 2
    """The snake is going right."""
    UP = 3
    """The snake is going up."""
    DOWN = 4
    """The snake is going down."""


class Snake:
    body: deque[Position]
    """Body of the snake comprised by all the positions in the grid it spans"""
    current_direction: Direction
    """The current direction the snake is going"""

    def __init__(self, start: Position):
        """
        Initialises the snake
        """
        # TODO: initialise a snake!
        #       - give its body a form...
        #           initialise a deque with the only location the snake covers
        #       - is is stationary or is it moving?
        pass

    def move(self, direction: Direction) -> Position:
        """
        Move the snake by one block

        Returns:
            the new position of the snake's head
        """
        # TODO: implement logic to move the snake by one block.
        #       To minimise the performance impact we could just move the
        #       last block of the body to the top and assign it the new
        #       position in the grid.
        #       Update the snake's current direction, if necessary.
        pass

    def eat(self, food: Food):
        """
        Let the snake eat some food
        """
        # TODO: grow the snake's tail!
        pass
