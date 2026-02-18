Post course feedback link https://firebrand.training/uk/feedback?cscode=app-PYTHONF


# PYTHONF-Challenges

## Lab 01A
### Calculating Pay

Jemima takes a job making widgets.  She is paid 50p for each widget she makes.

Write a program to calculate her pay for making 30 widgets, 40 widgets and 50 widgets.

You should use variables here.  It will make later parts of this challenge **much** easier.  Start with somthing like:

```
rate_per_widget = 0.50
quantity_made = 30

### Calculate the pay here

print(pay)

quantity_made = 40

### Repeat the calculation here.  Yes there is a better way than copy/paste but we have not taught it yet

print(pay)

### Repeat for the 50 quantity
```


Manually calculate the expected values and test that the program produces the results you expect

Extend that program so that for each widget after 35 Jemima is paid at a 50% higher rate per widget. You will have to do a little research on the `if` statement for this.  As of Day 1 we have not properly covered the `if` statement.  Don't worry if you have trouble with it we will
cover the `if` statement properly later on

Test it as above

Extend your code again so that after Jemima produces 45 widgets she gets a 10% bonus on her entire pay

Test it as above


## Working with string methods...

Set up a string with mixed case text in it, a string that's all upper case, and a string that's all lower case.

In the python docs look up the `string` methods. 

Experiment with `isupper()`, `islower()` do they correctly report your strings?

Experiment with `lower()` and `upper()`.

These are often useful with user input.  For example, if we get the user to answer a question y for yes n for no.
We cannot predict whether they will type the letters in lowercase or uppercase. A common programming technique is to convert what they enter into either all uppercase or all lowercase. This makes it easier for us to write conditions. Something like...

```
answer = input("Should I format your hard disk? (y/n)")
if answer.upper() == 'Y'
	print('Formatting...')
	# Code to format HDD goes here
else
	print('I am sad - I really wanted to format your disk!')
```

Experiment with that code.  Expand it to accept the full words (yes/no) as the response






## Lab02A

### Mutating a list...

Create a list containing the values 10, 20, 30, 40

Print the list.  Notice that the default print output shows the square brackets, to identify the output as a list 

Mutate the list by adding these values, one at a time **in the order specified**.  Print the state of the list after each modification.  Carefully consider using `.append` or `.insert` so that at the end the list is left in ascending numerical order (**without** using `sort`).

`.insert(index, value)` will add `value` at position `index` in the list.

45
46
44
43
15
25

Print all the even subscript items (Ie [0], [2] [4] etc)

Print all the odd subscript items

Print the list in reverse order

Overwrite the first element in the list with the value 5

## Lab 02B

Create a tuple containing the values 10, 20, 30, 40

Print your tuple.  Notice that the default print output shows the parentheses, to identify the output as a tuple 

Attempt to overwrite the first element in the tuple.  Discover that Python
will not allow it

## Lab 02C 

Some questions about sets.  You should try to solve them in your head first. THEN try coding them to see if you predicted the correct anwer and to test your code against your prediction

- **Question - 1**:

What is the output of the following code?

<code>a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]</code><br>
<code>b = set(a)</code><br>
<code>print(len(a) - len(b))</code>

Choices:
    
        1. 10
        2. 4
        3. Error
        4. 6

- **Question - 2**:

Given two lists:

<code>list1 = [1, 2, 3, 4, 5, 6]</code><br>
<code>list2 = [4, 5, 6, 7, 8]</code>

Find the missing and additional values in both the lists.

To do this convert the lists to sets. Check out the documentation for `set` operations like `intersection` and `difference`.  You should be able to get the results with just a couple of lines of code.

- **Question - 3**:

Given 3 lists:

<code>ls1 = [1, 5, 10, 20, 40, 80]</code><br>
<code>ls2 = [6, 7, 20, 80, 100]</code><br>
<code>ls3 = [3, 4, 15, 20, 30, 70, 80, 120]</code>

Use sets to find the common elements in the above lists.  (It can be done in one line of code.)


## Lab 2D

- **Question - 1**:

Create a dictionary that contains the following key-value pairs:
        
        1. Shanghai, 17.8
        2. Istanbul, 13.3
        3. Karachi, 13.0
        4. Mumbai, 12.5
        
Print the dictionary.  Note that the print statement formats the output in curly braces and wth key : value pairs.

 - **Question - 2**:
 
 Which of the following can be used as keys for a dictionary?
 
 Choices:
    
        1. string
        2. integer
        3. float
        4. lists
        5. All of above

