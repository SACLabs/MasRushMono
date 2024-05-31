import unittest
from snake import move, go_up, go_down, go_left, go_right


class TestSnakeGame(unittest.TestCase):
    def test_move_up(self):
        head_starting_position = (0, 0)
        go_up()
        move()
        self.assertEqual(head_starting_position[1] + 20, head.ycor())

    def test_move_down(self):
        head_starting_position = (0, 0)
        go_down()
        move()
        self.assertEqual(head_starting_position[1] - 20, head.ycor())

    def test_move_left(self):
        head_starting_position = (0, 0)
        go_left()
        move()
        self.assertEqual(head_starting_position[0] - 20, head.xcor())

    def test_move_right(self):
        head_starting_position = (0, 0)
        go_right()
        move()
        self.assertEqual(head_starting_position[0] + 20, head.xcor())

    def test_exit_on_failed(self):
        # TODO: @yaoshengyue
        pass


if __name__ == "__main__":
    unittest.main()
