import argparse
import sys
from file_types import *

def main():
	parser = argparse.ArgumentParser(description='Handle data in fillable PDFs.')
	args = sys.argv[1:]
	cmd = args[0]
	if cmd == 'extract':
		pdf = PdfFile(args[1])
		dest = pdf.convert(args[2].split('.')[-1], args[2])
		dest.write()
	if cmd == 'fill':
		src = fileTypes[args[2].split('.')[-1]](args[2])
		src.read()
		dest = src.convert(PdfFile, args[1])
		dest.write()

if __name__ == '__main__':
	main()