import pytest


class TestChatper02ex01:    
    @pytest.mark.solution_runner(2, 1, 0.1, ["14"])
    def test_solution_1_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "False\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 1, 0.1, ["21"])
    def test_solution_1_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "True\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChatper02ex02:    
    @pytest.mark.solution_runner(2, 2, 0.1, [""])
    def test_solution_2_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "False\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 2, 0.1, ["Hello!"])
    def test_solution_2_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "True\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
class TestChatper02ex03:    
    @pytest.mark.solution_runner(2, 3, 0.1, ["-10"])
    def test_solution_3_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Очень холодно, одевайтесь теплее.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 3, 0.1, ["0"])
    def test_solution_3_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "На улице прохладно, возьмите с собой куртку.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 3, 0.1, ["21"])
    def test_solution_3_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "На улице тепло, наденьте что-то удобное.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

class TestChatper02ex04:    
    @pytest.mark.solution_runner(2, 4, 0.1, ["1204"])
    def test_solution_4_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Число четное\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 4, 0.1, ["141"])
    def test_solution_4_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Число нечетное\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChatper02ex05:    
    @pytest.mark.solution_runner(2, 5, 0.1, ["50"])
    def test_solution_5_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Удовлетворительно\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 5, 0.1, ["100"])
    def test_solution_5_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Отлично\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 5, 0.1, ["-21"])
    def test_solution_5_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 5, 0.1, ["111"])
    def test_solution_5_output_4(self, solution_runner):
        solution_out = solution_runner
        expected_output = "\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

class TestChatper02ex06:
    @pytest.mark.solution_runner(2, 6, 0.1, ["3"])
    def test_solution_6_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Доброй ночи!\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 6, 0.1, ["23"])
    def test_solution_6_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Доброй ночи!\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.xfail
    @pytest.mark.solution_runner(2, 6, 0.1, ["-21"])
    def test_solution_6_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Доброй ночи!\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 6, 0.1, ["111"])
    def test_solution_6_output_4(self, solution_runner):
        solution_out = solution_runner
        expected_output = ""
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChatper02ex07:
    @pytest.mark.solution_runner(2, 7, 0.1, ["красный"])
    def test_solution_7_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "стой\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 7, 0.1, ["желтый"])
    def test_solution_7_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "готовься\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(2, 7, 0.1, ["зеленый"])
    def test_solution_7_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "иди\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

class TestChatper02ex08:
    @pytest.mark.solution_runner(2, 8, 0.1, ["21", "Y"])
    def test_solution_8_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Добро пожаловать в клуб!\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 8, 0.1, ["21", "N"])
    def test_solution_8_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Извините, вход запрещен.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(2, 8, 0.1, ["-14", "q"])
    def test_solution_8_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Введите корректные значения.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChatper02ex09:
    @pytest.mark.solution_runner(2, 9, 0.1, ["12", "70"])
    def test_solution_9_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Числа вне диапазона.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 9, 0.1, ["32", "50"])
    def test_solution_9_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Числа вне диапазона.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 9, 0.1, ["10", "50"])
    def test_solution_9_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Числа в диапазоне.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 9, 0.1, ["50", "20"])
    def test_solution_9_output_4(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Числа в диапазоне.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChatper02ex10:
    @pytest.mark.solution_runner(2, 10, 0.1, ["True", "True"])
    def test_solution_10_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Товар будет отправлен.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 10, 0.1, ["True", "False"])
    def test_solution_10_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Товар не может быть отправлен.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 10, 0.1, ["False", "G!!"])
    def test_solution_10_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Товар не может быть отправлен.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 10, 0.1, ["True", "Mur"])
    def test_solution_10_output_4(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Товар не может быть отправлен.\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChatper02ex11:
    @pytest.mark.solution_runner(2, 11, 0.1, ["4", "5"])
    def test_solution_11_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Продвинутая математика\nОперационные системы\nАлгоритмы и структуры данных\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 11, 0.1, ["1", "9"])
    def test_solution_11_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = ""
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 11, 0.1, ["3", "5"])
    def test_solution_11_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Операционные системы\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
        
    @pytest.mark.solution_runner(2, 11, 0.1, ["5", "2"])
    def test_solution_11_output_4(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Продвинутая математика\n"
        assert (
            solution_out == expected_output
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

class TestChatper02ex12:
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
            ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"