Why did you give that answer?
        
 - **Question - 3**:
 
 Given two lists:
 
 <code>keys = ['key1', 'key2', 'key3']</code><br>
 <code>values = [1, 2, 3]</code><br>
 
Convert these lists into a dictionary such that the `keys` list entries become the keys in the dictionary and the `values` list entries become the values in the same dictionary. To do this you need to pair together the first item in keys, with the first item in values, then the second items etc.  The `zip` function does exactly that.

- **Question - 4**:

Given the two dictionaries below:

<code> dict_1 = {'key1': 1, 'key2': 2, 'key3': 3}</code><br>
<code> dict_2 = {'key4': 4, 'key5': 5, 'key6': 6}</code><br>

Merge these dictionaries into a single dictionary. HINT - research the dictionary `update` method

Here the keys are unique over both dictionaries.  Experiment to show what happens if both dictionaries contain the same key?

- **Question - 5**:

<code>dictionary = {"class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}}</code></br>

Print the value for the key 'history'.

## Lab 03A

- **Question - 1**: 

Create an if-else statement to determine if a number is even or odd. 

Prompt for input and apply the even/odd check to that input. Print the number along with a message stating that the number is odd or even.

- **Question - 2**: 

Extend your code.  Add an initial check to see if the entered number is zero.  If zero print a suitable message

- **Question - 3**:

Check if a number is composed of a single digit, two digits, or three digits.  Print an appropriate message

- **Question - 4**:

Prompt the user to input a character. Write conditional statements to check if the given character is upper case, lower case, a digit, a vowel, or a special character.  Print a descriptive message.

Note: The categories overlap.  An upper case character might be a vowel as well.

- **Question - 5**:

Prompt the user for a year as an integer. Check if the year is a leap year using if-else statements.

Do some research to come up with the logic of how you can check for a leap year.  Just a multiple of 4 is not good enough

## Lab 03B

- **Question - 1**:

Consider the following list:

<code>ls=["Phil", "Oz", "Seuss", "Dre"]</code>

Use a for loop to create a new list, with the title 'Dr.' before each name.


- **Question - 2**:

You are given a list below:

<code>ls_1=[111, 32, -9, -45, -17, 9, 85, -10]</code>

Derive a new list from `ls_1` containing only the positive numbers

Note: You will need to include a conditional statement inside a loop

- **Question - 3**:

For this question, use the dictionary given below:

<code>dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}</code>

Derive a list from the dictionary.  The list should contain values from the dictionary that are over 1000.  Before adding an entry into the new list, subtract 500



## Lab 03C

- **Question - 1**:

Write a for loop, from 0 to 100, with a `break` statement so that it prints from 0 to 9 only (including 9)

Add an `else` clause to the `for` that just prints a message.  Try removing the `break` statement to show that the `else` is only executed for 'un-broken' for loops

- **Question - 2**:

Write a while loop that sums all the numbers up to 20 (inclusive).


- **Question - 3**:

Use this list of numbers:

<code>lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]</code>

Iterate through the list elements and if you find the value '100', print it with its index / position in the list.

Note: Having to print the index makes this trickier than a simple `for` loop

- **Question - 4**:

Write a program that repeatedly prompts the user to enter a number.  When the user enters zero the program should print the sum of all the numbers entered.


- **Question - 5**:

Loops go hand-in-hand with sequence type collections...

