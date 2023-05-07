import pytest
from snake.game.entities import Snake, Direction, Food


@pytest.fixture
def snake():
    yield Snake((5, 5))


@pytest.fixture
def food():
    yield Food((0, 0))


def test_snake_goes_left(snake):
    snake.move(Direction.LEFT)
    assert snake.current_direction == Direction.LEFT
    assert snake.body.pop() == (4, 5)
    assert len(snake.body) == 0


def test_snake_goes_right(snake):
    snake.move(Direction.RIGHT)
    assert snake.current_direction == Direction.RIGHT
    assert snake.body.pop() == (6, 5)
    assert len(snake.body) == 0


def test_snake_goes_up(snake):
    snake.move(Direction.UP)
    assert snake.current_direction == Direction.UP
    assert snake.body.pop() == (5, 4)
    assert len(snake.body) == 0


def test_snake_goes_down(snake):
    snake.move(Direction.DOWN)
    assert snake.current_direction == Direction.DOWN
    assert snake.body.pop() == (5, 6)
    assert len(snake.body) == 0


def test_snake_eats_left(snake, food):
    snake.move(Direction.LEFT)
    snake.eat(food)
    assert snake.body.pop() == (4, 5)
    assert snake.body.pop() == (5, 5)
    assert len(snake.body) == 0


def test_snake_eats_right(snake, food):
    snake.move(Direction.RIGHT)
    snake.eat(food)
    assert snake.body.pop() == (6, 5)
    assert snake.body.pop() == (5, 5)
    assert len(snake.body) == 0


def test_snake_eats_up(snake, food):
    snake.move(Direction.UP)
    snake.eat(food)
    assert snake.body.pop() == (5, 4)
    assert snake.body.pop() == (5, 5)
    assert len(snake.body) == 0


def test_snake_eats_down(snake, food):
    snake.move(Direction.DOWN)
    snake.eat(food)
    assert snake.body.pop() == (5, 6)
    assert snake.body.pop() == (5, 5)
    assert len(snake.body) == 0
