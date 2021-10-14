import os

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
	
	def convert(self, target_type):
		'''Return a file object of target_type with this file's contents'''
		# strip old extension if necessary
		if self.extension:
			path = self.path.split('.')[:-1]
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
	pass

class PdfFile(GenericFile):
	pass

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