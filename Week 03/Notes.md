# Part 1: Built-in types

## Type `bool`

Python has two Boolean operators: `True` and `False`. That statement evaluates to `False`, so does python really have two Boolean operators?

Comparison operators evaluate to a Boolean value:

| Description              | Operator | Example  | Result  |
|:-------------------------|:--------:|:---------|:--------|
| less than                | `<`      | `3 < 4`  | `True`  |
| greater than             | `>`      | `3 > 4`  | `False` |
| equal to                 | `==`     | `3 == 4` | `False` |
| greater than or equal to | `>=`     | `3 >= 4` | `False` |
| less than or equal to    | `<=`     | `3 <= 4` | `True`  |
| not equal to             | `!=`     | `3 != 4` | `True`  |

There are three logical operators that produce a Boolean value: `and`, `or` and `not`:

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

The order of precedence for logical operators is `not`, `and` and `or`. This can be overridden with parenthesis. Take the following example:

```python
>>> grade = 80
>>> grade2 = 90
>>> not grade >= 50 or grade2 >= 50
True
```

To visualize the flow of the example above:

```
not grade >= 50 or grade2 >= 50
↓
not True or True
↓
False or True
↓
True
```

If we add parenthesis to the expressions, we can make sure the outcome evaluates to `False`. The expressions between the parenthesis are evaluated first. That produces the Boolean `True`, but then `not` peeks around the corner and makes sure the statement evaluates to `False`:

```python
>>> grade = 80
>>> grade2 = 90
>>> not (grade >= 50 or grade2 >= 50)
False
```

To visualize the flow of this example:

```
not (grade >= 50 or grade2 >= 50)
↓
not (True or True)
↓
not True
↓
False
```

## Converting Between `int`, `str`, and `float`

The `str()` function takes a any number and turns it into a string. Example:

```python
>>> str(3)
'3'
>>> str(47.6)
'47.6'
>>>
```

The `int()` function take a string and turns it into a type integer. This works if the string only contains numbers. It can also turn floats to integers. Example:

```python
>>> int('12345')
12345
>>> int('-998')
-998
>>> int(-99.9)
-99
>>> int('99.9')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '99.9'
>>>
```

Note that `int()` function only works on digits. If the string contains a decimal it wil not work. We have the `float()` function for that. I also take an integer and turns it into a float. Example:

```python
>>> float('99.9')
99.9
>>> float('432')
432.0
>>> float(4)
4.0
>>>
```

## Import: Using Non-Built-in Functions

Not all functions are built-in and if you want to use a certain function, you need to import it. A module is a file with function definitions and other statements. You can import the module and then use the functions. You can of course create your own module. A module that gets imported should be in the same directory as the file that is importing it.

The general form for a an import statement is:

> `import module_name`

To use a function from a module:

> `module_name.function_name`

Example:

```python
import math

def area2(side1, side2, side3):
    semi = semiperimeter(side1, side2, side3)
    area = math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))
    return area
```

# Part 2: If statements

## If Statements

## No if Required

## Structuring if Statements