# Part 1: Fancy string processing

## More `str` Operators

You can concatenate strings with the `+` operator and multiple strings with the `*` operator. Let's see other operators at work with strings:

The equality and inequality operators:

```python
>>> 'a' == 'a'
True
>>> 'ant' == 'ace'
False
>>> 'a' == 'b'
False
>>> 'a' != 'b'
True
>>>
```

We can compare two strings for their dictionary order. Remember that capitalization matters and that lowercase letters are greater than capital letters:

```python
>>> 'abracadabra' < 'ace'
True
>>> 'abracadabra' > 'ace'
False
>>> 'a' <= 'a'
True
>>> 'A' < 'B'
True
>>> 'a' != 'A'
True
>>> 'a' < 'A'
False
>>>
```

The `in` operator checks if a strings appears in another string, this is called substringing. Example:

```python
>>> 'c' in 'aeiou'
False
>>> 'cad' in 'abracadabra'
True
>>> 'zoo' in 'ooze'
False
>>>
```

Python has a built-in function to check the length of a string:

```python
>>> len('')
0
>>> len('abracadabra')
11
>>> len('Bwa' + 'ha' * 10)
23
>>>
```

## `str`: Indexing and Slicing

An index is a position within a string. Each character, including spaces, have an index. Positive indexes start from 0 and read from left to right. Negative indexes start from -1 and start from right to left. Example:

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| L   | e   | a   | r   | n   |     | t   | o  |    | p  | r  | o  | g  | r  | a  | m  |
| -16 | -15 | -14 | -13 | -12 | -11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

To print the first character in the string `'Learn to program'` we have two options:

```python
>>> s = 'Learn to program'
>>> s[0]
'L'
>>> s[-16]
'L'
>>>
```

To print the second character in the string, we can do this:

```python
>>> s[1]
'e'
>>> s[-15]
'e'
>>>
```

The above examples show how to print a string with one character. If you want to print more then one character you need to slice. A slice is a substring from the start index up to, but not including the end index. Example:

```python
>>> s[0:5]
'Learn'
>>> s[6:8]
'to'
>>> s[9:16]
'program'
>>> s[9:len(s)]
'program'
>>> s[9:]
'program'
>>>
```

The last three slices (`s[9:16]`, `s[9:len(s)]` and `s[9:]`) all do the same thing: start from index 9 up to the end of the string. The first example, `s[9:16]`, is easy to read but you have to know the last index. The second example, `s[9:len(s)]`, starts at index 9 and calculates the last index with the `len()` function. The argument is the string or the variable that the string is assigned to. The last example is the shortest of all and to me the most easiest to read. If a `:` follows a number, it means that the slice starts at the number and ends at the last index.

The start of the slice can also be written in several ways:

```python
>>> s[0:8]
'Learn to'
>>> s[:8]
'Learn to'
>>>
```

To print the whole string with a slice:

```python
>>> s[:]
'Learn to program'
>>>
```

You can also use negative indexes in a slice:

```python
>>> s[-10:-8]
'to'
>>>
```

Note that while negative indexes start from right to left, the slice is written from left to right! In the example above you can't write `s[-8:-10]` if you want the substring `to`.

Indexing and slicing does not change the string. In all the previous examples, the string `Learn to program` is still the same because strings are immutable. That means they can't be changed. But you can use parts of the string, concatenate it and assign it to the same variable it was previously assigned too. Example:

```python
>>> s = 'Learn to program'
>>> s = "I'm " + s[:5] + 'ing' + s[5:] + '.'
>>> s
"I'm Learning to program."
>>>
```

## `str` Methods: Functions Inside of Object

Importing a module creates the module_name as a variable. After importing the module, you can use the functions inside of a module with `module_name.function(argument)`. Example:

```python
>>> import math
>>> math.sqrt(4.0)
2.0
>>>
```

A method is a function inside of an object. In the example above, the part `.sqrt()` is the method. The general form of a method call:

> `object.method(arguments)`

Example:

```python
>>> white_rabbit = "I'm late! I'm late! For a very important date!"
>>> white_rabbit.lower()
"i'm late! i'm late! for a very important date!"
>>> white_rabbit.count('ate')
3
>>>
```

In the example with `white_rabbit`, the string is never changed because strings are immutable. We seen the `lower()` and `count()` method. Both methods are built-in python and have a help page: `help(str.count)` and `help(str.find)`. There are many more methods for `str`, `help(str)` shows them all.

## `for` Loop Over `str`

The general form for a `for` loop over a `str`:

```
for variable in str:
    body
```

Example:

```python
>>> s = Yesterday
>>> for character in s:
        print(s)
Y
e
s
t
e
r
d
a
y
>>>
```

This lessons introduces another term: accumulator. Take this example:

```python
def num_vowels(user_string):
    """ (str) -> int
    
    Return the amount of vowels in user_string, but do not 
    treat the letter y as a vowel.
    
    >>> num_vowels('Hello there!')
    4
    >>> num_vowels('Abracadabra')
    5
    """
    num_vowels = 0

    for character in user_string:
        if character in 'aeiouAEIOU':
            num_vowels = num_vowels + 1

    return num_vowels
```

This is a `for` loop over a string. The loop will loop over each character in the string and if the character is in string `'aeiouAEIOU'` the amount of `num_vowels` is increased by one. After all characters are passed, the amount of vowels is returned. The accumulator in this little program is the variable `num_vowels` and it's a numeric accumulator.

There is another accumulator and that's the string accumulator. Example:

```python
def collect_vowels(user_string)
    """ (str) -> str
    
    Return a string with all vowels from user_string, but do no
    treat the letter y as a vowel.
    
    >>> collect_vowels('Happy Anniversary!')
    x
    >>> collect_vowels('xyz')
    x
    """
    
    vowels = ''
    
    for banana in user_string:
        if banana in 'aeiouAEIOU':
            vowels = vowels + banana
    
    return vowels
```

The variable `vowels` is a string accumulator. It is set to an empty string (and we have to set it before the `for` loop, else we get an error) and accumulates the vowels in the `user_string`. After all character are looped through, a string with all vowels in it is returned. If there are no vowels an empty string is returned. 

Note that `banana` is a variable and can be anything you want. It's wise to name it something that explains what it is, but this is just an example to show that you can name it anything you want.