                                    #MODULES


#modules are simply python files with the .py extension which implement a set of functions.
#modules are imported using the import command

#first time a module is loaded, it is initialized by executing the code. 
#if another module imports the same module again, it won't be loaded twice. - so local var's inside the module act as a singleton. they are init'd only once.

#if we want to import the urllib.request module, which enables us to request data from URLs


import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)

# Notice how we used urllib.request as a variable to refer to our module and then we called the methods using dot notation.

                                #CREATING YOUR OWN MODULES

#literally just import your .py file that has what you want. it must be in the same directory as the as the file that will import the module. 

#Writing your own Python modules is very simple. To create a module, we first create a new .py file with the module name in the same directory as the file that will import the module. Then we import it using the import command and the Python file name (without the .py extension)

#lets create a module of arithmetic ops.
#first create the .py file 
#<--- should be in the same DIRECTORY

        # import arithmetic
        # print(arithmetic.add(5, 8))
        # print(arithmetic.subtract(10, 5))
        # print(arithmetic.multiply(12, 6))

                                        #STANDARD (Built In) Modules

# Python comes with a library of standard modules. Some modules are built into the interpreter; these provide access to operations that are not part of the core of the language but are nevertheless built-in, either for efficiency or to provide access to operating system primitives such as system calls. The set of such modules is a configuration option which also depends on the underlying platform. For example, the winreg module is only provided on Windows systems. One particular module deserves special mention: sys, which is built into every Python interpreter.

#list of built in modules https://docs.python.org/3.6/library/index.html


                            # EXPLORING Built in modules

# Two very important functions come in handy when exploring modules in Py. the DIR and HELP functions. We can look for which functions are implemented in each module by using the dir function

dir(urllib.request)
# https://s3.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/Screen_Shot_2018-03-22_at_7.32.58_PM.png

                                    #Packages
#a module is a single file (or files) that is imported under one import.
#A PACKAGE is a collection of modules in directories that give a package hierarchy.

#just an ex
# from my_package.subdirectory import my_functions

# packages are namespaces which contain multiple packages and modules themselves.
# they are simplyt directories but with a twist

# sample_project
#      |_____ python_file.py
#      |_____ my_modules
#                |_____ __init__.py
#                |_____ test_module.py
#                |_____ another_module.py
#                |_____ third_module.py

#in the above diagram, the package name is my_modules.


                                            # WRITING PACKAGES 

# if/when we createa  directory called MY_MODULES, which marks the package name, we can then create a module inside that package called TEST_MODULE

# to use the module TEST_MODULES we can import it in two ways
# import my_modules.test.module
#OR
# from my_modules import test_module



                                    # __init__.py File
#in python2.7, it was required. nowadays its probably and often empty. but it was used to to indicated that files in the folder were part of the package.

#in python3.3, we only need the file if we need to customize what modules are available to anyone attempting to import the package.
#for ex, if we didnt want another_module or thid_module to be accessbile for importing, we could override the __ALL__ variable like so:

#sampleproj/my_modules/__init__.py
#__all__ = ["test_module"]