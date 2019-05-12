# Python Cheat Sheet

## Variables

The general form for an assignment statement:

```
variable = expression
```

```python
>>> spam = 42
>>> spam
42
>>> spam = 'Bring a towel.'
>>> spam
'Bring a towel.'
>>> sum = 1 + 1
2

# !! Note that an expression can have a single value because it evaluates to itself. !!
```

## Functions

The general form for a function:

```
def function_name(parameter, parameter):
    body
```

```python
def multi(num):
    return num * 2

def area(base, height)
    return base * height / 2

# !! Note that a function can have multiple parameters. !!
```

A function that does not have a return statement returns `None`.

The execution of a function exits immediately when it encounters a `return` statement. All code after the `return` statement is ignored.

The general form for an function call:

```
function_name(arguments, arguments)
```

```python
>>> multi(2)
4

>>> area(3, 4)
6.0

# !! Note that a function call can have multiple arguments. !!
```

Six steps in function design:

1. **Examples**
    - What should your function do?
    - Type a couple of examples.
    - Pick a name for the function. What is the short answer to "What does your function do"?
2. **Type contract**
    - What are the parameter types?
    - What type of value is returned?
3. **Header**
    - Pick meaningful parameter names.
4. **Description**
    - Mention every parameter in your function.
    - Describe the return value.
5. **Body**
    - Write the code.
6. **Tests**
    - Run the examples from step 1 and try some other tests.

Example of applied function design:

```python
def convert_to_celsius(fahrenheit):
    """(number) -> float

    Return the number of Celsius degrees equivalent to fahrenheit degrees.

    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    """
    
    return (fahrenheit - 32) * 5 / 9
```

## Built-in functions

`print()`

```python
>>> print('Hello', 'there.')
Hello there.
>>> print("You're", 'a', 'bold', 'one.')
You're a bold one.
```

`input()`

```python
>>> input("What's your name? ")
What's your name? Joh Doe
'John Doe'
>>> name = input("What's your name? ")
What's your name? John Doe
>>> name
'John Doe'
```