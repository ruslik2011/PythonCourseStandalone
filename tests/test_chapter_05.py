import pytest


class TestChapter05ex01:
    @pytest.mark.solution_runner("5", 0.1)
    def test_solution_1_output_5(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "1\t2\t3\t4\t5\t\n"
            "2\t4\t6\t8\t10\t\n"
            "3\t6\t9\t12\t15\t\n"
            "4\t8\t12\t16\t20\t\n"
            "5\t10\t15\t20\t25\t\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("3", 0.1)
    def test_solution_1_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "1\t2\t3\t\n"
            "2\t4\t6\t\n"
            "3\t6\t9\t\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("9", 0.1)
    def test_solution_1_output_9(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "1\t2\t3\t4\t5\t6\t7\t8\t9\t\n"
            "2\t4\t6\t8\t10\t12\t14\t16\t18\t\n"
            "3\t6\t9\t12\t15\t18\t21\t24\t27\t\n"
            "4\t8\t12\t16\t20\t24\t28\t32\t36\t\n"
            "5\t10\t15\t20\t25\t30\t35\t40\t45\t\n"
            "6\t12\t18\t24\t30\t36\t42\t48\t54\t\n"
            "7\t14\t21\t28\t35\t42\t49\t56\t63\t\n"
            "8\t16\t24\t32\t40\t48\t56\t64\t72\t\n"
            "9\t18\t27\t36\t45\t54\t63\t72\t81\t\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter05ex02:
    @pytest.mark.solution_runner("Программирование - это весело!", 0.1)
    def test_solution_2_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = 'Вот что сказал пользователь: "Программирование - это весело!"\n'
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Я люблю Python", 0.1)
    def test_solution_2_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = 'Вот что сказал пользователь: "Я люблю Python"\n'
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Всем привет!", 0.1)
    def test_solution_2_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = 'Вот что сказал пользователь: "Всем привет!"\n'
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter05ex03:
    @pytest.mark.solution_runner("-", 0.1)
    def test_solution_3_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "яблоко-банан-вишня\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(":", 0.1)
    def test_solution_3_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "яблоко:банан:вишня\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("/", 0.1)
    def test_solution_3_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "яблоко/банан/вишня\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter05ex04:
    @pytest.mark.solution_runner("%", 0.1)
    def test_solution_4_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Первая строка%Вторая строка%Третья строка\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("-", 0.1)
    def test_solution_4_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Первая строка-Вторая строка-Третья строка\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("/", 0.1)
    def test_solution_4_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Первая строка/Вторая строка/Третья строка\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter05ex05:
    @pytest.mark.solution_runner("10", 0.1)
    def test_solution_5_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("5", 0.1)
    def test_solution_5_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "1, 2, 3, 4, 5\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("3", 0.1)
    def test_solution_5_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "1, 2, 3\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter05ex06:
    @pytest.mark.solution_runner("5", 0.1)
    def test_solution_6_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "!_!!_!!!_!!!!_!!!!!\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("3", 0.1)
    def test_solution_6_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "!_!!_!!!\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("7", 0.1)
    def test_solution_6_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "!_!!_!!!_!!!!_!!!!!_!!!!!!_!!!!!!!\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter05ex07:
    @pytest.mark.solution_runner(("Алексей", "25"), 0.1)
    def test_solution_7_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Привет, Алексей! Тебе 25 лет.\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Ольга", "18"), 0.1)
    def test_solution_7_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Привет, Ольга! Тебе 18 лет.\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Иван", "30"), 0.1)
    def test_solution_7_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Привет, Иван! Тебе 30 лет.\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter05ex08:
    @pytest.mark.solution_runner(("8", "3"), 0.1)
    def test_solution_8_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "8.0 + 3.0 = 11.00\n"
            "8.0 - 3.0 = 5.00\n"
            "8.0 * 3.0 = 24.00\n"
            "8.0 / 3.0 = 2.67\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("10", "4"), 0.1)
    def test_solution_8_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "10.0 + 4.0 = 14.00\n"
            "10.0 - 4.0 = 6.00\n"
            "10.0 * 4.0 = 40.00\n"
            "10.0 / 4.0 = 2.50\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("15", "5"), 0.1)
    def test_solution_8_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "15.0 + 5.0 = 20.00\n"
            "15.0 - 5.0 = 10.00\n"
            "15.0 * 5.0 = 75.00\n"
            "15.0 / 5.0 = 3.00\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter05ex09:
    @pytest.mark.solution_runner(("100", "73.25"), 0.1)
    def test_solution_9_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "100 долларов = 7325.00 рублей\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("50", "65.00"), 0.1)
    def test_solution_9_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "50 долларов = 3250.00 рублей\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("200", "80.50"), 0.1)
    def test_solution_9_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "200 долларов = 16100.00 рублей\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter05ex10:
    @pytest.mark.solution_runner(("Ольга", "5", "4", "5"), 0.1)
    def test_solution_10_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Средняя оценка студента Ольга: 4.7\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Иван", "3", "4", "5"), 0.1)
    def test_solution_10_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Средняя оценка студента Иван: 4.0\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("Анна", "2", "3", "4"), 0.1)
    def test_solution_10_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Средняя оценка студента Анна: 3.0\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
