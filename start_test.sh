#!/bin/bash

# Check if at least one argument is provided
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <chapter_number> [exercise_number]"
    exit 1
fi

CHAPTER_NUM=$1

# Construct the test file name based on the chapter number
TEST_FILE="./tests/test_chapter_$(printf "%02d" $CHAPTER_NUM).py"

# Check if the test file exists
if [ ! -f "$TEST_FILE" ]; then
    echo "Test file $TEST_FILE does not exist."
    exit 1
fi

# If the second argument (exercise number) is provided
if [ "$#" -eq 2 ]; then
    EXERCISE_NUM=$2
    # Construct the test class name based on the exercise number
    TEST_CLASS="TestChatper$(printf "%02d" $CHAPTER_NUM)ex$(printf "%02d" $EXERCISE_NUM)"
    # Run only the specified test class in verbose mode
    python3 -m pytest -v "$TEST_FILE"::"$TEST_CLASS"
else
    # If no exercise number is provided, run all tests in the chapter
    python3 -m pytest -v "$TEST_FILE"
fi
