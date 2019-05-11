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