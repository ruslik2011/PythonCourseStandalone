import pytest
import ast
from ast import Assign
import subprocess


@pytest.mark.ch01ex01
class TestChatper01ex01:
    def test_solution_01_existance(self):
        try:
            import course.chapter_01.solutions.solution_1 as solution_1
        except ImportError:
            pytest.fail("Failed to import 'solution_1.py'")

    def test_solution_01_variables_type(self):
        try:
            from course.chapter_01.solutions.solution_1 import age, is_student, name
        except ImportError:
            pytest.fail("variables age, is_student or name are not exist")
        assert isinstance(age, int), "Variable age has not integer type"
        assert isinstance(is_student, bool), "Variable is_student has not bool type"
        assert isinstance(name, str), "Variable name has not string type"


@pytest.mark.ch01ex02
class TestChatper01ex02:
    def test_solution_02_existance(self):
        try:
            import course.chapter_01.solutions.solution_2 as solution_2
        except ImportError:
            pytest.fail("Failed to import 'solution_2.py'")

    def test_solution_02_contant(self):
        try:
            file = open("course/chapter_01/solutions/solution_2.py", "r")
            tree = ast.parse(file.read())
        except FileExistsError:
            pytest.fail("Failed to import 'solution_2.py'")

        for e in tree.body:
            assert isinstance(e, Assign), "Solution does not have two assigment"


@pytest.mark.ch01ex03
class TestChatper01ex03:
    def test_solution_03_existance(self):
        try:
            import course.chapter_01.solutions.solution_3 as solution_3
        except ImportError:
            pytest.fail("Failed to import 'solution_3.py'")

    def test_solution_03_variables_type(self):
        try:
            from course.chapter_01.solutions.solution_3 import (
                integer_literal,
                float_literal,
                string_literal,
                bool_literal,
            )
        except ImportError:
            pytest.fail(
                "variables integer_literal, float_literal, string_literal or bool_literal are not exist"
            )
        assert isinstance(
            integer_literal, int
        ), "Variable integer_literal has not integer type"
        assert isinstance(bool_literal, bool), "Variable bool_literal has not bool type"
        assert isinstance(
            string_literal, str
        ), "Variable string_literal has not string type"
        assert isinstance(
            float_literal, float
        ), "Variable float_literal has not float type"


@pytest.mark.ch01ex04
class TestChatper01ex04:
    def test_solution_04_existance(self):
        try:
            import course.chapter_01.solutions.solution_4 as solution_4
        except ImportError:
            pytest.fail("Failed to import 'solution_4.py'")

    def test_solution_04_variables_type(self):
        try:
            from course.chapter_01.solutions.solution_4 import result
        except ImportError:
            pytest.fail("variables result are not exist")
        assert result is None, "Variable result has not None"


@pytest.mark.ch01ex05
class TestChatper01ex04:
    def test_solution_05_existance(self):
        try:
            import course.chapter_01.solutions.solution_5 as solution_5
        except ImportError:
            pytest.fail("Failed to import 'solution_5.py'")

    def test_solution_05_variables_type(self):
        try:
            from course.chapter_01.solutions.solution_5 import sleep_time, name
        except ImportError:
            pytest.fail("variables sleep_time are not exist")
        assert isinstance(sleep_time, int), "Variable sleep_time has not int type"
        assert isinstance(name, str), "Variable name has not str type"

    @pytest.mark.parametrize("solution_runner", 
                             [[1, 5, ""]], 
                             indirect=True)
    def test_solution_05_output(self, solution_runner):
        from course.chapter_01.solutions.solution_5 import sleep_time, name
        solution_out = solution_runner
        expected_output = f"Hello {name} ! Вы спали всего {sleep_time} часов. Вам нужно больше спать!\n"
        assert solution_out == expected_output
