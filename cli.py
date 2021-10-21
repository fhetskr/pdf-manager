import argparse
import sys
from file_types import *

def main():
	'''Entry point to the program'''
	'''By Matthew'''
	parser = argparse.ArgumentParser(description='Handle data in fillable PDFs.')
	args = sys.argv[1:]
	cmd = args[0]
	if cmd == 'extract':
		pdf = PdfFile(args[1])
		if len(args) > 3:
			dest = pdf.convert_redirect(args[2].split('.')[-1], args[2], TxtFile(args[3]))
		else:
			dest = pdf.convert(args[2].split('.')[-1], args[2])
		dest.write()
	if cmd == 'fill':
		src = file_dict[args[2].split('.')[-1]](args[2])
		src.read()
		dest = src.convert('pdf', args[1])
		if '--ordered' in args or '-o' in args:
			dest.write_ordered()
		else:
			dest.write()
	if cmd == 'examine':
		pdf = PdfFile(args[1])
		dest = pdf.convert('txt', None)
		dest.write_keys()

if __name__ == '__main__':
	main()