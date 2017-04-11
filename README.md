# LineSearch 

Searches each line of the files contained in a list for a specific list of terms.  If a term is found on a line, it adds that line to a new file.

Terms should be standard text or regular expressions.  DO NOT use the preceding #r'# or #b'# prefixes.  If searching for an IP address or other special characters use brackets[] to wrap special characters.

For example: 192[.]168[.]0[.]199

Currently supports csv and txt (log) files.

# Instructions:

1. To execute, modify the finderconf.py file.
2. Open the python interpretter.
3. '>>> from findinline import findinline'
4. '>>> finder = findinline()'
5. '>>> finder.makenew()'

-----

Future Dev:

* Enable alternative outputs.

* Need to double check the use of str() and need to make it pythonic.

* Add a driver to make execution easier.
