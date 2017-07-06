# Finder Config

output = 'lessfile.csv'
filelist = ['..\\dumpfile.csv']

# Try None, if that doesn't work you may want to try 'UTF-8' or 'windows-1252'.  There are probably others but I haven't taken the time to look at different encodings for this yet.

encoding = None

# findlist is capable of being individual regular expressions.  Be aware that some characters will require a \ or {} to mark them as literals.
findlist = ['Process', 'http://m/', 'SENSEORNOT']
