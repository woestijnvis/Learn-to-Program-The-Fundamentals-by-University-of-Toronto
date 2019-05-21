# Part 1: `while` Loops

## `while` Loops

The general form for a `while` statement:

```
while expression:
    statements
```

Example:

```python
number = 2

while number < 100:
    number = number * 2
    print(number)
```

Output:

```
4
8
16
32
64
128
```

In the example above, the loop keeps looping if the statement `while number < 100` evaluates to `True`. While it loops, it takes the variable `number` and multiplies that with `2`. After multiplication, that value is assigned to `number` and then the value of `number` gets printed. This loop stops when `number` is greater than `100`.

Another word for looping is iterations.

Problem: Print the characters of a string up to the first vowel.

```python
>>> i = 0
>>> s = 'xyz'
>>> while not (s[i] in 'aeiouAEIOU'):
        print(s[i])
        i = i + i
x
y
z
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

This solution works until there are no more character left in the string. We can check for that with another statement:

```python
>>> i = 0
>>> s = 'xyz'
>>> while i < len(s) and (not s[i] in 'aeiouAEIOU'):
        print(s[i])
        i = i + i
x
y
z
```

Python is lazy when it comes to checking. If the first statement (`i < len(s)`) is `False`, the second statement (`(not s[i] in 'aeiouAEIOU')`) will not be checked. This prevents an IndexError.

# Part 2: Comments

## Comments

Comment start with a `#` for single line and `""" comment """` for multiple lines. Remember to explain what it does and not how it works. The code show how it works.

# Part 3: Lists, list methods and mutating lists

## Type list

The general form for a list:

```
[expression_1, expression_2, expression_3]
```

There are several list operations: index, slice, `len()`, `min()`, `max()`, `sum()` and the `in` operator. Example:

```python
>>> grades = [80, 90, 70]
>>> grades[0]
80
>>> grades[1]
90
>>> grades[2]
70
>>> grades[1:2]
[90]
>>> grades[0:2]
[80, 90]
>>> 80 in grades
True
>>> 60 in grades
False
>>> len(grades)
3
>>> min(grades)
70
>>> max(grades)
90
>>> sum(grades)
240
>>>
```

Most of the previous examples also work with string:

```python
>>> subjects = ['bio', 'cs', 'math', 'history']
>>> subjects[0]
'bio'
>>> subjects[1]
'cs'
>>> subjects[2]
'math'
>>> subjects[1:2]
['cs']
>>> subjects[0:2]
['bio', 'cs']
>>> 'bio' in subjects
True
>>> 60 in subjects
False
>>> len(subjects)
4
>>> min(subjects)
'bio'
>>> max(subjects)
'math'
>>>
```

Lists may have different data types:

```python
>>> address = ['B', 'Nieuwelaan', 112, 'Amsterdam', 'AB', 1247]
>>> dutch_address = '{} {} {}, {} {} {}'.format(address[1], address[2], address[0], address[5], address[4], address[3])
>>> dutch_address
'Nieuwelaan 112 B, 1247 AB Amsterdam'
>>>
```

The general form for a `for` loop over a list:

```
for variable in list:
    body
```

Example:

```python
>>> grades = [80, 90, 70]
>>> for grade in grades:
        print(grade)
80
90
70
>>> subjects = ['bio', 'cs', 'math', 'history']
>>> for subject in subjects:
        print(subject)
bio
cs
math
history
>>>
```

Note that an expression using slice notation (a colon in the square brackets) will evaluate to a list. This may be a list with a single element, which is different from that element itself. Example:

```python
>>> temp = [18, 20, 22.5, 24]
>>> temp[-1]
24
>>> temp[3:]
[24]
>>>
```

## List methods

Remember that a method is a function inside an object. For the methods in list, check what `dir(list)` outputs in python shell. This part of the course is about modifying lists and getting information from lists.

Modifying lists:

 - `list.append(object)`
 - `list.extend(list)`
 - `list.pop([index])`
 - `list.remove(object)`
 - `list.reverse()`
 - `list.sort()`
 - `list.insert(int, object)`

Getting information from lists:

- `list.count(object)`
- `list.index(object)`

Example:

```python
>>> colors = []
>>> prompt = 'Enter your favorite colors: '
>>> color = input(prompt)
Enter your favorite colors: blue
>>> color
'blue'
>>> colors
[]
>>> while color != '':
        colors.append(color)
        color = input(prompt)

Enter your favorite colors: yellow
Enter your favorite colors: brown
Enter your favorite colors: # Hit enter to exit prompt.
>>> colors
['blue', 'yellow', 'brown']
>>> colors.extend(['hot pink', 'neon green']) # Values need to be in a list!
>>> colors
['blue', 'yellow', 'brown', 'hot pink', 'neon green']
>>> colors.pop() # Using this method also returns the removed value.
'neon green'
>>> colors
['blue', 'yellow', 'brown', 'hot pink']
>>> colors.pop(2)
'brown'
>>> colors
['blue', 'yellow', 'hot pink']
>>> colors.remove('black') # Error because object is not in list.
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> if colors.count('yellow') > 0: # If 'yellow' in colors, remove it.
        colors.remove('yellow')

>>> colors
['blue', 'hot pink']
>>> if 'yellow' in colors: # This is waaay cleaner than the code above.
        colors.remove('yellow')

>>> colors.extend(['auburn', 'taupe', 'magenta']) # Make sure it's in a list!
>>> colors
['blue', 'hot pink', 'auburn', 'taupe', 'magenta']
>>> colors.sort()
>>> colors
['auburn', 'blue', 'hot pink', 'magenta', 'taupe']
>>> colors.reverse()
>>> colors
['taupe', 'magenta', 'hot pink', 'blue', 'auburn']
>>> colors.insert(-2, 'brown') # Shifts excisting values over.
>>> colors
['taupe', 'magenta', 'hot pink', 'brown', 'blue', 'auburn']
>>> if 'hot pink' in colors:
        where = colors.index('hot pink')
        colors.pop(where)

'hot pink'
>>> ['taupe', 'magenta', 'brown', 'blue', 'auburn']
>>> 
```

> A function or method has a side effect if it returns a value and also modifies an object.

Check the docs for list methods.

## Mutability and Aliasing

## `range`