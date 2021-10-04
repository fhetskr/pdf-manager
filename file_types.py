# TODO:
# just about everything


### Internal data types

class OrderedDictionary():
	# NB: I'm not sure we actually need to implement this -Peter
	pass

# A placeholder file type
class GenericFile():

	# The generic file type's methods should all be overwritten by its children
		
	def __init__(self, path):
		'''TODO: implement generic data storage format'''
		self.path = path
		self.contents = ''
	
	def read(self):
		'''Updates self.contents with the actual data from the file at self.path'''
		pass
		
	def write(self):
		'''Writes contents to the file at self.path'''
		pass
	
	def convert(self, target_type):
		'''Return a file object of target_type with this file's contents'''
		pass
		
	def verify(self):
		'''Verify that self.path points to a file of the appropriate format'''
		pass
				
### Actual file types
# TODO: implement these

class ExcelFile(GenericFile):
	pass

class TxtFile(GenericFile):
	pass

class PDFFIle(GenericFile):
	pass