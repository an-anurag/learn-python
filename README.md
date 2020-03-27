## Functional Python
### Introduction
* History
* Features
* Limitations
* Versions
* Installation
* Running python program

---------------------------------------------------------------------------------------------------------------------

### Basics
* **Statements**

* **Keywords (35)**
    1. Difference between `del` and `None`:
    1. `async` and `await` - python 3.7

* **Character set**
    1. A-Z
    1. a-z
    1. 0-9
    1. Underscore in Python.
        1. For storing the value of last expression in interpreter.
        1. For ignoring the specific values. (so-called “I don’t care”)
        1. To give special meanings and functions to name of vartiables or functions.
        1. To use as ‘Internationalization(i18n)’ or ‘Localization(l10n)’ functions.
        1. To separate the digits of number literal value.
* **Identifiers**
* **Literals**
    1. Int literals
    1. String literals
* **Variables**
* **Constants**
* **comments**
    1. single line
    1. multiline
* **Interactive shell**
* **Indentation**

---------------------------------------------------------------------------------------------------------------------

### Operators
* Types:
    1. **Arithmetic Operators**
        1. `+` ==>Addition
        1. `-` ==>Subtraction
        1. `*` ==>Multiplication
        1. `/`   ==>Division operator
        1. `%`   ===>Modulo operator
        1. `//`  ==>Floor Division operator
        1. `**`  ==>Exponent operator or power operator
    2. **Relational Operators or Comparison Operators**
        * `>`
        * `<`
        * `>=`
        * `>=`
        * `==`
        * `!=`
    3. **Equality operators**
        * `==`
        * `!=`
        * Chaining
    4. **Logical operators**
        * `and`
        * `or`
        * `not`
        * Boolean types behaviour
            1. and ==>If both arguments are True then only result is True
            1. or ====>If atleast one arugemnt is True then result is True
            1. not ==>complement
            1. True and False ==>False
            1. True or False ===>True
            1. not False ==>True
        * Non boolean types behaviour
            1. x and y:
                1. if x is evaluates to false return x otherwise return y
            1. x or y:
                1. If x evaluates to True then result is x otherwise result is y
    5. **Bitwise oeprators**
        * `&`
        * `|`
        * `^`
        * `~`
        * `<<`
        * `>>`
    6. **Assignment operators**
        * `=`
        * Augmented Assignments
            * `+=`
            * `-=`
            * `*=`
            * `/=`
            * `//=`
            * `**=`
    7. **Ternary operators**
    6. **Special operators**
        
        1. **Identity Operators**
            1. `is`
            2. `is not`
        2. **Membership operators**
            1. `in`
            2. `not in`
    7. **Walrus operator**
        * `->`
* **Operator precedence**

---------------------------------------------------------------------------------------------------------------------

### Data types
* **Fundamental types**
    1. int
    1. float
    1. complex
    1. bool
    1. str

1. **int**
    1. Literals
        1. Binary
        1. Octals
        1. Hexadecimals

2. **float**

3. **complex**

4. **bool**

5. **str**
    1. literals
        1. single line
        1. multiline
    1. Raw strings
    1. Operations
        1. Accessing
        1. Indexing
        1. Slicing
        
    1. Operators for string
        1. `+` operator for concatenation
        2. `*` operator for repetition
        3. <,<=,>,>= Comparison
        4. ==,!= equality
        5. in , not in membership

    1. Formatting
    1. Escape Sequenses
        * \a	ASCII Bell (BEL) character
        * \b	ASCII Backspace (BS) character
        * \f	ASCII Formfeed (FF) character
        * \n	ASCII Linefeed (LF) character
        * \N{<name>}	Character from Unicode database with given <name>
        * \r	ASCII Carriage Return (CR) character
        * \t	ASCII Horizontal Tab (TAB) character
        * \uxxxx	Unicode character with 16-bit hex value xxxx
        * \Uxxxxxxxx	Unicode character with 32-bit hex value xxxxxxxx
        * \v	ASCII Vertical Tab (VT) character
        * \oxx	Character with octal value xx
        * \xhh	Character with hex value hh
    1. Methods
        * capitalize()	Converts the first character to upper case
        * casefold()	Converts string into lower case
        * center()	Returns a centered string
        * count()	Returns the number of times a specified value occurs in a string
        * encode()	Returns an encoded version of the string
        * endswith()	Returns true if the string ends with the specified value
        * expandtabs()	Sets the tab size of the string
        * find()	Searches the string for a specified value and returns the position of where it was found
        * format()	Formats specified values in a string
        * format_map()	Formats specified values in a string
        * index()	Searches the string for a specified value and returns the position of where it was found
        * isalnum()	Returns True if all characters in the string are alphanumeric
        * isalpha()	Returns True if all characters in the string are in the alphabet
        * isdecimal()	Returns True if all characters in the string are decimals
        * isdigit()	Returns True if all characters in the string are digits
        * isidentifier()	Returns True if the string is an identifier
        * islower()	Returns True if all characters in the string are lower case
        * isnumeric()	Returns True if all characters in the string are numeric
        * isprintable()	Returns True if all characters in the string are printable
        * isspace()	Returns True if all characters in the string are whitespaces
        * istitle()	Returns True if the string follows the rules of a title
        * isupper()	Returns True if all characters in the string are upper case
        * join()	Joins the elements of an iterable to the end of the string
        * ljust()	Returns a left justified version of the string
        * lower()	Converts a string into lower case
        * lstrip()	Returns a left trim version of the string
        * maketrans()	Returns a translation table to be used in translations
        * partition()	Returns a tuple where the string is parted into three parts
        * replace()	Returns a string where a specified value is replaced with a specified value
        * rfind()	Searches the string for a specified value and returns the last position of where it was found
        * rindex()	Searches the string for a specified value and returns the last position of where it was found
        * rjust()	Returns a right justified version of the string
        * rpartition()	Returns a tuple where the string is parted into three parts
        * rsplit()	Splits the string at the specified separator, and returns a list
        * rstrip()	Returns a right trim version of the string
        * split()	Splits the string at the specified separator, and returns a list
        * splitlines()	Splits the string at line breaks and returns a list
        * startswith()	Returns true if the string starts with the specified value
        * strip()	Returns a trimmed version of the string
        * swapcase()	Swaps cases, lower case becomes upper case and vice versa
        * title()	Converts the first character of each word to upper case
        * translate()	Returns a translated string
        * upper()	Converts a string into upper case
        * zfill()	Fills the string with a specified number of 0 values at the beginning
