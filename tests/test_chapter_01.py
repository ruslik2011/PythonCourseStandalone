import pytest
import ast
from ast import Assign


class TestChapter01ex01:
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


class TestChapter01ex02:
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


class TestChapter01ex03:
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


class TestChapter01ex04:
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


class TestChapter01ex05:
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

    @pytest.mark.solution_runner("", 0.1)
    def test_solution_05_output(self, solution_runner):
        from course.chapter_01.solutions.solution_5 import sleep_time, name

        solution_out = solution_runner
        expected_output = f"Hello {name} ! Вы спали всего {sleep_time} часов. Вам нужно больше спать!\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter01ex06:
    @pytest.mark.solution_runner("Tony", 0.1)
    def test_solution_06_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "I know your name now. Your name is Tony .\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter01ex07:
    @pytest.mark.solution_runner(("Math", "4", "4.5"), 0.1)
    def test_solution_07_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Math - ваш любимый предмет . \
Судя по последней оценке 4 в журнале вы стараетесь. \
В этой четверти ваш средний бал станет выше 4.5 \
благодаря вашему упорству.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter01ex08:
    @pytest.mark.solution_runner(("4", "4"), 0.1)
    def test_solution_08_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "4 + 4 = 8\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.xfail
    @pytest.mark.solution_runner(("4.5", "4.5"), 0.1)
    def test_solution_08_typing(self, solution_runner):
        solution_out = solution_runner
        expected_output = "4.5 + 4.5 = 9.0\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter01ex09:
    @pytest.mark.solution_runner(("6.0", "4.0"), 0.1)
    def test_solution_09_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "P = 20.0\nS = 24.0\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter01ex10:
    @pytest.mark.solution_runner("15", 0.1)
    def test_solution_10_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "59.0\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter01ex11:
    @pytest.mark.solution_runner(
        [
            ("14", "3"),
            ("16", "4"),
        ],
        0.1,
    )
    def test_solution_11_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = ["2\n", "0\n"]
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"

    @pytest.mark.xfail
    @pytest.mark.solution_runner(["4.5", "4.5"], 0.1)
    def test_solution_11_typing(self, solution_runner):
        solution_out = solution_runner
        expected_output = "0"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter01ex12:
    @pytest.mark.solution_runner([("3", "3"), ("4", "4")], 0.1)
    def test_solution_12_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = ["27\n", "256\n"]
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"


class TestChapter01ex13:
    @pytest.mark.solution_runner("14", 0.1)
    def test_solution_13_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "24\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.xfail
    @pytest.mark.solution_runner("50.0", 0.1)
    def test_solution_13_typing(self, solution_runner):
        solution_out = solution_runner
        expected_output = "60.0"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter01ex14:
    @pytest.mark.solution_runner("Tony", 0.1)
    def test_solution_14_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Greeting you, Tony! Have a nice day!\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter01ex15:
    def pine(self, char: str):
        peek = [" " * (5 - i) + char * (i * 2 + 1) for i in range(3)]
        middle = [" " * (4 - i) + char * (i * 2 + 3) for i in range(4)]
        bottom = [" " * (3 - i) + char * (i * 2 + 5) for i in range(4)]
        return "\n".join(peek + middle + bottom) + "\n"

    @pytest.mark.solution_runner("+", 0.1)
    def test_solution_15_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = self.pine("+")
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("y", 0.1)
    def test_solution_15_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = self.pine("y")
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter01ex16:
    @pytest.mark.solution_runner(
        [
            "12.234",
            "12.999",
        ],
        0.1,
    )
    def test_solution_16_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = ["12.0\n", "12.0\n"]

        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}`\n Your program gives `{solution}`"


class TestChapter01ex17:
    @pytest.mark.solution_runner(
        [
            ("2", "3", "4"),
            ("5", "3.23", "5"),
        ],
        0.1,
    )
    def test_solution_17_int_input(self, solution_runner):
        solution_out = [float(i) for i in solution_runner]
        expected_output = (3.0, 4.41)
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"


class TestChapter01ex18:
    @pytest.mark.solution_runner([("21", "3"), ("1345", "10")], 0.1)
    def test_solution_18_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            f"Яблок у каждого из 3 друзей: 7\nЯблок в корзине: 0\n",
            f"Яблок у каждого из 10 друзей: 134\nЯблок в корзине: 5\n",
        )
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"
