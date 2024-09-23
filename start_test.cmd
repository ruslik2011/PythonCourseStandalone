@echo off
REM Check if at least one argument is provided
if "%~1"=="" (
    echo Usage: %0 ^<chapter_number^> [exercise_number]
    exit /b 1
)


set /A CHAPTER_NUM=%1
set /A TEN=10
REM Construct the test file name based on the chapter number

if %CHAPTER_NUM% LSS %TEN% (set TEST_FILE=tests\test_chapter_0%CHAPTER_NUM%) ELSE (set TEST_FILE=tests\test_chapter_%CHAPTER_NUM%)

REM Check if the test file exists
if not exist "%TEST_FILE%.py" (
    echo Test file %TEST_FILE%.py does not exist.
    exit /b 1
)

if "%~2"==""  (
    python -m pytest -v "%TEST_FILE%.py"
	exit /b 0
) 
set/A EXERCISE_NUM=%2
if %EXERCISE_NUM% LSS %TEN% (set "EXERCISE=0%EXERCISE_NUM%") 
if %CHAPTER_NUM% LSS %TEN% (set "CHAPTER=0%CHAPTER_NUM%") 
set "TEST_CLASS=TestChapter%CHAPTER%ex%EXERCISE%"
python -m pytest -v "%TEST_FILE%.py::%TEST_CLASS%"