6. **bytes**

7. **bytearray**

8. **range**

9. **list**
    1. defining list
        1. list = []
        2. list=[10,20,30,40]
        3. With dynamic input: (eval)
        4. With list() function:
    1. Operations
        1. Indexing
        1. Slicing
        1. Traversing
            1. using for loop
    1. List vs immutability:
    1. cloning
        Difference between = operator and copy() function
    1. Operators for list
        1. Concatenation operator(+):
        2. Repetition Operator(*):
        3. Comparison
            ==,!=
            <,<=,>,>=
        4. in , not in Membership
    1. Nested list
        Nested List as Matrix:
    1. Comprehensions
    1. Methods
        * append()	Adds an element at the end of the list
        * clear()	Removes all the elements from the list
        * copy()	Returns a copy of the list
        * count()	Returns the number of elements with the specified value
        * extend()	Add the elements of a list (or any iterable), to the end of the current list
        * index()	Returns the index of the first element with the specified value
        * insert()	Adds an element at the specified position
        * pop()	Removes the element at the specified position
        * remove()	Removes the first item with the specified value
        * reverse()	Reverses the order of the list
        * sort()	Sorts the list

10. **tuple**
    1. Defining tuple
        1. t=()
        2. t=(10,)
        3. t=10,20,30
        4. tuple()
    1. Operations
        1. Indexing
        1. Slicing
        1. Traversing
            using for loop
    1. Tuple vs immutability:
    1. Operators for tuple
        1. Concatenation operator(+):
        2. Repetition Operator(*):
        3. in , not in Membership
    1. Tuple Packing and Unpacking:
    1. Tuple comprehension
    1. Methods
        * count()	Returns the number of times a specified value occurs in a tuple
        * index()	Searches the tuple for a specified value and returns the position of where it was found

11. **set**
    1. Defining set
        1. using set()
    1. Set vs immutability:
    1. Operations:
        1. Union
        1. Intersection
        1. Difference
        1. Symmetric difference
    1. Operators for set
        1. Membership operators: (in , not in)
    1. Set comprehension
    1. Methods
        * add()	Adds an element to the set
        * clear()	Removes all the elements from the set
        * copy()	Returns a copy of the set
        * difference()	Returns a set containing the difference between two or more sets
        * difference_update()	Removes the items in this set that are also included in another, specified set
        * discard()	Remove the specified item
        * intersection()	Returns a set, that is the intersection of two other sets
        * intersection_update()	Removes the items in this set that are not present in other, specified set(s)
        * isdisjoint()	Returns whether two sets have a intersection or not
        * issubset()	Returns whether another set contains this set or not
        * issuperset()	Returns whether this set contains another set or not
        * pop()	Removes an element from the set
        * remove()	Removes the specified element
        * symmetric_difference()	Returns a set with the symmetric differences of two sets
        * symmetric_difference_update()	inserts the symmetric differences from this set and another
        * union()	Return a set containing the union of sets
        * update()	Update the set with the union of this set and others

12. **frozenset**

13. **dict**
    1. Defining dicts
        1. d = {}
        2. d = dict()
    1. Operations
        1. Accessing
        1. Updating dicts
        1. deleting elements
    1. dict comprehensions
    1. Methods
        * clear()	Removes all the elements from the dictionary
        * copy()	Returns a copy of the dictionary
        * fromkeys()	Returns a dictionary with the specified keys and values
        * get()	Returns the value of the specified key
        * items()	Returns a list containing a tuple for each key value pair
        * keys()	Returns a list containing the dictionary's keys
        * pop()	Removes the element with the specified key
        * popitem()	Removes the last inserted key-value pair
        * setdefault()	Returns the value of the specified key. If the key does not exist:
                        insert the key, with the specified value
        * update()	Updates the dictionary with the specified key-value pairs
        * values()	Returns a list of all the values in the dictionary
