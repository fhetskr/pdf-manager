#!/bin/sh
# Convert files and see if we write them.
# This script does NOT test the contents!
# This script will clean up after itself - if you want to preserve results,
# comment out the rm ... lines.
python3 ../cli.py --convert ../test-files/test-one.txt pdf ../test-files/result-one.pdf
if [ -f ../test-files/result-one.pdf ]
then
	echo "Test one passed."
	rm ../test-files/result-one.pdf
else
	"Test one failed."
fi

python3 ../cli.py --convert ../test-files/test-one.txt xlsx ../test-files/result-one.xlsx
if [ -f ../test-files/result-one.xlsx ]
then
	echo "Test two passed."
	rm ../test-files/result-one.xlsx
else
	echo "Test two failed."
fi

python3 ../cli.py --convert ../test-files/test-one.txt json ../test-files/result-one.json
if [ -f ../test-files/result-one.json ]
then
	echo "Test three passed."
	rm ../test-files/result-one.json
else
	echo "Test three failed."
fi

python3 ../cli.py --convert ../test-files/test-one.txt txt ../test-files/result-one.txt
if [ -f ../test-files/result-one.txt ]
then
	echo "Test four passed."
	rm ../test-files/result-one.txt
else
	echo "Test four failed."
fi

python3 ../cli.py --convert ../test-files/test-one.txt csv ../test-files/result-one.csv
if [ -f ../test-files/result-one.csv ]
then
	rm ../test-files/result-one.csv
	echo "Test five passed."
else
	echo "Test five ailed."
fi

