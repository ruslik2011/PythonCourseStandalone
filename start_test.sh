#!/bin/bash

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <chapter_number> [exercise_number]"
    exit 1
fi

CHAPTER_NUM=$1

TEST_FILE="./tests/test_chapter_$(printf "%02d" $CHAPTER_NUM).py"

if [ ! -f "$TEST_FILE" ]; then
    echo "Test file $TEST_FILE does not exist."
    exit 1
fi

if [ "$#" -eq 2 ]; then
    EXERCISE_NUM=$2

    TEST_CLASS="TestChapter$(printf "%02d" $CHAPTER_NUM)ex$(printf "%02d" $EXERCISE_NUM)"

    python3 -m pytest -vv "$TEST_FILE"::"$TEST_CLASS"
else

    python3 -m pytest -vv "$TEST_FILE"
fi
