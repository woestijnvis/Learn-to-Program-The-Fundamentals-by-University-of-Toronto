# Part 1: Fancy string processing

## More `str` Operators

You can concatenate strings with the `+` operator and multiple strings with the `*` operator. Let's see other operators at work with strings:

The equality and inequality operators:

```python
>>> 'a' == 'a'
True
>>> 'ant' == 'ace'
False
>>> 'a' == 'a'
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

An index is a position within a string. Each character, including spaces, have an index. Positive indexes start from 0 and read from left to right. Negative index start from -1 and start from right to left. Example:

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

Note that while negative indexes start from right to left, the slice is written from left to right! In the example above you can't write `s[-8:-10]` if you want the string `to`.

Indexing and slicing does not change the string. In all the previous examples, the string `Learn to program` is still the same because strings are immutable. That means they can't be changed. But you can use parts of the string, concatenate it and assign it to the same variable it was previously assigned too. Example:

```python
>>> s = 'Learn to program'
>>> s = "I'm " + s[:5] + 'ing' + s[5:] + '.'
>>> s
"I'm Learning to program."
>>>
```

## `str` Methods: Functions Inside of Object

## `for` Loop Over `str`

# Part 2: IDLE's Debugger

## IDLE's Debugger