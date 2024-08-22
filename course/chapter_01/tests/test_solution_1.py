import pytest

def test_import_module():
    try:
        import course.chapter_01.solutions.solution_1 as solution_1
    except ImportError:
        pytest.fail("Failed to import 'solution_1.py'")

def test_import_module():
    try:
        from course.chapter_01.solutions.solution_1 import age, is_student, name
    except ImportError:
        pytest.fail("variables age, is_student, name are not exist")
    assert isinstance(age, int), "Variable age has not integer type"
    assert isinstance(is_student, bool), "Variable is_student has not bool type"
    assert isinstance(name, str), "Variable name has not string type"
