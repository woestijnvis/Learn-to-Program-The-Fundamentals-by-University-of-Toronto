# Part 1: Strings

## Input/Output and `str` Formatting

The `print()` function can take more than one argument and arguments are separated by a comma. After evaluation, the values are separated by a space. You don't need to concatenate the arguments with the `+` operator.

Example:

```python
>>> print('Hello', 'there.')
Hello there.
>>> print("You're", 'a', 'bold', 'one.')
You're a bold one.
>>>
```

The general form for a `return` statement:

> `return expression`

When a `return` statement executes, the expression is evaluated to produce a memory address. 

- *What is passed back to the caller?* The memory address.
- *What is displayed?* Nothing!

Example of a `return` statement:

```python
>>> def square_return(num):
        return num ** 2
>>> answer_return = square_return(4)
>>> answer_return
16
>>> answer_return
16
>>>
```

In the above example, on line 3, the function `square_return` is called and the argument provided is `4`. The function takes the argument and puts 4 to the power 2. This expression results in the value `16`. It is the memory address (that contains `16`) that is assigned to the variable `answer_return`. Nothing is displayed to the user, there was only some calculation done. But when you call `answer_return`, it will show the value that is contained in the memory address. Notice how you can call `answer_return` over and over and that is keeps retaining the value `16`.

The general form for a `print()` statement:

> `print(argument)`

When a `print()` function call is executed, the argument(s) are evaluated to produce memory address(es). This is the same as in the `return` statement.

- *What is passed back to the caller?* Nothing!
- *What is displayed?* The values at those memory address(es) are displayed on screen.

Example of a `print()` statement:

```python
>>> def square_print(num):
        print('The square of num is', num ** 2)
>>> answer_print = square_print(4)
The square of num is 16
>>> answer_print
>>> 
```

In the above example, on line 3, the function `square_print` is called with `4` as provided argument. There is no `return` statement in this function, so what will happen is that the string `The square of num is 16` will be printed once and immediately. If you call `answer_print`, like on line 5, it shows nothing because the function `square_print` has the value `None`. This is caused by the lack of a `return` statement.

> A function that does not have a return statement returns `None`.

## Docstrings and Function Help

Docstrings provide information and help for you functions.

Example:

```python
def area(base, height):
    """(number, number) -> number
    
    Return the area of a triangle with dimensions base and height.
    """
    
    return base * height / 2
```

The built-in help function shows the description of a function. The parameters are shown in IDLE when you type the function name and first parenthesis.

!["Example of help function in IDLE."](function_description.png "Example of help function in IDLE")

# Part 2: Designing Functions

## Function Design Recipe

Functions should be designed with these six steps in mind:

1. Examples
2. Type contract
3. Header
4. Description
5. Body
6. Tests

Take a look at the example below. The problem that we would like to solve is creating a function that converts Fahrenheit degrees to Celsius degrees.

Step 1, **examples**:

- What should your function do?
- Type a couple of examples.
- Pick a name for the function. What is the short answer to "What does your function do"?

```python
>>> convert_to_celsius(32)
0.0
>>> convert_to_celsius(212)
100.0
```

Step 2, **type contract**:

- What are the parameter types?
- What type of value is returned?

```python
(number) -> float

>>> convert_to_celsius(32)
0.0
>>> convert_to_celsius(212)
100.0
```

Step 3, **header**:

- Pick meaningful parameter names.

```python
def convert_to_celsius(fahrenheit):
    """(number) -> float

    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    """
```

Step 4, **description**:

- Mention every parameter in your function.
- Describe the return value.

```python
def convert_to_celsius(fahrenheit):
    """(number) -> float

    Return the number of Celsius degrees equivalent to fahrenheit degrees.

    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    """
```

Step 5, **body**:

- Write the code.

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

Step 6, **tests**:

- Run the examples from step 1 and try some other tests.

## Function Reuse

Functions can be reused (that's why we're writing functions, for easy code reuse) and they can be called from other functions and in function calls. Let explore calling functions in other functions first.

We have a function that calculates the perimeter of a triangle:

```python
def perimeter(side1, side2, side3):
    """(number, number, number) -> number
    
    Return the perimeter of a triangle with sides of length side1, side2 and side3.
    
    >>> perimeter(3, 4, 5)
    12
    >>> perimeter(10.5, 6, 9.3)
    25.8
    """
    
    return side1 + side2 + side3
```

The problem we would like to solve is that we also need the semiperimeter. We can write another function for that:

```python
def semiperimeter(side1, side2, side3):
    """(number, number, number) -> float
    
    Return the semiperimeter of a triangle with sides of length side1, side2, side3.
    
    >>> semiperimeter(3, 4, 5)
    6.0
    >>> semiperimeter(10.5, 6, 9.3)
    12.9
    """
    
    return perimeter(side1, side2, side3) / 2
```

The only function `semiperimeter` has is adding all sides and dividing the result by 2. We could write all of that ourselves but we outsource the addition part to function `perimeter`. After we get the result back (the addition) we divide it by 2. This sounds like a silly example, but it shows how to call other functions instead of rewriting code. Remember that functions are for code-reuse.

Let's explore calling functions in function calls. The problem we want to solve is to figure out which pizza slice is the largest. We have a tape measure and a function for that:

```python
def area(base, height):
    """(number, number) -> number
    
    Return the area of a triangle with dimensions base and height.
    
    >>> area(4, 7)
    14.0
    >>> area(3.6, 8.9)
    16.02
    """
    
    return base * height / 2
```

```python
>>> max(area(3.8, 7), area(3.5, 6.8))
13.299999999999999
>>> area(3.8, 7)
13.299999999999999
>>> 
```

We call the function `area` in function call `max()`. `max()` needs at least two arguments to spit out the largest value. We provide two arguments by calling `area` and providing the arguments we measured. The function `area` returns a single value and because we called it two times, but with different arguments we get two different values back. The two values are then compared to each other by `max` and evaluate to a single value. To visualise the flow of this function call:

```
max(area(3.8, 7), area(3.5, 6.8))
↓
max(13.299999999999999, 11.9)
↓
13.299999999999999
```

## Visualizing Function Calls

What stood out most to me is the scope of variables in a a function. Variables in a function are destroyed after the function ends. Also, variables in a function can only be used locally (in the function). They do not exist outside of the function.