14. **None**

---------------------------------------------------------------------------------------------------------------------

### Mutability & Immutability

---------------------------------------------------------------------------------------------------------------------


### Shallow and Deep Copy

---------------------------------------------------------------------------------------------------------------------

### Type Casting
1. int()
1. float()
1. complex()
1. bool()
1. str()
1. list()
1. tuple()

---------------------------------------------------------------------------------------------------------------------

### Input and output statements
1. raw_input()
1. input()
1. print()
    1. Formatted string
        1. %i - int
        1. %d - int
        1. %f - float
        1. %s - String type
        1. %r - 
        1. print with {} operator

---------------------------------------------------------------------------------------------------------------------

### Command line arguments
1. Modules:
    1. sys
    1. argparse
    1. getopt
    1. optparse

---------------------------------------------------------------------------------------------------------------------

### Flow controls
1. **Conditionals**
    1. if
    2. if-elif
    3. if-elif-else
2. **Iterative**
    1. for-else
    2. while-else
3. **Transfer**
    1. continue
    2. break
    3. pass

---------------------------------------------------------------------------------------------------------------------

### Iterators and Iterable

An object is called iterable if we can get an iterator from it
1. Creating iterator
2. Iterating iterator
3. Internal working of for loop
4. Building your own iterator
4. Infinite Iterators

---------------------------------------------------------------------------------------------------------------------

### Functions:
**Types:**
1. **Built in Functions**
    1.  **Math**
        1. abs()	Returns absolute value of a number
        1. divmod()	Returns quotient and remainder of integer division
        1. max()	Returns the largest of the given arguments or items in an iterable
        1. min()	Returns the smallest of the given arguments or items in an iterable
        1. pow()	Raises a number to a power
        1. round()	Rounds a floating-point value
        1. sum()	Sums the items of an iterable

    1. **Type Conversion**
        1. ascii()	Returns a string containing a printable representation of an object
        1. bin()	Converts an integer to a binary string
        1. bool()	Converts an argument to a Boolean value
        1. chr()	Returns string representation of character given by integer argument
        1. complex()	Returns a complex number constructed from arguments
        1. float()	Returns a floating-point object constructed from a number or string
        1. hex()	Converts an integer to a hexadecimal string
        1. int()	Returns an integer object constructed from a number or string
        1. oct()	Converts an integer to an octal string
        1. ord()	Returns integer representation of a character
        1. repr()	Returns a string containing a printable representation of an object
        1. str()	Returns a string version of an object
        1. type()	Returns the type of an object or creates a new type object

    1. **Iterables and Iterators**
        1. all()	Returns True if all elements of an iterable are true
        1. any()	Returns True if any elements of an iterable are true
        1. enumerate()	Returns a list of tuples containing indices and values from an iterable
        1. filter()	Filters elements from an iterable
        1. iter()	Returns an iterator object
        1. len()	Returns the length of an object
        1. map()	Applies a function to every item of an iterable
        1. next()	Retrieves the next item from an iterator
        1. range()	Generates a range of integer values
        1. reversed()	Returns a reverse iterator
        1. slice()	Returns a slice object
        1. sorted()	Returns a sorted list from an iterable
        1. zip()	Creates an iterator that aggregates elements from iterables

    1. **Composite Data Type**
        1. bytearray()	Creates and returns an object of the bytearray class
        1. bytes()	Creates and returns a bytes object (similar to bytearray, but immutable)
        1. dict()	Creates a dict object
        1. frozenset()	Creates a frozenset object
        1. list()	Constructs a list object
        1. object()	Returns a new featureless object
        1. set()	Creates a set object
        1. tuple()	Creates a tuple object

    1. **Classes, Attributes, and Inheritance**
        1. classmethod()	Returns a class method for a function
        1. delattr()	Deletes an attribute from an object
        1. getattr()	Returns the value of a named attribute of an object
        1. hasattr()	Returns True if an object has a given attribute
        1. isinstance()	Determines whether an object is an instance of a given class
        1. issubclass()	Determines whether a class is a subclass of a given class
        1. property()	Returns a property value of a class
        1. setattr()	Sets the value of a named attribute of an object
        1. super()	Returns a proxy object that delegates method calls to a parent or sibling class

    1. **Input/Output**
        1. format()	Converts a value to a formatted representation
        1. input()	Reads input from the console
        1. open()	Opens a file and returns a file object
        1. print()	Prints to a text stream or the console
        1. Variables, References, and Scope
        1. Function	Description
        1. dir()	Returns a list of names in current local scope or a list of object attributes
        1. globals()	Returns a dictionary representing the current global symbol table
        1. id()	Returns the identity of an object
        1. locals()	Updates and returns a dictionary representing current local symbol table
        1. vars()	Returns __dict__ attribute for a module, class, or object

    1. **Miscellaneous**
        1. callable()	Returns True if object appears callable
        1. compile()	Compiles source into a code or AST object
        1. eval()	Evaluates a Python expression
        1. exec()	Implements dynamic execution of Python code
        1. hash()	Returns the hash value of an object
        1. help()	Invokes the built-in help system
        1. memoryview()	Returns a memory view object
        1. staticmethod()	Returns a static method for a function
        1. `__import__()`	Invoked by the import statement


