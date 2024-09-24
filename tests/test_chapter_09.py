import pytest


class TestChapter09ex01:
    @pytest.mark.solution_runner("Я изучаю язык программирования Python", 0.1)
    def test_solution_1_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "5\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Привет мир", 0.1)
    def test_solution_1_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "2\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex02:
    @pytest.mark.solution_runner("Программирование — это интересно!", 0.1)
    def test_solution_2_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Количество гласных букв: 13\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Я люблю Питон!", 0.1)
    def test_solution_2_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Количество гласных букв: 5\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex03:
    @pytest.mark.solution_runner("Python", 0.1)
    def test_solution_3_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "nohtyP\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Программирование", 0.1)
    def test_solution_3_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "еинавориммаргорП\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex04:
    @pytest.mark.solution_runner("    Привет, как дела?    ", 0.1)
    def test_solution_4_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Результат: 'Привет, как дела?'\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("     Программирование это круто!   ", 0.1)
    def test_solution_4_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Результат: 'Программирование это круто!'\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex05:
    @pytest.mark.solution_runner("12345", 0.1)
    def test_solution_5_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Состоит только из цифр: True\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("123a45", 0.1)
    def test_solution_5_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Состоит только из цифр: False\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex06:
    @pytest.mark.solution_runner("Я изучаю Python", 0.1)
    def test_solution_6_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Результат: Я-изучаю-Python\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Программирование это круто", 0.1)
    def test_solution_6_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Результат: Программирование-это-круто\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex07:
    @pytest.mark.solution_runner("Python3 - это круто!", 0.1)
    def test_solution_7_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Количество букв: 14\nКоличество цифр: 1\nКоличество других символов: 5\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Я изучаю Python 3!", 0.1)
    def test_solution_7_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Количество букв: 13\nКоличество цифр: 1\nКоличество других символов: 4\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex08:
    @pytest.mark.solution_runner("топот", 0.1)
    def test_solution_8_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Палиндром\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Программирование", 0.1)
    def test_solution_8_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Не палиндром\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex09:
    @pytest.mark.solution_runner("Python 3 - это 100% круто!", 0.1)
    def test_solution_9_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Python  - это % круто!\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Программирование 321 сложно", 0.1)
    def test_solution_9_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Программирование  сложно\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex10:
    @pytest.mark.solution_runner(("Программирование - это круто!\nр"), 0.1)
    def test_solution_10_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "'р' встречается 4 раз(а).\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Python это мощно!\nо"), 0.1)
    def test_solution_10_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "'о' встречается 3 раз(а).\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex11:
    @pytest.mark.solution_runner("Python это мощный язык программирования", 0.1)
    def test_solution_11_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Количество слов: 5\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Программирование это круто", 0.1)
    def test_solution_11_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Количество слов: 3\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex12:
    @pytest.mark.solution_runner("яблоко банан вишня", 0.1)
    def test_solution_12_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "яблоко, банан, вишня\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Программирование это круто", 0.1)
    def test_solution_12_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Программирование, это, круто\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex13:
    @pytest.mark.solution_runner("Программирование это круто", 0.1)
    def test_solution_13_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "круто это Программирование\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Я изучаю Python", 0.1)
    def test_solution_13_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Python изучаю Я\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex14:
    @pytest.mark.solution_runner(("Python это мощный инструмент\n-"), 0.1)
    def test_solution_14_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Python-это-мощный-инструмент\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Программирование это круто\n*"), 0.1)
    def test_solution_14_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Программирование*это*круто\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex15:
    @pytest.mark.solution_runner("привет мир это python3", 0.1)
    def test_solution_15_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Результат: Привет Мир Это python3\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("это крутой инструмент", 0.1)
    def test_solution_15_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Результат: Это Крутой Инструмент\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex16:
    @pytest.mark.solution_runner("Hello world", 0.1)
    def test_solution_16_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "olleH dlrow\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Привет мир", 0.1)
    def test_solution_16_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "тевирП рим\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex17:
    @pytest.mark.solution_runner("Я изучаю Python", 0.1)
    def test_solution_17_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[1, 6, 6]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Программирование это круто", 0.1)
    def test_solution_17_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[16, 3, 5]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter09ex18:
    @pytest.mark.solution_runner("Я изучаю Python", 0.1)
    def test_solution_18_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Результат: Я ию Pn\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Программирование это круто", 0.1)
    def test_solution_18_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Результат: Пе эо ко\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
