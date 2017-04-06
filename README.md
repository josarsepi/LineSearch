# LineSearch 

Searches each line of the files contained in a list for a specific list of terms.  If a term is found on a line, it adds that line to a new file called betterlog.txt.

It definately needs some optimization.

-----

Future Dev:

* Have a single regex built from the config list that can be compiled at the time the class is called up.  May increase the speed of searches.

* Make it work with lists, strings, or dicts.

* Enable alternative outputs.

* Need to double check the use of str() and need to make it pythonic.