1. **User Defined Functions**
    1. defining a function
    2. calling a function
    3. returning from function
    1. namespace
    1. global Vs local variables
    4. function arguments
        1. positional args
        2. default args
        3. keyword args
        4. `**args`
        5. `**kwargs`
    5. Nested functions
        1. defining nested function
        2. calling nested function
        3. returning nested functions which is not returning value
        3. returning nested functions which is returning value
        4. returning nested function reference which is not returning value
        4. returning nested function reference which is returning value
        5. function closure
        6. use of `global` keyword
        7. use of `nonlocal` keyword
    6. function aliasing
    7. Function as a argument
        1. calling passed function
        2. returning passed function call
        3. returning passed function reference
    7. generators
        1. Using functions
        2. Using generator expressions
        3. yield from
        4. `send()`
    8. function decorators
        1. without function args
        2. with function args
        3. with decorator args
        4. with @wrap
        5. decorator chaining
    9. Recursive functions
    10. Lambda function

---------------------------------------------------------------------------------------------------------------------

### Special variables

1. `__bases__`
1. `__builtins__`
1. `__call__`
1. `__class__`
1. `__closure__`
1. `__dict__`
1. `__doc__`
1. `__file__`
1. `__init__`
1. `__init_subclass__`
1. `__loader__`
1. `__main__`
1. `__metaclass__`
1. `__module__`
1. `__new__`
1. `__name__`
1. `__package__`
1. `__prepare__`
1. `__slots__`
1. `__subclasshook__`
1. `__spec__`
1. `__weakref__`


---------------------------------------------------------------------------------------------------------------------

### File Handling
1. **syntax**
    1. open()
    2. with open()

2. **Access modes**

    1. <r>	It opens a file in read-only mode while the file offset stays at the root.
    1. <rb>	It opens a file in (binary + read-only) modes. And the offset remains at the root level.
    1. <r+>	It opens the file in both (read + write) modes while the file offset is again at the root level.
    1. <rb+>	It opens the file in (read + write + binary) modes. The file offset is again at the root level.
    1. <w>	It allows write-level access to a file. If the file already exists, then it’ll get overwritten. It’ll create a new file if the same doesn’t exist.
    1. <wb>	Use it to open a file for writing in binary format. Same behavior as for write-only mode.
    1. <w+>	It opens a file in both (read + write) modes. Same behavior as for write-only mode.
    1. <wb+>	It opens a file in (read + write + binary) modes. Same behavior as for write-only mode.
    1. <a>	It opens the file in append mode. The offset goes to the end of the file. If the file doesn’t exist, then it gets created.
    1. <ab>	It opens a file in (append + binary) modes. Same behavior as for append mode.
    1. <a+>	It opens a file in (append + read) modes. Same behavior as for append mode.
    1. <ab+>	It opens a file in (append + read + binary) modes. Same behavior as for append mode.
    1. 'x'	Creates a new file. If file already exists, the operation fails.
    1. 't'	This is the default mode. It opens in text mode.
    1. 'b'	This opens in binary mode.

3. **Methods**
    1. close()	Close an open file. It has no effect if the file is already closed.
    1. detach()	Separate the underlying binary buffer from the TextIOBase and return it.
    1. fileno()	Return an integer number (file descriptor) of the file.
    1. flush()	Flush the write buffer of the file stream.
    1. isatty()	Return True if the file stream is interactive.
    1. read(n)	Read atmost n characters form the file. Reads till end of file if it is negative or None.
    1. readable()	Returns True if the file stream can be read from.
    1. readline(n=-1)	Read and return one line from the file. Reads in at most n bytes if specified.
    1. readlines(n=-1)	Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.
    1. seek(offset,from=SEEK_SET)	Change the file position to offset bytes, in reference to from (start, current, end).
    1. seekable()	Returns True if the file stream supports random access.
    1. tell()	Returns the current file location.
    1. truncate(size=None)	Resize the file stream to size bytes. If size is not specified, resize to current location.
    1. writable()	Returns True if the file stream can be written to.
    1. write(s)	Write string s to the file and return the number of characters written.
    1. writelines(lines)	Write a list of lines to the file.

4. **Modules:**
    1. os
    1. pathlib
    1. tempfile
    1. shutil
    1. zipfile
    1. tarfile
    1. fileinput

5. **Common Operation**
    1. Get directory contents and file properties
    1. Create directories and directory trees
    1. Filename pattern matching
    1. Traversing dir and processing file
    1. Deleting files and dir
    1. Move, rename, copy, and delete files or directories
    1. Create temporary files and directories
    1. Read and extract data from different types of archives
        1. zip
        1. tar
    1. Read multiple files simultaneously using fileinput
    1. Reading continuously growing file

