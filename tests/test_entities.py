import pytest
from snake.game.entities import Snake, Direction, Food


@pytest.fixture
def snake():
    yield Snake((5, 5))


@pytest.fixture
def food():
    yield Food((0, 0))


def test_snake_goes_left(snake):
    next_pos = snake.move(Direction.LEFT)
    assert snake.current_direction == Direction.LEFT
    assert next_pos == (4, 5)
    assert snake.body.pop() == (4, 5)
    assert len(snake.body) == 0


def test_snake_goes_right(snake):
    next_pos = snake.move(Direction.RIGHT)
    assert snake.current_direction == Direction.RIGHT
    assert next_pos == (6, 5)
    assert snake.body.pop() == (6, 5)
    assert len(snake.body) == 0


def test_snake_goes_up(snake):
    next_pos = snake.move(Direction.UP)
    assert snake.current_direction == Direction.UP
    assert next_pos == (5, 4)
    assert snake.body.pop() == (5, 4)
    assert len(snake.body) == 0


def test_snake_goes_down(snake):
    next_pos = snake.move(Direction.DOWN)
    assert snake.current_direction == Direction.DOWN
    assert next_pos == (5, 6)
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
