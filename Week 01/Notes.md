# Part 2: Getting Started

## Python and Computer Memory

Think of computer memory as a long list of storage locations. Each location has a unique number called the memory address. We write that number with an x as prefix to differentiate it from other numbers. So, x201, x202 and x203 all refer to a unique memory address. Or you can prefix the number with id (id201, id202, id203).

Programs need a way to keep track of memory addresses and it uses variables for that.

> A variable is a named location in computer memory. 

Python keeps track of variables in a separate area of memory. A variable contains a memory address and that memory address contains a value.

```python
>>> shoe_size = 44
```

The variable `shoe_size` contains memory address x34 and x34 contains the value `44`. In one line:

> variable → memory address → value

Terminology:

- A value has a memory address
- A variable contains a memory address
- A variable refers/points to a value

Examples of terminology:

- Value `44` has memory address x34
- Variable `shoe_size` contains memory address x34
- The value of `shoe_size` is `44`
- `shoe_size` refers/points to value `44`

# Part 3: Variables and Functions

## Variables

The general form of an assignment statement:

> `variable = expression`.

Example:

```python
>>> base = 20
>>> height = 12
>>> area = base * height / 2
>>> area
120.0
>>>
```

The rules for executing an assignment statement:

1. Evaluate the expression on the right side of the = sign. This produces a value. That value has a memory address.
2. Store that memory address in the variable on the left side of the = sign.

The rules for naming variables in python:

1. Variable names must start with a letter of an _ (underscore).
2. Variable names can only contain letters, digits and the _ (underscore).
3. Capitalization matters.
4. The convention is to use `pothole_case` and lowercase letters.

## Visualizing Assignment Statements

Bookmark this tool: [Python Visualizer](http://pythontutor.com/visualize.html#mode=edit) and learn how to use it.

## Built-in Functions

Let's define what an argument is first:

> An argument is an expression that appears between the parenthesis of a function call.

The general form of an function call:

> `function_name(arguments)`

Example:

```python
>>> max(36.7, 500)
500
>>> round(4.7)
5
>>>
```

The rules for executing a function call:

1. Evaluate each argument one at a time, from left to right.
2. Call the function by its name and pass the arguments between the parenthesis.

Terminology:

- Argument: a value given to a function to do something with (a function can receive more then one argument!).
- Pass: to provide to a function.
- Call: ask python to evaluate a function.
- Return: pass back a value.

In the previous example, `max(argument, argument)` and `round(argument)`, are built-in functions. There is also a help function that can give you more information about a built-in function. Example for the function `max()`:

```python
max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value

    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.
```

To show all built-in functions, run:

```python
>>> dir(__builtins__)
```

## Defining Functions

The general form for a function is:

```python
def function_name(parameter):
    body
```

Rules for defining a function definition are:

1. Functions start with the word `def`,
2. Then comes the `function_name`,
3. Followed by `()` (parenthesis) and the `argument(s)` between them,
4. And then a colon.
5. After that comes the `body` (code and comments).

Functions often end with the return statement and pass back a value to the caller.

Example:

```python
>>> def multi(num):
        return num * 2
>>> multi(2)
4
>>>
```

In the above example, we call the definition `multi` and the argument provided is the value `2`. The definition returns the value of the expression `2 * 2`, in this case `4`. `num` gets assigned a value of `2` and is therefor a variable. 

> Function calls are often expressions.

You can assign the return of a function to a variable:

```python
>>> def multi(num):
        return num * 2
>>> result = multi(2)
>>> result
4
>>>
```

Rules for execution a function call:

1. Evaluate the arguments to produce memory addresses.
2. Store those memory addresses in the corresponding parameters.
3. Execute the body of the function.

Take this example and the explanation below it:

```python
>>> def area(base, height):
        return base * height / 2
>>> area(3, 4)
6.0
>>>
```

This function calculates the area of a triangle. The function needs two arguments: `base` and `height`. The arguments for `base` and `height` are `3` and `4`. Even a single value like the int `3` or `4` evaluates to itself. That means that the expression for `base` is `3` and `height` get the expression `4`. Those expressions are stored in a memory address and the parameters for `base` and `height` contain the corresponding memory address. After the call, the body of code runs and produces the expression `6.0`. This value gets returned.