6. Working with csv files
7. working with JSON data
8. Python File Encoding

---------------------------------------------------------------------------------------------------------------------
### Context Managers
* with function
* with classes

---------------------------------------------------------------------------------------------------------------------

### Exception handling
1. **keywords**
    1. try
    1. except
    1. finally
    1. else
    1. raise

1. **Exception hierarchy**
   
    1. BaseException
        * SystemExit
        * KeyboardInterrupt
        * GeneratorExit
        * Exception
            * StopIteration
            * StopAsyncIteration
            * ArithmeticError
                * FloatingPointError
                * OverflowError
                * ZeroDivisionError
            * AssertionError
          * AttributeError
          * BufferError
          * EOFError
          * ImportError
              * ModuleNotFoundError
          * LookupError
              * IndexError
              * KeyError
          * MemoryError
          * NameError
            * UnboundLocalError
          * OSError
              * BlockingIOError
              * ChildProcessError
              * ConnectionError
                  * BrokenPipeError
                  * ConnectionAbortedError
                  * ConnectionRefusedError
                  * ConnectionResetError
              * FileExistsError
              * FileNotFoundError
              * InterruptedError
              * IsADirectoryError
              * NotADirectoryError
              * PermissionError
              * ProcessLookupError
              * TimeoutError
          * ReferenceError
          * RuntimeError
              * NotImplementedError
              * RecursionError
          * SyntaxError
            * IndentationError
                * TabError
          * SystemError
          * TypeError
          * ValueError
            * UnicodeError
              * UnicodeDecodeError
              * UnicodeEncodeError
              * UnicodeTranslateError
          * Warning
               * DeprecationWarning
               * PendingDeprecationWarning
               * RuntimeWarning
               * SyntaxWarning
               * UserWarning
               * FutureWarning
               * ImportWarning
               * UnicodeWarning
               * BytesWarning
               * ResourceWarning

---------------------------------------------------------------------------------------------------------------------

## Modular Python
1. Builtin modules
2. User defined modules
3. Imports
    1. Absolute imports
    2. Relative imports
4. Module aliasing while importing
5. Member aliasing
6. Reloading a module
7. Finding members of module using dir()
4. `if __name__ == '__main__'`
               
---------------------------------------------------------------------------------------------------------------------

### Regular expression

