import pytest


class TestChapter02ex01: 
    @pytest.mark.solution_runner(["14", "21"], 0.1)
    def test_solution_1_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = ["False\n", "True\n"]
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"
            

class TestChapter02ex02:   
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_2_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "False\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner("Hello!", 0.1)
    def test_solution_2_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "True\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
class TestChapter02ex03:    
    @pytest.mark.solution_runner(
        ["-10",
         "0",
         "21"], 0.1
    )
    def test_solution_3_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = [
            "Очень холодно, одевайтесь теплее.\n",
            "На улице прохладно, возьмите с собой куртку.\n",
            "На улице тепло, наденьте что-то удобное.\n"
        ]
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"

class TestChapter02ex04:    
    @pytest.mark.solution_runner(["1204", "141"], 0.1)
    def test_solution_4_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = [
            "Число четное\n",
            "Число нечетное\n"
        ]
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"


class TestChapter02ex05:    
    @pytest.mark.solution_runner(
        ["50",
         "100",
         "-21",
         "111"
        ], 0.1
    )
    def test_solution_5_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = [
            "Удовлетворительно\n",
            "Отлично\n",
            "\n",
            "\n"
        ]
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"

class TestChapter02ex06:
    @pytest.mark.solution_runner(
        [
        "3",
        "23",
        "-21",
        "111"
        ], 0.1
    )
    def test_solution_6_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = [
            "Доброй ночи!\n",
            "Доброй ночи!\n",
            "",
            ""
        ]
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"

    

class TestChapter02ex07:
    @pytest.mark.solution_runner([
        "красный",
        "желтый",
        "зеленый"
    ], 0.1
    )
    def test_solution_7_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = [
            "стой\n",
            "готовься\n",
            "иди\n"
            ]
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"


class TestChapter02ex08:
    @pytest.mark.solution_runner([
        ("21", "Y"),
        ("21", "N"),
        ("-14", "q")
        ], 0.1
        )
    def test_solution_8_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = [
            "Добро пожаловать в клуб!\n",
            "Извините, вход запрещен.\n",
            "Введите корректные значения.\n"            
        ]
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"


class TestChapter02ex09:
    @pytest.mark.solution_runner([
        ("12", "70"),
        ("32", "50"),
        ("10", "50"),
        ("50", "20")
    ], 0.1)
    def test_solution_9_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = [
            "Числа вне диапазона.\n",
            "Числа вне диапазона.\n",
            "Числа в диапазоне.\n",
            "Числа в диапазоне.\n"
        ]
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"


class TestChapter02ex10:
    @pytest.mark.solution_runner([
        ("True", "True"),
        ("True", "False"),
        ("False", "G!!"),
        ("True", "Mur")
        ], 0.1)
    def test_solution_10_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = [
            "Товар будет отправлен.\n",
            "Товар не может быть отправлен.\n",
            "Товар не может быть отправлен.\n",
            "Товар не может быть отправлен.\n"
        ]
                           
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"

class TestChapter02ex11:
    @pytest.mark.solution_runner([
        ("4", "5"),
        ("1", "9"),
        ("3", "5"),
        ("5", "2")
        ], 0.1)
    def test_solution_11_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = [
            "Продвинутая математика\nОперационные системы\nАлгоритмы и структуры данных\n",
            "",
            "Операционные системы\n",
            "Продвинутая математика\n"
            ]
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"

class TestChapter02ex12:
    @pytest.mark.solution_runner([("4", "5", "6"),
                                  ("4", "15", "3"),
                                  ("14", "5", "6"),
                                  ("4", "5", "16")], 0.1)
    def test_solution_12_output_1(self, solution_runner):
        expected_output = ["Такой треугольник существует\n",
                           "Такой треугольник не существует\n",
                           "Такой треугольник не существует\n",
                           "Такой треугольник не существует\n"
                           ]
        solution_out = solution_runner
        for expected, solution in zip(expected_output, solution_out):
            assert (
                expected == solution
            ), f"expected output is `{expected}` \n Your program gives `{solution}`"