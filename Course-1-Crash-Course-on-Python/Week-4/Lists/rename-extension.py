# Given a list of filenames, we want to rename all the files with extension 
# hpp to the extension h. To do this, we would like to generate a new list 
# called newfilenames, consisting of the new filenames. 

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [name.replace(".hpp", ".h") if ".hpp" in name else name for name in filenames]  

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]