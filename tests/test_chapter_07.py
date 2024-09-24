import pytest
import ast


class TestChapter07ex01:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_1_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Сумма элементов списка: 150\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    def test_solution_numbers_variable(self):
        # Проверка наличия переменной numbers и правильности значений
        with open("course/chapter_07/solutions/solution_1.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            numbers = False
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "numbers":
                        assert isinstance(node.value, ast.List), "numbers должно быть списком"
                        values = [elt.n for elt in node.value.elts]
                        assert values == [10, 20, 30, 40, 50], "Неверные значения в numbers"
                        numbers = True
                        break
            if numbers:
                break
        else:
            if not numbers:
                pytest.fail("Переменная 'numbers' не найдена")


class TestChapter07ex02:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_2_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "2, 4, 6, 8, 10\n1, 3, 5, 7, 9\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    def test_solution_numbers_variable(self):
        # Проверка наличия переменной numbers и правильности значений
        with open("course/chapter_07/solutions/solution_2.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            numbers = False
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "numbers":
                        assert isinstance(node.value, ast.List), "numbers должно быть списком"
                        values = [elt.n for elt in node.value.elts]
                        assert values == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Неверные значения в numbers"
                        numbers = True
                        break
            if numbers:
                break
        else:
            if not numbers:
                pytest.fail("Переменная 'numbers' не найдена")


class TestChapter07ex03:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_3_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Максимальный элемент: 21\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

            
    def test_solution_numbers_variable(self):
        # Проверка наличия переменной numbers и правильности значений
        with open("course/chapter_07/solutions/solution_3.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            numbers = False
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "numbers":
                        assert isinstance(node.value, ast.List), "numbers должно быть списком"
                        values = [elt.n for elt in node.value.elts]
                        assert values == [3, 17, 6, 12, 9, 21, 5], "Неверные значения в numbers"
                        numbers = True
                        break
            if numbers:
                break
        else:
            if not numbers:
                pytest.fail("Переменная 'numbers' не найдена")


class TestChapter07ex04:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_4_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Список после замены: [12, 0, 5, 0, 8, 0]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"



class TestChapter07ex05:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_5_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "0, 2, 4, 6, 8\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


    def test_solution_numbers_variable(self):
        # Проверка наличия переменной numbers и правильности значений
        with open("course/chapter_07/solutions/solution_5.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            numbers = False
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "numbers":
                        assert isinstance(node.value, ast.List), "numbers должно быть списком"
                        values = [elt.n for elt in node.value.elts]
                        assert values == [4, 7, 2, 9, 8, 5, 6, 3, 0, 1], "Неверные значения в numbers"
                        numbers = True
                        break
            if numbers:
                break
        else:
            if not numbers:
                pytest.fail("Переменная 'numbers' не найдена")

class TestChapter07ex06:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_6_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "50\n40\n30\n20\n10\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
            
    def test_solution_numbers_variable(self):
        # Проверка наличия переменной numbers и правильности значений
        with open("course/chapter_07/solutions/solution_6.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            numbers = False
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "numbers":
                        assert isinstance(node.value, ast.List), "numbers должно быть списком"
                        values = [elt.n for elt in node.value.elts]
                        assert values == [10, 20, 30, 40, 50], "Неверные значения в numbers"
                        numbers = True
                        break
            if numbers:
                break
        else:
            if not numbers:
                pytest.fail("Переменная 'numbers' не найдена")


class TestChapter07ex07:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_7_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Среднее арифметическое: 22.5\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


    def test_solution_numbers_variable(self):
        # Проверка наличия переменной numbers и правильности значений
        with open("course/chapter_07/solutions/solution_7.py", "r") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            numbers = False
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "numbers":
                        assert isinstance(node.value, ast.List), "numbers должно быть списком"
                        values = [elt.n for elt in node.value.elts]
                        assert values == [5, 10, 15, 20, 25, 30, 35, 40], "Неверные значения в numbers"
                        numbers = True
                        break
            if numbers:
                break
        else:
            if not numbers:
                pytest.fail("Переменная 'numbers' не найдена")
                
class TestChapter07ex08:
    @pytest.mark.solution_runner(("Иван\nАнна\nСергей\n\nМарина\nКирилл\n\nСергей\n"), 0.1)
    def test_solution_8_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "['Иван', 'Анна', 'Марина', 'Кирилл']\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Петр\nЕлена\n\nДмитрий\n\nЕлена\n"), 0.1)
    def test_solution_8_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "['Петр', 'Дмитрий']\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Максим\nОльга\n\nАлексей\nИрина\n\nОльга\n"), 0.1)
    def test_solution_8_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "['Максим', 'Алексей', 'Ирина']\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter07ex09:
    @pytest.mark.solution_runner(("3\n5\n4\n2\n1\n\n"), 0.1)
    def test_solution_9_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Минимальная оценка: 1\nМаксимальная оценка: 5\nОтсортированные оценки: [1, 2, 3, 4, 5]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("10\n8\n6\n4\n2\n\n"), 0.1)
    def test_solution_9_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Минимальная оценка: 2\nМаксимальная оценка: 10\nОтсортированные оценки: [2, 4, 6, 8, 10]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("7\n9\n1\n3\n5\n\n"), 0.1)
    def test_solution_9_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Минимальная оценка: 1\nМаксимальная оценка: 9\nОтсортированные оценки: [1, 3, 5, 7, 9]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter07ex10:
    @pytest.mark.solution_runner(("Кукла\nМяч\nПазлы\n\nЛошадка\nРобот\n\nМяч\nВертолет\n"), 0.1)
    def test_solution_10_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "такой игрушки нет\n['Кукла', 'Пазлы', 'Лошадка', 'Робот']\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Конструктор\nМашина\nПазлы\n\nСамолет\nЛего\n\nМашина\nПазлы\n"), 0.1)
    def test_solution_10_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "['Конструктор', 'Самолет', 'Лего']\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Мяч\nКукла\n\nКубик\nТанк\n\nМяч\nКукла\n"), 0.1)
    def test_solution_10_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "['Кубик', 'Танк']\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter07ex11:
    @pytest.mark.solution_runner(("Спальник\nФонарь\nТопор\n\n"), 0.1)
    def test_solution_11_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Вы не взяли палатку!\n3\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Палатка\nСпальник\nФонарь\n\n"), 0.1)
    def test_solution_11_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "3\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Рюкзак\nКотелок\nТопор\nФонарик\n\n"), 0.1)
    def test_solution_11_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Вы не взяли палатку!\n4\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter07ex12:
    @pytest.mark.solution_runner(("10 20 30 40 50 60 70\n3"), 0.1)
    def test_solution_12_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[10, 20, 30]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("5 15 25 35 45\n2"), 0.1)
    def test_solution_12_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[5, 15]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("1 2 3 4 5 6 7 8 9\n4"), 0.1)
    def test_solution_12_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[1, 2, 3, 4]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter07ex13:
    @pytest.mark.solution_runner(("5 10 15 20 25 30\n2"), 0.1)
    def test_solution_13_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "55\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("3 6 9 12 15 18\n3"), 0.1)
    def test_solution_13_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "45\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("100 200 300 400 500 600\n1"), 0.1)
    def test_solution_13_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "600\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter07ex14:
    @pytest.mark.solution_runner(("1 2 3 4 5 6 7 8\n"), 0.1)
    def test_solution_14_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[1, 3, 5, 7]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("10 20 30 40 50\n"), 0.1)
    def test_solution_14_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[10, 30, 50]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("5 10 15 20 25 30\n"), 0.1)
    def test_solution_14_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[5, 15, 25]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter07ex15:
    @pytest.mark.solution_runner(("9 8 7 6 5\n"), 0.1)
    def test_solution_15_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[5, 6, 7, 8, 9]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("3 2 1 0\n"), 0.1)
    def test_solution_15_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[0, 1, 2, 3]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("1 2 3 4 5\n"), 0.1)
    def test_solution_15_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[5, 4, 3, 2, 1]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter07ex16:
    @pytest.mark.solution_runner(("100 200 300 400 500 600 700\n2"), 0.1)
    def test_solution_16_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Максимум: 500\nМинимум: 300\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("10 20 30 40 50\n1"), 0.1)
    def test_solution_16_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Максимум: 40\nМинимум: 20\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("5 10 15 20 25 30 35 40\n3"), 0.1)
    def test_solution_16_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Максимум: 25\nМинимум: 20\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter07ex17:
    @pytest.mark.solution_runner(("3 2 1 0 5 10 11 12 6 8 7 9\n3"), 0.1)
    def test_solution_17_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[0, 3, 8, 11]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("5 10 15 20 25 30\n2"), 0.1)
    def test_solution_17_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[5, 15, 25]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("9 8 7 6 5 4 3 2 1\n4"), 0.1)
    def test_solution_17_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[1, 5, 9]\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
