# LineSearch 

Currently this has only been tested in Python 3.6

Searches each line of the files contained in a list for a specific list of terms.  If a term is found on a line, it adds that line to a new file.

In addition it tracks the number of lines read in each file, matches in each file, total lines read, total matches, and times to a log file.

Terms should be standard text or regular expressions.  DO NOT use the preceding #r'# or #b'# prefixes.  If searching for an IP address or other special characters use brackets[] to wrap special characters.

For example: 192[.]168[.]0[.]199

Supports csv and txt (log) files.

# Instructions:

1. To execute, modify the finderconf.py file.
2. python main.py

-----

Future Dev:

* Enable alternative inputs/outputs (to make this more modular.)

* Need to double check the use of str() and need to make it pythonic.
 
-----

Added the ability to change encoding.

