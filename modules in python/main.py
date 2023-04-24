import utility

print(utility)
print(utility.add(1,3))
print(utility.multiply(5, 8))

# when this file runs a folder __pycache__ is created 
# This folder has a compiled cache file of the utility.py file 
# so when we run the main.py file again then the cached version of utility file is loaded for performance boost

# if we modify the utility.py file and run the main.py file again then the interpreter re-runs the utility file and updates the cache version of the same file.


