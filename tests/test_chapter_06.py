import pytest
import ast


class TestChapter06ex01:
    @pytest.mark.solution_runner("5", 0.1)
    def test_solution_1_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "0\n01\n012\n0123\n01234\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    def test_solution_uses_loop(self):
        # Проверка, что программа использует цикл
        with open("course/chapter_06/solutions/solution_1.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                break
        else:
            pytest.fail("The solution must use a 'for' loop")


class TestChapter06ex02:
    @pytest.mark.solution_runner("5", 0.1)
    def test_solution_2_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "2.283333333333333\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

class TestChapter06ex03:
    @pytest.mark.solution_runner("5", 0.1)
    def test_solution_3_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "1\n22\n333\n4444\n55555\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    def test_solution_uses_loop(self):
        # Проверка, что программа использует цикл
        with open("course/chapter_06/solutions/solution_3.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                break
        else:
            pytest.fail("The solution must use a 'for' loop")


class TestChapter06ex04:
    @pytest.mark.solution_runner("5", 0.1)
    def test_solution_4_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "54321\n5432\n543\n54\n5\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    def test_solution_uses_loop(self):
        # Проверка, что программа использует цикл
        with open("course/chapter_06/solutions/solution_4.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                break
        else:
            pytest.fail("The solution must use a 'for' loop")


class TestChapter06ex05:
    @pytest.mark.solution_runner("20", 0.1)
    def test_solution_5_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "2\n3\n5\n7\n11\n13\n17\n19\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"




class TestChapter06ex06:
    @pytest.mark.solution_runner("100", 0.1)
    def test_solution_6_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "1060\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"



class TestChapter06ex07:
    @pytest.mark.solution_runner("", 10)
    def test_solution_7_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "200 375 425\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    def test_solution_uses_nested_loops(self):
        # Проверка на использование вложенных циклов
        with open("course/chapter_06/solutions/solution_7.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.For) and any(isinstance(n, ast.For) for n in ast.iter_child_nodes(node)):
                break
        else:
            pytest.fail("The solution must use nested 'for' loops")


class TestChapter06ex08:
    @pytest.mark.solution_runner(("3", "123", "654", "789"), 0.1)
    def test_solution_8_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "45\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        

    @pytest.mark.solution_runner(("2", "111", "222"), 0.1)
    def test_solution_8_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "9\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("4", "987", "654", "321", "123"), 0.1)
    def test_solution_8_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "51\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"



class TestChapter06ex09:
    @pytest.mark.solution_runner(("4", "5"), 0.1)
    def test_solution_9_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "1  5  9  13 17\n"
            "2  6  10 14 18\n"
            "3  7  11 15 19\n"
            "4  8  12 16 20\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    def test_solution_uses_nested_loops(self):
        # Проверка на использование вложенных циклов
        with open("course/chapter_06/solutions/solution_9.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.For) and any(isinstance(n, ast.For) for n in ast.iter_child_nodes(node)):
                break
        else:
            pytest.fail("The solution must use nested 'for' loops")

    @pytest.mark.solution_runner(("3", "4"), 0.1)
    def test_solution_9_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "1  4  7  10\n"
            "2  5  8  11\n"
            "3  6  9  12\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("2", "3"), 0.1)
    def test_solution_9_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "1 3 5\n"
            "2 4 6\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter06ex10:
    @pytest.mark.solution_runner("5", 0.1)
    def test_solution_10_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "1 1 1 1 1\n"
            "1 2 2 2 1\n"
            "1 2 3 2 1\n"
            "1 2 2 2 1\n"
            "1 1 1 1 1\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


    def test_solution_uses_nested_loops(self):
        # Проверка на использование вложенных циклов
        with open("course/chapter_06/solutions/solution_10.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.For) and any(isinstance(n, ast.For) for n in ast.iter_child_nodes(node)):
                break
        else:
            pytest.fail("The solution must use nested 'for' loops")
            

    @pytest.mark.solution_runner("3", 0.1)
    def test_solution_10_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "1 1 1\n"
            "1 2 1\n"
            "1 1 1\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("4", 0.1)
    def test_solution_10_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "1 1 1 1\n"
            "1 2 2 1\n"
            "1 2 2 1\n"
            "1 1 1 1\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

