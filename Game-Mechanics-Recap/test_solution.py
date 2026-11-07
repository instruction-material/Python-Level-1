import ast
import math
import runpy
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch

SOLUTION = Path(__file__).with_name("solution") / "main.py"


class TraceTurtle:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.heading = 0
        self.moves = []
        self.phase = 0

    def forward(self, distance):
        if len(self.moves) >= 300:
            raise AssertionError("A reference loop exceeded the movement budget")
        self.x += distance * math.cos(math.radians(self.heading))
        self.y += distance * math.sin(math.radians(self.heading))
        self.moves.append((self.phase, round(self.x, 8), round(self.y, 8)))

    def penup(self):
        pass

    def pendown(self):
        pass

    def goto(self, x, y):
        self.x, self.y = x, y
        self.phase += 1

    def setheading(self, angle):
        self.heading = angle

    def xcor(self):
        return self.x

    def ycor(self):
        return self.y


class RecapReferenceTests(unittest.TestCase):
    def test_each_original_exercise_terminates_at_its_own_limit(self):
        pen = TraceTurtle()
        screen = types.SimpleNamespace(mainloop=lambda: None)
        turtle = types.ModuleType("turtle")
        turtle.Turtle = lambda: pen
        turtle.Screen = lambda: screen
        with patch.dict(sys.modules, {"turtle": turtle}):
            result = runpy.run_path(str(SOLUTION), run_name="__main__")
        phases = [[move for move in pen.moves if move[0] == i] for i in range(3)]
        self.assertEqual([len(moves) for moves in phases], [100, 51, 101])
        self.assertEqual(result["counter"], 100)
        self.assertEqual(phases[0][-1][1:], (100.0, 0.0))
        self.assertEqual(phases[1][-1][1:], (0.0, 51.0))
        self.assertEqual(phases[2][-1][1:], (-101.0, 0.0))
        self.assertEqual(phases[1][-2][1:], (0.0, 50.0))
        self.assertEqual(phases[2][-2][1:], (-100.0, 0.0))

    def test_either_strict_boundary_stops_the_actual_final_condition(self):
        program = ast.parse(SOLUTION.read_text())
        final_loop = [node for node in program.body if isinstance(node, ast.While)][-1]
        condition = next(node.test for node in final_loop.body if isinstance(node, ast.If))
        expression = compile(ast.Expression(condition), str(SOLUTION), "eval")
        for x, y, expected in [
            (0, 51, True), (-101, 0, True), (-101, 51, True),
            (0, 0, False), (-100, 50, False), (101, 0, False)
        ]:
            with self.subTest(x=x, y=y):
                pen = types.SimpleNamespace(xcor=lambda: x, ycor=lambda: y)
                self.assertIs(eval(expression, {"drawing_turtle": pen}), expected)


if __name__ == "__main__":
    unittest.main()
