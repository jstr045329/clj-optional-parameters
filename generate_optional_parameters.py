"""This script generates skeleton code for Clojure functions that take a dictionary parameter with optional keys. 
The point is to let you do things like this:

    (my-fun x y z {:optional-param 42})
    
However, the dictionary of optional parameters can be as large as you like, and every optional parameter gets
a default.

The motivation for this function is to make optional parameters more maintainable.

Use it like this:
    $ python generate_optional_parameters.py x 0 y 1 z fred"""
import sys
import os

def tab(n=1):
    return "  " * n

def main():
    function_name = sys.argv[1]
    los = sys.argv[2:]
    y = """(defn %s [your-args-here param-map]""" % (function_name)
    y += os.linesep + tab(1) + """(let ["""
    for i in range(0, len(los), 2):
        one_key = los[i]
        one_default = los[i+1]
        if (i > 0):
            y += tab(2)
        y += """%s (if (:%s param-map) (:%s param-map) %s)""" % (one_key, one_key, one_key, one_default)
        if i == (len(los) - 2):
            y += """]"""
        else:
            y += os.linesep + tab(2)
    y += os.linesep + tab(1) + "()) ;; Your code here"
    print(y)


if __name__ == "__main__":
    main()
