# conftest.py
import os
import pytest
from subprocess import Popen, PIPE, STDOUT, TimeoutExpired


# def pytest_configure(config):
#     config.addinivalue_line(
#         "markers",
#         "solution_runner(arg1, arg2, arg3, arg4):\
#          custom marker for my fixture",
#     )


@pytest.fixture()
def solution_runner(request):
    marker = request.node.get_closest_marker("solution_runner")
    if marker is None:
        pytest.fail("The 'solution_runner' marker must be provided")
    chapter, solution, timeout, inputed_values = marker.args
    inputed_values = map(lambda x: x + "\n", inputed_values)
    chapter = "chapter_0" + str(chapter) if chapter < 10 else "chapter_" + str(chapter)
    solution = "solution_" + str(solution) + ".py"
    file_path = os.path.join("course", chapter, "solutions", solution)
    if not os.path.isfile(file_path):
        pytest.fail("Solution not exist")
    try:
        p = Popen(
            ["python3", file_path], stdout=PIPE, stdin=PIPE, stderr=PIPE, text=True
        )
        p.stdin.writelines(inputed_values)
        p.stdin.close()
        p.wait(timeout=timeout)
    except TimeoutExpired:
        pytest.fail("Programm not terminate in timeout")

    result = p.stdout.read()
    return result
