'''
Doctring Synopsis
he convention followed for a docstring is a multi-line string where the first line starts with a capital letter and ends with a dot. Then the second line is blank followed by any detailed explanation starting from the third line. You are strongly advised to follow this convention for all your docstrings for all your non-trivial functions.
We can access the docstring of the printMax function using the __doc__ (notice the double underscores) attribute (name belonging to) of the function. Just remember that Python treats everything as an object and this includes functions. We'll learn more about objects in the chapter on classes.
If you have used the help() in Python, then you have already seen the usage of docstrings! What it does is just fetch the __doc__ attribute of that function and displays it in a neat manner for you. You can try it out on the function above - just include help(printMax) in your program. Remember to press q to exit the help.
Automated tools can retrieve the documentation from your program in this manner. Therefore, I strongly recommend that you use docstrings for any non-trivial function that you write. The pydoc command that comes with your Python distribution works similarly to help() using docstrings.
'''

def printMax(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x = int(x)  # convert to integers, if possible
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'


printMax(3, 5)
#printMax.__doc__
help(printMax)
