@echo off
REM Check if at least one argument is provided
if "%~1"=="" (
    echo Usage: %0 ^<chapter_number^> [exercise_number]
    exit /b 1
)

set CHAPTER_NUM=%1
REM Construct the test file name based on the chapter number
set TEST_FILE=tests\test_chapter_%CHAPTER_NUM%
if %CHAPTER_NUM% LSS 10 (
    set TEST_FILE=tests\test_chapter_0%CHAPTER_NUM%
)

REM Check if the test file exists
if not exist "%TEST_FILE%.py" (
    echo Test file %TEST_FILE%.py does not exist.
    exit /b 1
)

REM If the second argument (exercise number) is provided
if not "%~2"=="" (
    set EXERCISE_NUM=%2
    REM Construct the test class name based on the exercise number
    set TEST_CLASS=TestChatper%CHAPTER_NUM%ex%EXERCISE_NUM%
    if %CHAPTER_NUM% LSS 10 (
        set TEST_CLASS=TestChatper0%CHAPTER_NUM%ex%EXERCISE_NUM%
    )
    if %EXERCISE_NUM% LSS 10 (
        set TEST_CLASS=TestChatper%CHAPTER_NUM%ex0%EXERCISE_NUM%
    )
    REM Run only the specified test class in verbose mode
    python -m pytest -v "%TEST_FILE%.py"::"%TEST_CLASS%"
) else (
    REM If no exercise number is provided, run all tests in the chapter
    python -m pytest -v "%TEST_FILE%.py"::"%TEST_CLASS%"
)
