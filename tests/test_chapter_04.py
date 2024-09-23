import pytest

class TestChapter04ex01:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_1_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "".join([str(i) + "\n" for i in range(10, 0, -1)]) + "Поехали!\n"
        )
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter04ex02:
    @pytest.mark.solution_runner("5", 0.1)
    def test_solution_2_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "*****\n****\n***\n**\n*\n"
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter04ex03:
    @pytest.mark.solution_runner("5", 0.1)
    def test_solution_3_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "15\n"
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter04ex04:
    @pytest.mark.solution_runner("4", 0.1)
    def test_solution_4_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "30\n"
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter04ex05:
    @pytest.mark.solution_runner("21", 0.1)
    def test_solution_5_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "1\n3\n7\n21\n"
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter04ex06:
    @pytest.mark.solution_runner("17", 0.1)
    def test_solution_6_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "17 - простое\n"
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter04ex07:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_7_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "Треугольные числа:\n1\n3\n6\n10\n15\n21\n28\n36\n45\n55\n"
        )
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter04ex08:
    @pytest.mark.solution_runner("10", 0.1)
    def test_solution_8_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "Числа Фибоначчи:\n1\n1\n2\n3\n5\n8\n13\n21\n34\n55\n"
        )
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter04ex09:
    @pytest.mark.solution_runner(("2", "3", "10"), 0.1)
    def test_solution_9_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "2\n3\n5\n8\n13\n21\n34\n55\n89\n144\n"
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
