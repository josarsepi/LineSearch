def managed(func):
	
	import timeit
	
	def wrappedfunc(self, *args, **kwargs):
		start = timeit.default_timer()
		retval = func(self, *args, **kwargs)
		end = timeit.default_timer()
		tot = end - start
		print(func.__name__ + " total time: " + str(tot))
		self.tottime = self.tottime + tot
		return retval
	return wrappedfunc

class findinline:
	
	def __init__(self):
		
		import re
		
		from finderconf import filelist
		from finderconf import findlist
		from finderconf import output
		
		self.filelist = filelist
		self.findlist = findlist
		self.output = output
		self.totline = 0
		self.tottime = 0
		self.comreg = None

#################################
#
#################################
			
		comreg = '|'.join(self.findlist)
		self.comreg = r'.*(' + str(comreg) + ')'
		self.regex = re.compile(str(self.comreg))
		print("Searching for: " + str(self.regex.pattern))
		
##################################
#
##################################
	
	def makenew(self):
		
		import os
		import io
		from io import FileIO, BufferedWriter
		
		with BufferedWriter(FileIO(self.output,'wb'),buffer_size=4096000) as self.outf:
			self.searchfiles(self.filelist,self.findlist)
		self.outf.close

		print("Total Lines: " + str(self.totline))
		print("Total time: " + str(self.tottime))

#################################
#
#################################

	def searchfiles(self,filelst,findlst):
		import os
		
		for each in filelst:
			self.finder(each,self.findlist)
			
#################################
#
#################################
		
	@managed
	def finder(self, file2read,findlist):
		import os
		import io
		from io import FileIO, BufferedReader, BufferedWriter
		import re
		
		print("Adding matches from " + str(file2read) + " to output: " + str(self.output))
		
		#with BufferedWriter(FileIO(self.output,'wb'),buffer_size=409600) as outf:

		with open(file2read, 'r', encoding='utf-8') as f:
			rowcount = 0
			matchcount = 0
				
			line = f.readline()
			while line != '':
				rowcount = rowcount + 1
				nugget = re.match(self.regex,str(line))
				if nugget != None:
					self.outf.write(str.encode(line))
					matchcount = matchcount + 1

				line = f.readline()

		self.totline = self.totline + rowcount
		print("Done adding objects to file " + str(self.output))
		
		print("Total Lines in " + str(file2read) + " : " + str(rowcount))
		print("Total Matches in " + str(file2read) + " : " + str(matchcount))
