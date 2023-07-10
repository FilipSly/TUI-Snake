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
        return '🍏'

    @staticmethod
    def value() -> int:
        return 1


class RedApple(Food):
    @staticmethod
    def display() -> str:
        return "🍎"

    @staticmethod
    def value() -> int:
        return 2


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
        self.body = deque([start])
        self.current_direction = Direction.UNKNOWN
        self.score = 0

    def move(self, direction: Direction) -> Position:
        """
        Move the snake by one block
        Returns:
            the new position of the snake's head
        """
        n = self.body.popleft()
        self.last_seen = n
        x, y = n[0], n[1]
        i = n
        if direction == Direction.LEFT:
            i = tuple([x - 1, y])
        elif direction == Direction.RIGHT:
            i = tuple([x + 1, y])
        elif direction == Direction.UP:
            i = tuple([x, y - 1])
        elif direction == Direction.DOWN:
            i = tuple([x, y + 1])
        self.body.append(i)
        self.current_direction = direction
        return i

    def eat(self, food: Food):
        """
        Let the snake eat some food
        """
        self.body.appendleft(self.last_seen)
        self.score = self.score + food.value()
