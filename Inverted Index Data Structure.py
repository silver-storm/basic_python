class Inverted_Index():
	def __init__(self):
		self.storage = {}

	def __str__(self):
		for key in self.storage.keys():
			print(f"{key} : {self.storage[key]}")
		return '\a'

	def add_files(self,filenames=[]):
		if type(filenames) is not list:
			try:
				filenames = list(files)
			except Exception:
				raise TypeError(f"Input must be an iterable, not {type(filenames)}")

		for filename in filenames:
			if type(filename) is not str:
				raise TypeError("Filenames should be given as a string")

		for file in filenames:
			with open(file,'r+') as f:
				word_ct = 0
				for line in f.readlines():
					line = line.strip().rstrip('\n').split(sep=' ')
					for word in line:
						if word not in self.storage.keys():
							self.storage[word] = []
							self.storage[word].append((word_ct,file))
						else:
							self.storage[word].append((word_ct,file))
						word_ct += 1

		self.word_count = len(self.storage)
		print(f"Added {self.word_count} words to storage!\n")
		return self

	def close_index(self):	
		del self.storage

if __name__ == '__main__':
	filenames = ['./file1.txt','./file2.txt']	
	Index_obj = Inverted_Index().add_files(filenames)
	print(Index_obj)