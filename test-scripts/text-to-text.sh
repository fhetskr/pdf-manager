#/bin/bash

# Paths to test files, where results should go, and where the expected results are.
BASE_TEST_PATH="../test-files/tests/txt"
BASE_RESULT_PATH="../test-files/results/txt"
BASE_EXPECTED_PATH="../test-files/expected/txt"

# Generate all resultant text files from text to text conversion.
python3 ../cli.py -c $BASE_TEST_PATH/test-one.txt txt $BASE_RESULT_PATH/result-one.txt
python3 ../cli.py -c $BASE_TEST_PATH/test-two.txt txt $BASE_RESULT_PATH/result-two.txt
python3 ../cli.py -c $BASE_TEST_PATH/test-three.txt txt $BASE_RESULT_PATH/result-three.txt

if cmp $BASE_RESULT_PATH/result-one.txt $BASE_EXPECTED_PATH/expected-one.txt 
then
	echo Test one passed.
else
	echo Test one failed.
fi

if cmp $BASE_RESULT_PATH/result-two.txt $BASE_EXPECTED_PATH/expected-two.txt
then
	echo Test two passed.
else
	echo Test two failed.
fi

if cmp $BASE_RESULT_PATH/result-three.txt $BASE_EXPECTED_PATH/expected-three.txt
then
	echo Test three passed.
else
	echo Test three failed.
fi