1. Metacharacters:

    1. `\`	escape special characters
    1. `.`	matches any character
    1. `^`	matches beginning of string
    1. `$`	matches end of string
    1. `[5b-d]`	matches any chars '5', 'b', 'c' or 'd'
    1. `[^a-c6]`	matches any char except 'a', 'b', 'c' or '6'
    1. `R|S`	matches either regex R or regex S
    1. `()`	creates a capture group and indicates precedence
    
1. Quantifiers    
    1. `*`  0 or more (append ? for non-greedy)
    1. `+`	1 or more (append ? for non-greedy)
    1. `?`	0 or 1 (append ? for non-greedy)
    1. `{m}`	exactly mm occurrences
    1. `{m, n}`	from m to n. m defaults to 0, n to infinity
    1. `{m, n}?`	from m to n, as few as possible
    
1. Special sequences    
    1. `\A`	start of string
    1. `\b`	matches empty string at word boundary (between \w and \W)
    1. `\B`	matches empty string not at word boundary
    1. `\d`	digit
    1. `\D`	non-digit
    1. `\s`	whitespace: `[ \t\n\r\f\v]`
    1. `\S`	non-whitespace
    1. `\w`	alphanumeric: `[0-9a-zA-Z_]`
    1. `\W`	non-alphanumeric
    1. `\Z`	end of string
    1. `\g<id>`	matches a previously defined group
    1. `(?iLmsux)`	matches empty string, sets re.X flags
    1. `(?:...)`	non-capturing version of regular parentheses
    1. `(?P...)`	matches whatever matched previously named group
    1. `(?P=)`	digit
    1. `(?#...)`	a comment; ignored
    1. `(?=...)`	lookahead assertion: matches without consuming
    1. `(?!...)`	negative lookahead assertion
    1. `(?<=...)`	lookbehind assertion: matches if preceded
    1. `(?<!...)`	negative lookbehind assertion
    1. `(?(id)yes|no)`	match 'yes' if group 'id' matched, else 'no'
    
1. Method:
    1. `match()` Returns match object on successful search
    1. `findall()`	Returns a list containing all matches
    1. `search()`	Returns a Match object if there is a match anywhere in the string
    1. `split()`	Returns a list where the string has been split at each match
    1. `sub()`	Replaces one or many matches with a string
    1. `subn()` The re.subn() is similar to re.sub() except it returns a tuple of 2 items containing the new string and the number of substitutions made.

1. Flags:

    1. [re.M]	Make begin/end consider each line
    1. [re.I]	It ignores case
    1. [re.S]	Make [ . ]
    1. [re.U]	Make { \w,\W,\b,\B} follows Unicode rules
    1. [re.L]	Make {\w,\W,\b,\B} follow locale
    1. [re.X]	Allow comment in Regex

---------------------------------------------------------------------------------------------------------------------
### Date and time

1. Modules
    1. `time`
    1. `datetime`
    
1. Methods

---------------------------------------------------------------------------------------------------------------------
### Collections

1. Name

---------------------------------------------------------------------------------------------------------------------
### Database Programming

1. DB-API
1. Modules
1. Connections
1. Cursors
1. Connection strings
1. Exceptions
1. Methods
    1. connect()
    1. execute()
    1. executemany()
    1. fetch()
    1. fetchone()
    1. fetchall()
    1. close()    

---------------------------------------------------------------------------------------------------------------------

## Object Oriented Python

### Classes and Objects
1. class
1. object
    1. in Python, everything is an object. 
    1. __new__, __init__
1. Old style and new style classes
    1. class != type -- old --upto P2.2
    1. class == type -- new --P3
        
1. `self` Reference variable
1. Constructor
    1. __init__
1. Variables
    1. Access modifiers
        1. public, protected, private
    1. Instance variables
        1. Operations
            1. Creation
                1. Inside Constructor by using self variable
                1. Inside Instance Method by using self variable:
                1. Outside of the class by using object reference variable:
            2. Access
                We can access instance variables with in the class by using self variable and outside of the class by
                using object reference.
            3. Deletion
                1. Within a class we can delete instance variable as follows
                del self.variableName
                2. From outside of class we can delete instance variables as follows
                del objectreference.variableName
                          
    1. static variables
        1. Operations
            1. Creation
                1. In general we can declare within the class directly but from out side of any method
                2. Inside constructor by using class name
                3. Inside instance method by using class name
                4. Inside classmethod by using either class name or cls variable
                5. Inside static method by using class name
            2. Access
                1. inside constructor: by using either self or classname
                2. inside instance method: by using either self or classname
                3. inside class method: by using either cls variable or classname
                4. inside static method: by using classname
                5. From outside of class: by using either object reference or classnmae
            3. Modification
                If we change the value of static variable by using either self
                or object reference variable:
            3. Deletion
                We can delete static variables from anywhere by using the following syntax
                del classname.variablename
                But inside classmethod we can also use cls variable
                del cls.variablename

    1. local variables
        1. Operations
            1. Creation
            2. Access
            3. Modification
            3. Deletion
            
1. Methods
    1. Instance methods
    1. Class methods
    1. Static methods

1. Inner classes:

1. class decorator
    1. implement __init__
    1. implement __call__ 

1. nested methods

1. Meta classes
    1. They allow customization of class instantiation.
    1. Metaclasses are sometimes referred to as class factories.
    1. When defining a class and no metaclass is defined the default type metaclass will be used
    1. the type of any new-style class is type.
    1. The type of the built-in classes you are familiar with is also type:
    1. For that matter, the type of type is type as well (yes, really):
    1. type is a metaclass, of which classes are instances
    1. In the above case:
        1. x is an instance of class Foo.
        1. Foo is an instance of the type metaclass.
        1. type is also an instance of the type metaclass, so it is an instance of itself.
        
    1. Creation
        1. one
            1. using separate class
            1. implement __new__ with cls, name, base, dct
            1. call super().__new__(cls, name, bases, dct)
            1. add this newly created metaclass via `metaclass=` kwarg
        1. two
            1. Inheriting class that has already passed in `metaclass=` kwarg
    1. singletons using meta
        
        
1. Dynamic creation of classes
    1. The built-in type() function, when passed one argument, returns the type of an object. For new-style classes
    1. You can also call type() with three arguments—type(<name>, <bases>, <dct>):
        1. <name> specifies the class name. This becomes the __name__ attribute of the class.
        1. <bases> specifies a tuple of the base classes from which the class inherits. This becomes the __bases__ attribute of the class.
        1. <dct> specifies a namespace dictionary containing definitions for the class body. This becomes the __dict__ attribute of the class.
    1. Calling type() in this manner creates a new instance of the type metaclass. In other words, it dynamically creates a new class.

        
1. Garbage collection
    1. module gc

1. Destructors
    1. Like Destructor is counter-part of a Constructor, function __del__ is the counter-part of function __new__. Because __new__ is the function which creates the object.
    1. __del__ method is called for any object when the reference count for that object becomes zero.
    1. As reference counting is performed, hence it is not necessary that for an object __del__ method will be called if it goes out of scope. The destructor method will only be called when the reference count becomes zero.
    1. Exception in __init__ method

### Object Relationships (Passing members of one class to another class)

1. Composition / HAS-A
    1. code reusability
    1. classes is composed of one or more instance of other classes.
    1. weak relation
    
1.  Inheritance/ Aggregation / IS-A
    1. code reusability
    1. Strong relation
    1. Exceptions Are an Exception
    1. Exception class do not derived from object
    1. Types
        1. Single
            1. single parent, single child, A -> B
        1. Multilevel
            1. A -> B -> C
        1. Hierarchical
            1. single parent, multiple child A -> B, A -> C, A -> D
        1. Multiple
            1. Many parent, single child, A, B -> C
        1. Cyclic
            1. class itself is parent and child, A -> B -> A
        1. Hybrid
            1. single, multilevel, hierarchical, multiple
            
    1. MRO (Method resolution order)
        1. It tells Python how to search for inherited methods.
        1. depth first, left to right
        1. mro(), `__mro__`
        1. c3 linearization algorithm
            1. start
            1. mro(X) = X + merge(mro(P1), mro(P2), parent list ie. P1P2)
            1. If head element of first list not present in the tail part of any other list then consider that element in the 
               result
            1. remove that element from all the lists. 
            1. else leave the first list as it is  and consider the next list and repeat
            1. end
            
    1. super(): calls parent of your child unlike any other language in which super calls to the parent
        1. call parent class constructor from child
        1. call parent class methods from child
        1. call parent class variables from child (non instance variables only)
        1. you can call parent instance, class and static methods from child class constructor
        1. you can call parent instance, class and static methods from child class instance method
        1. you can call parent instance, class and static methods from child class classmethod method
        1. you can call parent instance, class and static methods from child class static method
        1. super is always talks about immediate parent
        1. you can call particular class implementation from child class
            1. one way is `className.method_name(self)` (constructor also)
            1. other way is `super(ClassName, self).method_name()`
        1. Technically, super() doesn’t return a method. It returns a proxy object. 
        1. This is an object that delegates calls to the correct class methods without making an additional object.
        1. In Python 3, the super(Square, self) call is equivalent to the parameterless super() call.
        1. A call to the __init__ method of a superclass during object initialization may be omitted:
            1. When a subclass calls the __init__ method of the wrong class.
            1. When a call to the __init__ method of one its base classes is omitted.
            1. When multiple inheritance is used and a class inherits from several base classes, and at least one of those does not use super() in its own __init__ method.
        
    1. Difference between `type` and `isinstance`
        1. type() simply returns the type of an object.
        1. isinstance(): returns true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof.

    
### Polymorphism

1. Duck Typing Philosophy of Python

1. Distinction between Overwriting, Overloading and Overriding

1. Overwriting
    1. Nothing to do with OOP
    1. Simply make first definition unavailable
    
1. Overriding
    1. Constructor overriding
    1. Method Overriding
    
1. Overloading:
    1. Operator Overloading
        1. Supported
        1. Magic methods available
        1. Need to implement these methods
        
    2. Method Overloading
        1. Not possible
        1. If 2 methods having same name but different type of arguments then those methods are said to
            be overloaded methods.
        1. If we are trying to declare multiple methods with same name and different number of arguments
            then Python will always consider only last method.
        1. Handling this req
            1. With default args
            1. With var-args
        
    3. Constructor Overloading
        1. Not possible
        1. If we define multiple constructors then the last constructor will be considered.
    
1. Python magic methods (Object oriented python)
    1. Numeric magic methods

        1. Unary operators and functions
    
            `__pos__(self), __neg__(self), __abs__(self), __invert__(self), __round__(self, n), __floor__(self)
            __ceil__(self), __trunc__(self)`
    
        1. Normal arithmetic operators
    
            `__add__(self, other), __sub__(self, other), __mul__(self, other), __floordiv__(self, other), __div__(self, other)
            __truediv__(self, other), __mod__(self, other), __divmod__(self, other), __pow__, __lshift__(self, other)
            __rshift__(self, other), __and__(self, other), __or__(self, other), __xor__(self, other)`
    
        1. Reflected arithmetic operators
    
            `__radd__(self, other), __rsub__(self, other), __rmul__(self, other), __rfloordiv__(self, other)
            __rdiv__(self, other), __rtruediv__(self, other), __rmod__(self, other), __rdivmod__(self, other)
            __rpow__, __rlshift__(self, other), __rrshift__(self, other), __rand__(self, other)
            __ror__(self, other), __rxor__(self, other)`

    1. Augmented assignment
    
        `__iadd__(self, other), __isub__(self, other), __imul__(self, other), __ifloordiv__(self, other)
        __idiv__(self, other), __itruediv__(self, other), __imod__(self, other), __ipow__, __ilshift__(self, other)
        __irshift__(self, other), __iand__(self, other), __ior__(self, other), __ixor__(self, other)`
    
    1. Type conversion magic methods
    
        `__int__(self), __long__(self), __float__(self), __complex__(self), __oct__(self), __hex__(self)
        __index__(self), __trunc__(self), __coerce__(self, other)`

    1. Representing your Classes.
    
        `__str__(self), __repr__(self), __unicode__(self), __format__(self, formatstr), __hash__(self)
        __nonzero__(self), __dir__(self), __sizeof__(self)`
    
    1. Controlling Attribute Access
    
        `__getattr__(self, name), __setattr__(self, name, value), __delattr__(self, name), __getattribute__(self, name)`
    
    1. Making Custom Sequences
    
        `__len__(self), __getitem__(self, key), __setitem__(self, key, value), __delitem__(self, key), __iter__(self)
        __reversed__(self), __contains__(self, item), __missing__(self, key)`
    
    1. Reflection
    
        `__instancecheck__(self, instance), __subclasscheck__(self, subclass)`
    
    1. Context Managers
    
        `__enter__(self), __exit__(self, exception_type, exception_value, traceback)`
    
    1. Building Descriptor Objects
    
        `__get__(self, instance, owner), __set__(self, instance, value), __delete__(self, instance)`
    
    1. Copying
    
        `__copy__(self), __deepcopy__(self, memodict={})`
    
    1. Pickling your own Objects
    
        `__getinitargs__(self), __getnewargs__(self), __getstate__(self), __setstate__(self, state), __reduce__(self)
        __reduce_ex__(self), __reduce_ex__, __reduce__`

### Abstraction
1. What is abstraction
1. Abstract classes
    1. Abstract class vs Concrete class
1. Abstract methods
    1. @abstractmethod
    1. @abstractstaticmethod -> depricated P3.3
    1. @abstrctclassmethod -> depricated P3.3
1. python implementation
    1. module `abc`
    1. Abstract Base Classes
        1. class ABC
        1. Abstract base classes exist to be inherited, but never instantiated.
        1. You can use leading underscores in your class name to tell that objects of that class should not be created.
    1. Abstract property

1. Interfaces
    1. Informal Interface
        1. Using Metaclasses
        1. Virtual base class
            1. virtual base classes don’t appear in the subclass MRO.
    1. Formal Interfaces
        1. Using abc.ABCMeta
        1. Using .__subclasshook__()
        1. Using abc to Register a Virtual Subclass
        1. Using Subclass Detection With Registration
        1. Using Abstract Method Declaration
1. Difference between Abstract class / Concrete class

### Encapsulation
1. Information hiding
1. We are all adults here
1. protected variables
1. private variables (name mangling)
1. Setter and Getter Methods:
1. Property
    1. getter
    1. setter
    1. deleter

### Descriptor

### Assertions

### Concurrency & Multiprogramming
1. Multithreading
    1. What Is a Thread?
    1. Starting a Thread
    1. Working With Many Threads
    1. Using a ThreadPoolExecutor
    1. Race Conditions
    1. Basic Synchronization Using Lock
    1. Deadlock
    1. Producer-Consumer Threading
    1. Threading Objects
    
2. Multiprocessing
3. Co-routines
4. AsyncIO
    1. `async` & `await`
    1. Async generator
    
---------------------------------------------------------------------------------------------------------------------
### Design patterns
   1. Creational Patterns:
   1. Structural Patterns:
   1. Behavioral Patterns:
   1. Design for Testability Patterns:
   1. Fundamental Patterns:
---------------------------------------------------------------------------------------------------------------------


### Packages
1. Builtin packages
2. User defined packages
3. Use of `__init__`

---------------------------------------------------------------------------------------------------------------------

### Environments
* Whats is envs
* Creating envs
    * Using Pipenv
    * Using virtualenv
* activating and deactivating envs
* Installing packages in envs
* environment variables
    1. PYTHONSTARTUP: 
        - file executed on interactive startup (no default)
        
    1. PYTHONPATH: 
        - ':'-separated list of directories prefixed to the default module search path.  The result is sys.path.
        
    1. PYTHONHOME: 
        - alternate <prefix> directory (or <prefix>:<exec_prefix>).
          The default module search path uses <prefix>/lib/pythonX.X.
          
    1. PYTHONCASEOK: 
        - ignore case in 'import' statements (Windows).
        
    1. PYTHONIOENCODING: 
        - Encoding[:errors] used for stdin/stdout/stderr.
        
    1. PYTHONFAULTHANDLER: 
        - dump the Python traceback on fatal errors.
        
    1. PYTHONHASHSEED: 
        - if this variable is set to 'random', a random value is used
       to seed the hashes of str, bytes and datetime objects.  It can also be
       set to an integer in the range [0,4294967295] to get hash values with a
       predictable seed.
       
    1. PYTHONMALLOC: 
        - set the Python memory allocators and/or install debug hooks
       on Python memory allocators. Use PYTHONMALLOC=debug to install debug
       hooks.
       
    1. PYTHONCOERCECLOCALE: 
        - if this variable is set to 0, it disables the locale
       coercion behavior. Use PYTHONCOERCECLOCALE=warn to request display of
       locale coercion and locale compatibility warnings on stderr.
       
    1. PYTHONBREAKPOINT: 
        - if this variable is set to 0, it disables the default
       debugger. It can be set to the callable of your debugger of choice.
       
    1. PYTHONDEVMODE: 
        - enable the development mode.

---------------------------------------------------------------------------------------------------------------------

### Python project setup
* Code tags
* PEP standards

---------------------------------------------------------------------------------------------------------------------

### Package management
* What is PIP
* easy_install
* Managing packages
* Packaging python apps
* Distributing python apps
* Publishing python apps

---------------------------------------------------------------------------------------------------------------------
