# the name of the import matches the file name (minus the .py)
# these two files MUST BE IN THE SAME DIRECTORY
import first_module

first_module.main() # this will fire off the first module's main function

print("Module #2 Name=", __name__)
