import pytest
import ast
from ast import Assign


class TestChapter03ex01:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_1_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "".join([str(i) + "\n" for i in range(1, 11)])
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex02:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_2_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "".join([str(i) + "\n" for i in range(2, 21, 2)])
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex03:
    @pytest.mark.solution_runner("", 0.1)
    def test_solution_3_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "".join([str(i) + "\n" for i in range(10, 0, -1)]) + "Время вышло!\n"
        )
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex04:
    @pytest.mark.solution_runner("4", 0.1)
    def test_solution_4_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = "".join(
            ["4 x " + str(i) + " = " + str(4 * i) + "\n" for i in range(1, 11)]
        )
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex05:
    def get_password():
        try:
            file = open("course/chapter_03/solutions/solution_5.py", "r")
            tree = ast.parse(file.read())
        except FileExistsError:
            pytest.fail("Failed to import 'solution_5.py'")

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "password":
                        if isinstance(node.value, ast.Constant) and isinstance(
                            node.value.value, str
                        ):
                            return node.value.value
        pytest.fail(
            "Failed to find password variable\n" + "or password variable has wrong type"
        )
        return None

    @pytest.mark.solution_runner(
        ("4sgr____4234fasf", "34qfqw4fq4fq3hweq4_!4", get_password()), 0.1
    )
    def test_solution_5_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "Неверный пароль, попробуйте снова.\n"
            + "Неверный пароль, попробуйте снова.\n"
            + "Доступ разрешён.\n"
        )
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex06:
    @pytest.mark.solution_runner(["4", "10", "100", "20"], 0.1)
    def test_solution_6_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = ["10\n", "55\n", "5050\n", "210\n"]
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex07:
    @pytest.mark.solution_runner(["1", "3", "5", "10"], 0.1)
    def test_solution_7_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = ["1\n", "6\n", "120\n", "3628800\n"]
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex08:
    @pytest.mark.solution_runner(["1", "3", "101", "65"], 0.1)
    def test_solution_8_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = ["1\n", "4\n", "2601\n", "1089\n"]
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex09:
    @pytest.mark.solution_runner(["1", "3", "101", "6235"], 0.1)
    def test_solution_9_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = ["1\n", "3\n", "2\n", "16\n"]
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex10:
    @pytest.mark.solution_runner(["35", "221", "121", "64"], 0.1)
    def test_solution_10_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = ["5\n", "13\n", "11\n", "2\n"]
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex11:
    @pytest.mark.solution_runner(
        [
            ("1", "2", "3", "4", "5"),
            ("1", "-12", "2", "3", "-44", "4", "5"),
            ("-41", "5", "-12", "5", "5", "-44", "4", "5"),
        ],
        0.1,
    )
    def test_solution_11_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = ["15\n", "15\n", "24\n"]
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex12:
    def get_value():
        try:
            file = open("course/chapter_03/solutions/solution_12.py", "r")
            tree = ast.parse(file.read())
        except FileExistsError:
            pytest.fail("Failed to import 'solution_12.py'")

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "num":
                        if isinstance(node.value, ast.Constant) and isinstance(
                            node.value.value, int
                        ):
                            return str(node.value.value)
        pytest.fail("Failed to find num variable\n" + "or num variable has wrong value")
        return None

    @pytest.mark.solution_runner(
        [
            ("0", "0", get_value()),
            ("100", get_value()),
            ("0", "0", "0", "0", "0", "0"),
        ],
        0.1,
    )
    def test_solution_12_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = [
            "Загаданное число больше.\n"
            + "Загаданное число больше.\n"
            + "Поздравляем! Вы угадали число.\n",
            "Загаданное число меньше.\n" + "Поздравляем! Вы угадали число.\n",
            "Загаданное число больше.\n" * 5 + "Попытки закончились\n",
        ]
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex13:
    def get_password():
        try:
            file = open("course/chapter_03/solutions/solution_13.py", "r")
            tree = ast.parse(file.read())
        except FileExistsError:
            pytest.fail("Failed to import 'solution_13.py'")

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "password":
                        if isinstance(node.value, ast.Constant) and isinstance(
                            node.value.value, str
                        ):
                            return node.value.value
        pytest.fail(
            "Failed to find password variable\n" + "or password variable has wrong type"
        )
        return None

    @pytest.mark.solution_runner(
        [
            (
                "4sgr____4233g3hwh44w4fasf",
                "34qfqw4fq4fq3h2362346weq4_!4",
                get_password(),
            ),
            (
                "4sgr____4234fasadfw3gf",
                "34qfqw4fq4fq3hw23geq4_!4",
                "34f3434gaegaeg236236ae;h4g",
            ),
            (get_password(),),
        ],
        0.1,
    )
    def test_solution_13_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = [
            "Неверный пароль, попробуйте снова.\n"
            + "Неверный пароль, попробуйте снова.\n"
            + "Доступ разрешён.\n",
            "Неверный пароль, попробуйте снова.\n" * 2 + "Доступ запрещен\n",
            "Доступ разрешён.\n",
        ]
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex14:
    @pytest.mark.solution_runner(
        [("-3", "1"), ("3",), ("-100", "101"), ("-1", "-2", "6235")], 0.1
    )
    def test_solution_14_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = ["1\n", "3\n", "2\n", "16\n"]
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter03ex15:
    @pytest.mark.solution_runner(
        [("-3", "1"), ("3",), ("-100", "101"), ("-1", "-2", "6235")], 0.1
    )
    def test_solution_14_output(self, solution_runner):
        solution_out = solution_runner
        expected_output = [
            "1\n",
            "1\n3\n",
            "1\n101\n",
            "1\n5\n29\n43\n145\n215\n1247\n6235\n",
        ]
        assert (
            expected_output == solution_out
        ), f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