Working with the code challenge from day 1 (Jemima's pay calculation), set up a list, named `quantities` to contain the quantities of widgets Jemima makes - 30, 40, and 50

Paste in this code to iterate through those values...

```
for quantity_made in quantities:
	# Indented code establishes the loop body
	print(quantity_made)

## un-indented code does not belong to the loop
print('Loop ended')
```

The loop will set the variable `quantity_made` one by one to the members of the list.  Inside the body of the loop it prints that value.  Run it to make sure
it displays the three quantity values

Copy/paste ONE copy of the pay calculation code into the loop body.  It must be indented to become the loop body.  Here is the original code for that...
```
rate_per_widget = 0.50
quantity_made = 50

pay = 0.50 * quantity_made
higher_rate_pay = 0
if quantity_made > 35:
    higher_rate_pay = (quantity_made - 35) * 0.50 * 0.50
    print('higher rate', higher_rate_pay)

pay = pay + higher_rate_pay

print('before bonus', pay)
if quantity_made > 45:
    pay = pay * 1.10

print('The pay for 50 is', pay)

```

REMOVE the assignment to `quantity_made` inside the loop body.  The loop header already does that.

ADJUST the final print statement so that it uses the `quantity_made` variable instead of the hard coded 50

Test to see that the loop produces the same results as the original repeated code

Add some more test values to the list.

**Question** Which are the best test values?  Why?


- **Question - 6**:

We have been given a specification change for the payroll calculation.
For those who produce more than 45 units, there are three possible bonus values; 10% 15% and 20%.  As we calculate pay we are to print all three possible final pay values.
Use a nested loop to implement this.


## Lab 04A

- **Question 1**

Write a function named `Add` to take in two numbers and return their sum

Write some print function calls to test the `Add` function.  Like

```
print("2 plus 2 =", Add(2,2))
print("9 plus -3 =", Add(9, -3))
```

- **Question 2**

### Refactoring

Refactoring is a general word for changing (to improve!) the design of a piece of code whilst preserving what it does.

Go back to your code for Jemima's payment calculation

Extract the payment calculation into a function.  Your function should take in rate_per_widget and quantity_made.  It should return the calculated pay.  (Use the version WITHOUT the nested loop of three special bonuses.)

Write a few `print()` function calls to test it

### Bonus steps

Make your function more flexible. Take in the threshold for enhanced pay (35) as another parameter.  Set this parameter to default to 35 if unspecified.  So your existing test code does not require change.

Get this working first.  THEN try it with a specified value for the enhanced payment

Similarly take in the second enhanced payment threshold (45) as a parameter, also give this one a default value

- **Question 3**

Write a function named `powers`.  Have it accept a single number.

Make it return a `tuple` where [0] is the original passed in number, [1] is the square, [2] is the cube, [3] is the fourth power.

Again test it by calling it from a few `print` functions.  Eg:

```
print(powers(2))
print(powers(3))
```


## Lab 04B

Add a doc string to your powers function.  To do this add a multiline literal as the first thing after the `def` statement.  (Indented so that it belongs to the function)

Hint:
```
def powers():
	'''
	The powers function is....
	'''
```

Now start a command prompt and navigate to the directory containing your powers function file.

Run the command...

`python -m pydoc <name of the file with your powers function>`

See that the pydoc system extracts the content of your doc string.  Doc strings are a general idea and can be used for files, functions, classes, etc in a python application.

Add a couple more functions, with doc strings, to the file and try generating the pydoc output again

This is a just a taste of what the pydoc system is capable of.




## Lab 04C

- **Question - 1: Raise an Exception**

Create a small function that expects a single parameter value between 0 to 100, if the value received by the function is outside the specified range, `raise` a `ValueError` exception.  The function should NOT handle this error internally.  It doesn't need to do anything with the incoming parameter other than check its range

Write code to call the function with a value inside the range and a value outside the range.  Notice that the value outside the range causes the program to crash.

Place your calling code inside a `try` block.  Add an `except` block to handle the `ValueError` exception by printing a polite message.

Test that the exception path is only triggered by a value outside the range 0, 100.

## Lab 05A

1. Create a module
    - A file named `functions.py`
    - add a print call like
        `print("Hello from functions.py")`
    - add a function named `square` that takes a number and returns the square

1. Create another file
    - named `caller.py`
    - add an import for the module `functions`. Eg...
    `import functions` note there is no .py
    - add a line
        `print("about to call square")`
    - call the `square` function in the functions module using the fully qualified name...
    `fourSquared = functions.square(4)`
    `print(fourSquared)`

1. Run and test
    - note that when the module is imported all 'unenclosed code' (code not in a function) is executed hence the `Hello` message is seen when the import is executed
    - It's a bad practice to have unenclosed code in a module that gives an intrusive effect.  Ie don't print anything!

### Bonus Ideas
1. Extend the module with a function, `tupleExtender` that expects a tuple and a newItem as parameters.  It appends `newItem`to the tuple and then returns it. Tuples are immutable so you have to
    - convert the tuple to a list
    - append to the list
    - convert the list back to a new tuple
    - return the new tuple

1. Add a call to `tupleExtender` to test it

1. Experiment with importing the module using an alias
    - `import functions as fns`
	- discover that you have to use `fns` as the qualifier

1. Experiment with importing an individual function into the current namespace
    - `from functions import square`
    - discover that now it's callable without qualification
    - `sq = square(4)`


## Lab 05B


1. Write a program to read a text file (just hard code a file name) and display the contents using `print()`

    - Create some test data.  Suggestion... some imaginary, 5 digit, employee numbers

    - Test your program

1. Try the code both the old way - just calling `open` then `close`.  

	Also try the more modern way using `with`

	Something like `with open(<file path> "r") as <file object reference>` which makes the close automatic

1. Enhance your program so that it reads the input file.  But only displays an employee number on the first occasion it appears in the file

    - Suggestion, check each incoming employee number in a `set`.  
    - If it is NOT present in the `set`, `print` it and add it to the `set`.

1. Enhance your program to both print the output and write it to a new file (hard code the file name)

## Bonus ideas

1. Do a bit of research to find out how to access command line arguments
    - Allow the file names to be supplied at the command line.
    - For this you should run the program from a command prompt window.
    - On our VM's python is installed in a subdirectory `anaconda3`.  So from the standard `LabUser` directory you would run somthing like...
`.\anaconda3\python yourprogram.py inputFile outputFile`

1. Do a bit more research and give the user a warning if they are about to overwrite an existing file

Hint - check out the docs for `os.path.exists()`

# Module 6

## Lab 06A

### Triangle class

1. Create a class to represent a triangle.  Store just the three sides of the triangle.  DON'T attempt to store angles as well

    Your constructor should check for an invalid triangle:
    - negative side length
    - any pair of sides adding up to less than the length of the third side
    - the right thing to do for an invalid triangle would be to throw an exception.  If you don't know how to do that then just print a message

1. Add a member function `get_perimeter(self)` to calculate the perimeter of the triangle.

1. Write some test code to show that you can create triangles and compute their perimeters

1. Print out the detail of a triangle, (all three sides and perimeter).  Don't add a member function for this, write lines like:
    - print(triangle1.side1)
    - print(triangle1.get_perimeter())

1. Notice this is inconsistent syntax. To retrieve the perimeter requires very different syntax (`get_perimeter(self)`)

1. Add a property definition for perimeter to the class
    `perimeter = property(get_perimeter)`
(notice that you MUST NOT have parentheses (like `()`) after get_perimeter)
1. Now find that you can access the attribute `perimeter` of the class *as if* it were simple read only data.  The property automates calling the `get_perimeter` function, and returning its result

### Bonus Ideas

1. Add a colour attribute, as a string, to the Triangle class.  In the constructor default it to "Black"
1. Print the triangle colour as well as the side lengths
1. Notice that you can set the colour to any random value by simple assignment
    `t1.colour = "Dog"`
    obviously dog is not a valid colour value

#### Make colour a property
1. Change the name `colour` to `_colour` thoughout the class.  It is a python convention that leading underscore variables are considered `private` and programmers using the class should NOT touch them.  It is just a convention, the language does not enforce it.
Add a `get_colour(self)` function and a `set_colour(self, newColour)` function to your class
Add a property for `colour` like this...
    `colour = property(get_colour, set_colour)`
Retest your code.  Discover that you can still set `colour` (NOT `_colour` you should not touch that) to silly values
1. In the `set_colour` function add protection code so that it will ONLY accept the colour values "Red", "Blue" "Green".  Again the right thing to do for an invalid value would be to throw an exception.  If you don't know how to do that just print a message.
1. Discover that assignments to `colour` are now validated by the logic in `set_colour`

## Lab 06B

### Shape class

1. Continue working in your `Triangle` class file

1. Add a class `Shape`

1. Have it store a position (Just pass and store an x co-ordinate and a y co-ordinate in the constructor)

1. Now make `Triangle` inherit from `Shape`.  It looks like this
    `class Triangle(Shape)`
    ...this means that `Triangle` is to have all the attributes of `Shape`...

1. To enforce that, when we create a `Triangle` we should supply an x and a y coordinate.  Extend `Triangle.__init__` to accept an x and a y parameter.
1. Pass those values up to the `Shape` class constructor using the built in `super()` function.  Like this...
    `super().__init__(x, y)`
    notice that this automatically passes the `self` object
1. Retest your code.  Notice that creating a `Triangle` now requires an x and y co-ordinate


### Bonus ideas...

### Demonstrate polymorphism

1. Create a `Rectangle` class that also inherits from `Shape`.  Have `Rectangle` store a width and a height
1. Don't forget that the `Rectangle` constructor should have an x and a y co-ordinate parameters.  It should also pass them up to `Shape` using the `super()` function (just like `Triangle`)
1. Give `Rectangle` a read only `perimeter` property.  Hint - to make it read only; create just a `get_Perimeter(self)` method, (ie omit coding a setter) 
1. Test this by creating a list with a `Triangle` and a `Rectangle`.  Iterate over the list and access the `perimeter` property for both objects.  Your code might look like this (A hint in case you don't know how to create a list and iterate over it)...
```
shapes = [ Triangle(2,2,3, 100, 110), Square(10,10, 110, 120) ]
for shape in shapes:
    print(shape.perimeter)

```

## Lab 06C

## Flush printing text

Newspapers and magazines often print lines such that the first character aligns on the left margin and the last character aligns on the right margin.  With a fixed pitch font this is done by adding extra spaces between the words to push the rightmost character to the correct position.

Clearly it looks silly to put (say) five spaces before the last word.  The (say) five spaces should be distributed, evenly as possible, into the gaps between the words on the line.  The process is a little more complex with variable pitch fonts, but the idea is the same

The lab doesn't implement the entire functionality, just a couple of useful parts. You can complete it later if you like!

1. Paste this code into a new file to make the test framework

    ```Python
    import unittest

    def add(a, b):
        return a + b

    class TestAddFunction(unittest.TestCase):
        def test_add_positive_numbers(self):
            self.assertEqual(add(1, 2), 3)

        def test_add_negative_numbers(self):
            self.assertEqual(add(-1, -2), -3)

        def test_add_mixed_numbers(self):
            self.assertEqual(add(1, -2), -1)
            self.assertEqual(add(-1, 2), 1)

    if __name__ == '__main__':
        unittest.main()
    ```

1. The short description of how it works...
    - the `if __name__ == '__main__':` is a handy Python trick.  It is un-enclosed code so it runs if the module is executed stand alone, it is also executed if the module is imported.  It relies on Python behaviour that when a module runs stand-alone the special variable `__name__` is set to the magic value `'__main__'`.  Therefore this is a condition that determines if the module is being run stand alone
    - If it **is** being run stand alone then we call the main function in the testing package
    - The testing package's `main` function then finds classes that inherit from `unittest.TestCase` and executes all those member functions with names beginning with `test_`

    - When imported to another module then the condition skips executing any of the tests

    - This trick is handy as it allows the tests to stay with the implementation code. They are more likley to be kept up to date and less likely to be lost

1. Start off by adding a test for a function that takes a string, (the text for the line), and an integer, (the intended length of the line).  
    - this function should return BOTH the words, as a list, and the number of spaces to fill the line to the desired length. Simplest is to return a tuple `return (wordsList, requiredSpaces)`.  The caller can then sequence unpack that result `words, spaces = f(...)`
    - assert that the list of words contains the expected words
    - assert that the calculated number of spaces is correct
    - Of course real life lines are maybe 80 characters long and have maybe ten plus words.  You should keep it simple, maybe three words.  Pick your own line length but it needs to be large enough for the words and the spaces...  Follow the pattern of the existing tests. Maybe
    ```Python
        def test_lineDecomposition(self):
            words, spaces = split_line_to_words_and_spaces("the..   boy", 12)
            self.assertEqual(words, ["the..",  "boy"])
            self.assertEqual(spaces, 4)
    ```

1. Run your file.  You expect it to crash because you have no function yet

1. Write the header line for your line splitting function, and implement it's functionality.  Keep running the tests until they pass

1. Once those tests pass for your split function...

1. Write a test for a function that takes a list of words, and a number (the number of spaces required to separate the words of the line AND pad it to the required length).  
    - You will notice that this is exactly what the previous function emits, but you should TEST THIS ONE INDEPENDANTLY
    - Your test might look like this
    ```Python
   
        def test_distributeExcessSpacesAtEndOfLine(self):
            line = distribute_spaces_at_end(["the..", "boy", "stood", "on"], 4)
            self.assertEqual(line, "the.. boy stood  on")
    ```
    - notice that there are three words, but a demand for four spaces.  That is why in the assertion there are TWO spaces between 'stood' and 'on' 

    - Now write the code to make this pass.

1. Add more cases, some ideas...
    - a line with one word
    - a five word line with, say, seven spaces required.  You decide what should happen.  As a suggestion, distribute excess spaces into the gaps working from the end of the line towards the front.  Write the test, then make it pass
