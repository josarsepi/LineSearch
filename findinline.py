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
	
	# from findinline import findinline
	# finder = findinline()
	# finder.makenew()
	
	def __init__(self):
		
		import re
		
		from finderconf import filelist
		from finderconf import findlist
		from finderconf import isother
		from finderconf import output
		from finderconf import newline
		
		self.filelist = filelist
		self.findlist = findlist
		self.output = output
		self.isother = isother
		self.newline = newline
		self.totline = 0
		self.tottime = 0
		self.littelist = None
		self.biglist = None
		self.newline = None
		self.comreg = None

		for each in self.findlist:
			place = self.findlist.index(each)
			neweach = '.*(' + str(each) + ')'
			del self.findlist[place]
			self.findlist.insert(place,neweach)
			
		comreg = '|'.join(self.findlist)
		self.comreg = 'r' + "'" + str(comreg) + "'"
		self.regex = re.compile(str(self.comreg))
	
	def makenew(self):
		
		import os
		import io
		
		print("What I think the regex is:\n" + str(self.comreg))
		print("What the regex actually is:\n" + str(self.regex.pattern))
		
		#print("Searching these files: " + str(self.filelist) + "\n For these things: " + str(self.findlist))
		
		self.searchfiles(self.filelist,self.findlist)

		print("Total Lines: " + str(self.totline))
		print("Total time: " + str(self.tottime))
		
	def searchfiles(self,filelst,findlst):
		import os
		
		print("Here's your isother statement: " + str(self.isother))
		
		if self.isother == None:
			for each in filelst:
				self.finder(each,self.findlist)

		elif str(self.isother) == 'csv':
			for each in filelst:
				self.csvfinder(each,self.findlist)
		
	@managed
	def finder(self, path2file,findlist):
		import os
		import io
		from io import FileIO, BufferedWriter
		import re
		
		print("Adding matches from " + str(path2file) + " to output: " + str(self.output))
		
		file2read = path2file
		

		with open(file2read, 'r') as f:
			rowcount = 0
			matchcount = 0
			
			with BufferedWriter(FileIO(self.output,'wb'),buffer_size=409600) as outf:
			
				line = f.readline()
				while line is not None:
					rowcount = rowcount + 1
					nugget = re.search(self.regex,line)
					if nugget == None:
							outf.write(str.encode('\n'.join(line)))
							matchcount = matchcount + 1
					else:
						pass
					line = f.readline()

			outf.close
			
			self.totline = self.totline + rowcount
			print("Done adding objects to file " + str(self.output))
			
			print("Total Rows in " + str(path2file) + " : " + str(rowcount))
			print("Total Matches in " + str(path2file) + " : " + str(matchcount))
	
	@managed
	def csvfinder(self,path2file,findlist):
		import os
		import io
		from io import FileIO, BufferedWriter
		import re
		import csv
		
		print("Adding matches from " + str(path2file) + " to output: " + str(self.output))
		
		with open(path2file, newline=self.newline, encoding='utf8') as csvfile:

			rowcount = 0
			matchcount = 0
			with BufferedWriter(FileIO(self.output,'wb'),buffer_size=409600) as outf:
				f = csv.reader(csvfile)
				for row in f:
					rowcount = rowcount + 1
					full = str(row)
					nugget = re.match(self.regex,full)
					if nugget != None:
						outf.write(str.encode(full + '\n'))
						matchcount = matchcount + 1

			outf.close
			
			self.totline = self.totline + rowcount
			print("Done adding objects to file " + str(self.output))
			
			print("Total Rows in " + str(path2file) + " : " + str(rowcount))
			print("Total Matches in " + str(path2file) + " : " + str(matchcount))

