import pdfrw
import file_types as ft

def append(new_path, *file_paths):
	'''
	Merges an arbitrary number of files together.
	Writes the result to disk and returns a PdfFile object.
	'''
	new_pdf = pdfrw.PdfWriter()
	for file in file_paths:
		reader = pdfrw.PdfReader(file)
		for page in reader.pages:
			new_pdf.addpage(page)
	new_pdf.write(new_path)
	return ft.PdfFile(new_path)

def split(original_file, page_nums, *new_paths):
	'''Splits file at each page in page_nums to create new files, returns list of pdf objects'''
	
	og_file = pdfrw.PdfReader(original_file)
	writers = [pdfrw.PdfWriter()]
	# search through the original file and generate the appropriate
	# PdfWriter objects
	for i in range(len(og_file.pages)):
		if i in page_nums:
			writers.append(pdfrw.PdfWriter())
		writers[-1].addpage(og_file.pages[i])
	objs = []
	# Write pdfs to disk and make pdf objects
	for writer, path in zip(writers, new_paths):
		writer.write(path)
		try:
			objs.append(ft.PdfFile(path))
		except:
			print("{} was written to disk, but failed to convert to pdf object!".format(path))
	return objs
