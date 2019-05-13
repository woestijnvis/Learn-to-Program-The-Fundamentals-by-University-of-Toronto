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

## Boolean operators

Comparision operators:

| Description              | Operator | Example  | Result  |
|:-------------------------|:--------:|:---------|:--------|
| less than                | `<`      | `3 < 4`  | `True`  |
| greater than             | `>`      | `3 > 4`  | `False` |
| equal to                 | `==`     | `3 == 4` | `False` |
| greater than or equal to | `>=`     | `3 >= 4` | `False` |
| less than or equal to    | `<=`     | `3 <= 4` | `True`  |
| not equal to             | `!=`     | `3 != 4` | `True`  |

Logical operators:

| Description | Operator | Example                     | Result  |
|:------------|:--------:|:----------------------------|:--------|
| not         | `not`    | `not (80 >= 50)`            | `False` |
| and         | `and`    | `(80 >= 50) and (70 <= 50)` | `False` |
| or          | `or`     | `(80 >= 50) or (70 <= 50)`  | `True`  |

The `and` operator evaluates to `True` if both expression evaluate to `True`. If the first expression is `False`, the second expression will not even be checked:

| Expression 1 | Expression 2 | Results |
|:-------------|:-------------|:-------:|
| `True`       | `True`       | `True`  |
| `True`       | `False`      | `False` |
| `False`      | `True`       | `False` |
| `False`      | `False`      | `False` |

The `or` operator evaluates to `True` if at least one expression evaluates to `True`. If the first expression is `True`, the second expression will not be checked because the statement as a whole already evaluates to `True`:

| Expression 1 | Expression 2 | Results |
|:-------------|:-------------|:-------:|
| `True`       | `True`       | `True`  |
| `True`       | `False`      | `True`  |
| `False`      | `True`       | `True`  |
| `False`      | `False`      | `False` |

The `not` operator evaluates to `True` if the expression evaluates to `False`:

| Expression 1 | `not` Expression 1 |
|:-------------|:-------------------|
| `True`       | `False`            |
| `False`      | `True`             |

The order of precedence for logical operators is `not`, `and` and `or`.