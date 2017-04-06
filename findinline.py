class findinline():
    
    # from findinline import findinline
    # finder = findinline()
    # finder.makenew()
    
    def __init__(self):
        from finderconf import filelist
        from finderconf import findlist
        
        self.filelist = filelist
        self.findlist = findlist
        self.littelist = None
        self.biglist = None

    def makenew(self):
        
        import os
        import io
        
        print("Searching these files: " + str(self.filelist) + "\n For these things: " + str(self.findlist))
        
        self.biglist = self.searchfiles(self.filelist,self.findlist)
        
        betterlog = open('betterlog.txt', 'w')
        for littlelist in self.biglist:
            for record in littlelist:
                betterlog.write(str(record))
            
        betterlog.close
        

    def searchfiles(self,filelst,findlst):
        import os
        
        biglist = []
        
        print("Createing BIGLIST from LITTLELISTS.")
        
        for each in filelst:
            self.littlelist = self.finder(each,self.findlist)
            for those in self.littlelist:
                biglist.append([those])
                
        print("Finished creating Biglist.")
        
        return biglist
    
    def finder(self, path2file,findlist):
        import os
        import io
        import re
        
        print("Creating a LITTLELIST from " + str(path2file) + ".")
        
        file2read = path2file
        littlelist = []
        for each in findlist:
            regex = r'' + str(each) + ''
            print("Searching for: " + str(regex))
            with open(file2read) as f:
                for line in f:
                    nugget = re.search(regex,line)
                    if nugget != None:
                        putter = str(line)
                        littlelist.append(putter)
            
            length = len(littlelist)
            print("Done creating or updating a LITTLELIST with " + str(length) + " objects.")

        return littlelist
        
