import pytest
import ast

class TestChapter08ex01:
    @pytest.mark.solution_runner("Мария", 0.1)
    def test_solution_1_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "'Мария': 2\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Иван", 0.1)
    def test_solution_1_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "'Иван': 0\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    def test_solution_numbers_variable(self):
        # Проверка наличия переменной numbers и правильности значений
        with open("course/chapter_08/solutions/solution_1.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            names = False
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "names":
                        assert isinstance(node.value, ast.Tuple), "names должно быть списком"
                        values = [elt.n for elt in node.value.elts]
                        assert values == ['Иван', 'Ольга', 'Мария', 'Анна'], "Неверные значения в names"
                        names = True
                        break
            if names:
                break
        else:
            if not names:
                pytest.fail("Переменная 'names' не найдена")

class TestChapter08ex02:
    @pytest.mark.solution_runner("2", 0.1)
    def test_solution_2_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Число 2 встречается 3 раз(а).\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("7", 0.1)
    def test_solution_2_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Число 7 встречается 2 раз(а).\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

            
    def test_solution_numbers_variable(self):
        # Проверка наличия переменной numbers и правильности значений
        with open("course/chapter_08/solutions/solution_2.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            numbers = False
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "numbers":
                        assert isinstance(node.value, ast.Tuple), "numbers должно быть списком"
                        values = [elt.n for elt in node.value.elts]
                        assert values == [1, 2, 3, 2, 4, 2, 5, 7, 6, 8, 7, 6, 5, 1, 9], "Неверные значения в numbers"
                        numbers = True
                        break
            if numbers:
                break
        else:
            if not numbers:
                pytest.fail("Переменная 'numbers' не найдена")


class TestChapter08ex03:
    @pytest.mark.solution_runner(("2014\n8\n13\n2014\n3\n21"), 0.1)
    def test_solution_3_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "(2014, 8, 13) > (2014, 3, 21)\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("2020\n1\n1\n2020\n12\n31"), 0.1)
    def test_solution_3_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "(2020, 1, 1) < (2020, 12, 31)\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter08ex04:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_4_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "45\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
    
    def test_solution_numbers_variable(self):
        # Проверка наличия переменной numbers и правильности значений
        with open("course/chapter_08/solutions/solution_4.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            matrix = False
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "matrix":
                        assert isinstance(node.value, ast.List), "matrix должно быть списком"
                        values = [[elt.n for elt in row.elts] for row in node.value.elts]
                        assert values == [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "Неверные значения в matrix"
                        matrix = True
                        break
            if matrix:
                break
        else:
            if not matrix:
                pytest.fail("Переменная 'matrix' не найдена")


class TestChapter08ex05:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_5_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "1 4 7\n2 5 8\n3 6 9\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

            
    def test_solution_numbers_variable(self):
        # Проверка наличия переменной numbers и правильности значений
        with open("course/chapter_08/solutions/solution_5.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            matrix = False
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "matrix":
                        assert isinstance(node.value, ast.List), "matrix должно быть списком"
                        values = [[elt.n for elt in row.elts] for row in node.value.elts]
                        assert values == [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "Неверные значения в matrix"
                        matrix = True
                        break
            if matrix:
                break
        else:
            if not matrix:
                pytest.fail("Переменная 'matrix' не найдена")


class TestChapter08ex06:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_6_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "5\n8\n9\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    def test_solution_numbers_variable(self):
        # Проверка наличия переменной numbers и правильности значений
        with open("course/chapter_08/solutions/solution_6.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            matrix = False
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "matrix":
                        assert isinstance(node.value, ast.List), "matrix должно быть списком"
                        values = [[elt.n for elt in row.elts] for row in node.value.elts]
                        assert values == [[3, 5, 1], [7, 2, 8], [6, 9, 4]], "Неверные значения в matrix"
                        matrix = True
                        break
            if matrix:
                break
        else:
            if not matrix:
                pytest.fail("Переменная 'matrix' не найдена")

class TestChapter08ex07:
    @pytest.mark.solution_runner(("10.5\n22.7"), 0.1)
    def test_solution_7_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Вы находитесь в начальной точке маршрута\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("10.3\n22.8"), 0.1)
    def test_solution_7_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "0.2\n-0.1\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter08ex08:
    @pytest.mark.solution_runner(("Гарри Поттер\n500\nВойна и мир\n1225\n1984\n328\nМастер и Маргарита\n470\n"), 0.1)
    def test_solution_8_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Самая толстая книга: ('Война и мир', 1225)\nСуммарное число страниц: 2523\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Три мушкетера\n700\nГраф Монте-Кристо\n1200\n"), 0.1)
    def test_solution_8_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Самая толстая книга: ('Граф Монте-Кристо', 1200)\nСуммарное число страниц: 1900\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter08ex09:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_9_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "Дмитрий 4 3 5 4\n"
            "Ольга 3 2 3\n"
            "Михаил 5 4 4 5\n"
            "Арсений 5 2 4 2\n"
            "Ксения 5 5 5\n"
            "Марк 5 5 5\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter08ex10:
    @pytest.mark.solution_runner(("Анна\n12.5\nИван\n11.3\nОлег\n13.0\nМария\n10.9\n"), 0.1)
    def test_solution_10_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Победитель: Мария\nВремя: 10.9 минут\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Катя\n10.5\nЛена\n11.2\n"), 0.1)
    def test_solution_10_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Победитель: Катя\nВремя: 10.5 минут\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter08ex11:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_11_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "Дмитрий 4.0\n"
            "Ольга 2.7\n"
            "Михаил 4.5\n"
            "Арсений 3.2\n"
            "Ксения 5.0\n"
            "Марк 5.0\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter08ex12:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_12_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Арсений\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter08ex13:
    @pytest.mark.solution_runner("Марк", 0.1)
    def test_solution_13_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "5 5 5\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Дмитрий", 0.1)
    def test_solution_13_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "4 3 5 4\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Алексей", 0.1)
    def test_solution_13_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "такого ученика нет\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter08ex14:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_14_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "Дмитрий 4 3 5 4 5\n"
            "Ольга 3 2 3 5\n"
            "Михаил 5 4 4 5 5\n"
            "Арсений 5 2 4 2 5\n"
            "Ксения 5 5 5 5\n"
            "Марк 5 5 5 5\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
