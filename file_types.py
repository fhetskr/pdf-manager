import os
import pdfrw


### Internal data types

class OrderedDictionary():
	# NB: I'm not sure we actually need to implement this -Peter
	# Edit: nvm I think we probably will have to
	pass

class FileError(Exception):
	'''Exception for invalid files'''
	pass

# A placeholder file type
class GenericFile():
	
	def __init__(self, path):
		'''Generic constructor for file types'''
		# save path to self.path
		self.path = path
		
		# get file extension
		if len(path.split('.')) > 1:
			self.extension = path.split('.')[-1]
		
		if os.path.isfile(path):
			self.verify()
			self.read()
		else:
			# create an empty file if none exists.
			with open(path, 'w') as f:
				pass
	
	def read(self):
		'''Updates self.contents with the actual data from the file at self.path'''
		pass
		
	def write(self):
		'''Writes contents to the file at self.path'''
		pass
	
	def convert(self, target_type, target_path):
		'''Return a file object of target_type with this file's contents'''
		if target_path:
			path = target_path
		else:
			# strip old extension if necessary
			if self.extension:
				path = '.'.join(self.path.split('.')[:-1])
			else:
				path = self.path
			# add new extension
			path = '.'.join((path,target_type))
		# create new file object and return it
		new_file = fileTypes[target_type](path)
		new_file.contents = self.contents
		return new_file
		
	def verify(self):
		'''Verify that self.path points to a file of the appropriate format'''
		pass
		
	def delete(self):
		'''Deletes the file at self.path from the filesystem, but retains contents'''
		os.remove(self.path)
				
### Actual file types
# TODO: implement these

class ExcelFile(GenericFile):
	pass

class TxtFile(GenericFile):
	pass

class CsvFile(GenericFile):
	def write(self):
		f = open(self.path, 'w')
		ret = ''
		for key, value in self.contents.items():
			ret += '"%s","%s"\n' % (key, value)
		f.write(ret)
		f.close()

class PdfFile(GenericFile):
	def read(self):
		# flow for reading pdfs from https://akdux.com/python/2020/10/31/python-fill-pdf-files.html
		# store the entire pdf in base_data
		self.data = pdfrw.PdfReader(self.path)
		self.contents = {}
		# iterate over pages
		for page in self.data.pages:
			annots = page['/Annots']
			# then over annotations on that page
			for annot in annots:
				# check that we're in a widget with a field key
				if annot['/Subtype'] == '/Widget':
					if annot['/T']:
						print(annot)
						key = annot['/T'][1:-1]
						val = ''
						# read the field value, if any
						if annot['/AS']:
							if annot['/AS'] == '/Yes':
								val = True
							if annot['/AS'] == '/Off':
								val = False
						elif annot['/V']:
							val = annot['/V'][1:-1]
						self.contents[key] = val
						print('%s,%s' % (key, val))
				# ugly handling of edge cases in case a field is embedded entirely within the parent value
				if annot['/Parent']:
					print(annot['/Parent'])
					if annot['/Parent']['/T']:
						key = annot['/Parent']['/T'][1:-1]
						val = ''
						# read the field value, if any
						if annot['/AS']:
							if annot['/AS'] == '/Yes':
								val = True
							if annot['/AS'] == '/Off':
								val = False
						elif annot['/V']:
							val = annot['/V'][1:-1]
						self.contents[key] = val
						print('%s,%s' % (key, val))

class JsonFile(GenericFile):
	pass

# Dictionary for file types
fileTypes = {
	"txt": TxtFile,
	"csv": CsvFile,
	"xlsx": ExcelFile,
	"pdf": PdfFile,
	"json": JsonFile
}