# Python Cheat Sheet

## Variables

### General form for an assignment statement

Note that an expression can have a single value because it evaluates to itself!

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
>>> 2
2
>>> 'This strings evaluates to itself.'
'This strings evaluates to itself.'
>>>
```

## Boolean operators

### Comparison operators

| Description              | Operator | Example  | Result  |
|:-------------------------|:--------:|:---------|:--------|
| less than                | `<`      | `3 < 4`  | `True`  |
| greater than             | `>`      | `3 > 4`  | `False` |
| equal to                 | `==`     | `3 == 4` | `False` |
| greater than or equal to | `>=`     | `3 >= 4` | `False` |
| less than or equal to    | `<=`     | `3 <= 4` | `True`  |
| not equal to             | `!=`     | `3 != 4` | `True`  |

### `and` operator
The `and` operator evaluates to `True` if both expression evaluate to `True`. If the first expression is `False`, the second expression will not even be evaluated.

| Expression 1 | Expression 2 | Result  |
|:-------------|:-------------|:--------|
| `True`       | `True`       | `True`  |
| `True`       | `False`      | `False` |
| `False`      | `True`       | `False` |
| `False`      | `False`      | `False` |

```python
>>> 80 >= 50 and 70 >= 50    # True and True → True
True
>>> 80 >= 50 and 100 <= 50   # True and False → False
False
>>> 80 <= 50 and 30 == 30    # False and True → False 
False
>>> 10 > 100 and 100 < 10    # False and False → False
False
>>>
```

### `or` operator

The `or` operator evaluates to `True` if at least one expression evaluates to `True`. If the first expression is `True`, the second expression will not be evaluated because the statement as a whole already evaluates to `True`.

| Expression 1 | Expression 2 | Result  |
|:-------------|:-------------|:--------|
| `True`       | `True`       | `True`  |
| `True`       | `False`      | `True`  |
| `False`      | `True`       | `True`  |
| `False`      | `False`      | `False` |

```python
>>> 80 >= 50 or 70 >= 50    # True or True → True
True
>>> 80 >= 50 or 100 <= 50   # True or False → True
True
>>> 80 <= 50 or 30 == 30    # False or True → True
True
>>> 10 > 100 or 100 < 10    # False or False → False
False
>>>
```

### `not` operator

The `not` operator evaluates to `True` if the expression evaluates to `False`.

| Expression 1 | `not` Expression 1 |
|:-------------|:-------------------|
| `True`       | `False`            |
| `False`      | `True`             |

```python
>>> not 80 >= 50    # not True → False
False
>>> not 10 > 100    # not False → True
True
>>>
```

Note that the order of precedence for logical operators is `not`, `and` and `or`!

## Functions

### General form for a function

Note that a function can have multiple parameters!

```
def function_name(parameter):
    body
```

```python
def multi(num):    # One parameter
    return num * 2

def area(base, height)    # Two parameters
    return base * height / 2
```

A function that does not have a return statement returns `None`. The execution of a function exits immediately when it encounters a `return` statement. All code after the `return` statement is ignored.

### General form for an function call

Note that a function call can have multiple arguments!

```
function_name(argument)
```

```python
>>> multi(2)    # One argument
4
>>> area(3, 4)    # Two arguments
6.0
>>>
```

### Six steps for function design

1. **Examples** (lines 6 - 9)
    - What should your function do?
    - Type a couple of examples.
    - Pick a name for the function. What is the short answer to "What does your function do"?
2. **Type contract** (line 2)
    - What are the parameter types?
    - What type of value is returned?
3. **Header** (line 1)
    - Pick meaningful parameter names.
4. **Description** (Line 4)
    - Mention every parameter in your function.
    - Describe the return value.
5. **Body** (Line 12)
    - Write the code.
6. **Tests**
    - Run the examples from step 1 and try some other tests.

```python
def convert_to_celsius(fahrenheit):
    """ (number) -> float

    Return the number of Celsius degrees equivalent to fahrenheit degrees.

    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    """
    
    return (fahrenheit - 32) * 5 / 9
```

## Indexing and Slicing

An index is a position within a string. Each character, including spaces, have an index. Positive indexes start from 0 and read from left to right. Negative indexes start from -1 and start from right to left. Slicing does not change the string because strings are immutable.

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| L   | e   | a   | r   | n   |     | t   | o  |    | p  | r  | o  | g  | r  | a  | m  |
| -16 | -15 | -14 | -13 | -12 | -11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

```python
>>> s = 'Learn to program'
>>> s[0:8]
'Learn to'
>>> s[:8]
'Learn to'
>>> s[9:16]
'program'
>>> s[9:]
'program'
>>> s[9:len(s)]
'program'
>>> s[:]
'Learn to program'
>>>
```

You can also use negative indexes in a slice:

```python
>>> s = 'Learn to program'
>>> s[-16:-8]
'Learn to'
>>> s[-7:]
'program'
>>> s[-7:len(s)]
'program'
>>>
```

Note that while negative indexes start from right to left, the slice is written from left to right! In the example above you can't write `s[-8:-10]` if you want the substring `to`.





