def managed(func):
	
	import timeit
	
	def wrappedfunc(self, *args, **kwargs):
		start = timeit.default_timer()
		retval = func(self, *args, **kwargs)
		end = timeit.default_timer()
		tot = end - start
		print(func.__name__ + " total time: " + str(tot))
		return retval
	return wrappedfunc

class findinline:
	
	# from csvfindinline import csvfindinline
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
		self.littelist = None
		self.biglist = None
		self.newline = None
		self.comreg = None

		for each in self.findlist:
			place = self.findlist.index(each)
			neweach = '(' + str(each) + ')'
			del self.findlist[place]
			self.findlist.insert(place,neweach)
			
		comreg = '|'.join(self.findlist)
		self.comreg = 'r' + "'.*" + str(comreg) + ".*'"
		self.regex = re.compile(str(self.comreg))
	
	@managed
	def makenew(self):
		
		import os
		import io
		
		print(str(self.comreg))
		
		print("Searching these files: " + str(self.filelist) + "\n For these things: " + str(self.findlist))
		
		self.biglist = self.searchfiles(self.filelist,self.findlist)

		betterlog = open(self.output, 'w')
		for littlelist in self.biglist:
			for record in littlelist:
				betterlog.write(str(record))
			
		betterlog.close
		
	@managed
	def searchfiles(self,filelst,findlst):
		import os
		
		biglist = []
		
		print("Createing BIGLIST from LITTLELISTS.")
		
		# print("Here's your isother statement: " + str(self.isother))
		
		if str(self.isother) == None:
			for each in filelst:
				self.littlelist = self.finder(each,self.findlist)
				for those in self.littlelist:
					biglist.append([those])
		elif str(self.isother) == 'csv':
			for each in filelst:
				self.littlelist = self.csvfinder(each,self.findlist)
				for those in self.littlelist:
					biglist.append([those])
				
		print("Finished creating Biglist.")
		
		return biglist
		
	@managed
	def finder(self, path2file,findlist):
		import os
		import io
		import re
		
		print("Creating a LITTLELIST from " + str(path2file) + ".")
		
		file2read = path2file
		littlelist = []

		with open(file2read) as f:
			rowcount = 0
			matchcount = 0
			for line in f:
				rowcount = rowcount + 1
				nugget = re.search(self.regex,line)
				if nugget != None:
					matchcount = matchcount + 1
					putter = str(line)
					littlelist.append(putter)
			
			length = len(littlelist)
			print("Done creating or updating a LITTLELIST with " + str(length) + " objects.")
			print(rowcount)
			print(matchcount)

		return littlelist
	
	@managed
	def csvfinder(self,path2file,findlist):
		import os
		import io
		import re
		import csv
		
		print("Creating a LITTLELIST from " + str(path2file) + ".")

		littlelist = []
		
		with open(path2file, newline=self.newline, encoding='utf8') as csvfile:
			f = csv.reader(csvfile)
			rowcount = 0
			matchcount = 0
			for row in f:
				rowcount = rowcount + 1
				nugget = re.search(self.regex,str(row))
				if nugget != None:
					matchcount = matchcount + 1
					putter = row
					littlelist.append(putter)

			length = len(littlelist)
			print("Done creating or updating a LITTLELIST with " + str(length) + " objects.")
			print("Total Rows in " + str(path2file) + " : " + rowcount)
			print("Total Matches in " + str(path2file) + " : " + matchcount)
			
		return littlelist

