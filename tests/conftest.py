# conftest.py
import pytest
import subprocess

@pytest.fixture()
def solution_runner(request):
    chapter = request.param[0]
    solution = request.param[1]
    inputed_values = request.param[2]
    print(chapter, solution)
    import os
    chapter = "chapter_0" + str(chapter) if chapter < 10 else "chapter_" + str(chapter)
    solution = "solution_" + str(solution) + ".py"
    file_path = os.path.join("course", chapter, "solutions", solution)
    result = subprocess.run(['python3', file_path], input=inputed_values, capture_output=True, text=True)
    return result.stdout



