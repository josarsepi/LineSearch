import logging
import datetime
logfile = 'log.findinline.log'
logging.basicConfig(filename=logfile,level=logging.INFO)

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
		
################################
# Initialize Logging
################################

		logging.info(str(self.ts()) + 'Starting up.')
		
#################################
# Build Regular Expressions
#################################

		logging.debug(str(self.ts()) + 'Trying to build regex.')
		
		comreg = '|'.join(self.findlist)
		self.comreg = r'.*(' + str(comreg) + ')'
		self.regex = re.compile(str(self.comreg))
		print("Searching for: " + str(self.regex.pattern))
		
		logging.info(str(self.ts()) + "Searching for: " + str(self.regex.pattern))
		logging.debug(str(self.ts()) + 'Finished building regex.')
		
##################################
# Execute Main Program
##################################
	
	def makenew(self):
		
		import os
		import io
		from io import FileIO, BufferedWriter
		
		logging.debug(str(self.ts()) + 'Trying makenew.')
		
		try:
			with BufferedWriter(FileIO(self.output,'wb'),buffer_size=4096000) as self.outf:
				logging.debug(str(self.ts()) + 'Trying searchfiles.')
				self.searchfiles(self.filelist,self.findlist)
				logging.debug(str(self.ts()) + 'Finished searchfiles.')
			self.outf.close

			print("Total Lines: " + str(self.totline))
			print("Total time: " + str(self.tottime))
			
			logging.info(str(self.ts()) + "Total Lines: " + str(self.totline))
			logging.info(str(self.ts()) + "Total time: " + str(self.tottime))
			
		except:
			logging.error(str(self.ts()) + 'Something went terribly wrong.', exc_info=True)

#################################
# Seperate each file from the list and send file to finder.
#################################

	def searchfiles(self,filelst,findlst):
		import os
		
		for each in filelst:
			logging.debug(str(self.ts()) + 'Trying finder against' + str(each))
			self.finder(each,self.findlist)
			logging.debug(str(self.ts()) + 'Finished finder gainst' + str(each))
			
		logging.debug(str(self.ts()) + 'Finished searchfiles')
			
#################################
# Search for each regular expression.
#################################
		
	@managed
	def finder(self, file2read,findlist):
		import os
		import io
		from io import FileIO, BufferedReader, BufferedWriter
		import re
		
		print("Adding matches from " + str(file2read) + " to output: " + str(self.output))
		logging.info(str(self.ts()) + "Adding matches from " + str(file2read) + " to output: " + str(self.output))
		
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
		print("Done adding matches to file " + str(self.output))
		logging.info(str(self.ts()) + "Done adding matches to file " + str(self.output))		
		
		print("Total Lines in " + str(file2read) + " : " + str(rowcount))
		print("Total Matches in " + str(file2read) + " : " + str(matchcount))
		
		logging.info(str(self.ts()) + "Total Lines in " + str(file2read) + " : " + str(rowcount))
		logging.info(str(self.ts()) + "Total Matches in " + str(file2read) + " : " + str(matchcount))

#################################
# Timestamp Creator
#################################
	def ts(self):
		time = str('__' + str(datetime.datetime.today()) + '__')
		return time