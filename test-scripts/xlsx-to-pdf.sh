#/bin/bash

BASE_TEST_PATH=../test-files/tests/xlsx
BASE_RESULT_PATH=../test-files/results/pdf
BASE_EXPECTED_PATH=../test-files/expected/pdf

python3 ../cli.py -c $BASE_TEST_PATH/expected-four-fill.xlsx pdf $BASE_RESULT_PATH/pdf-four-xlsx-fill.pdf
