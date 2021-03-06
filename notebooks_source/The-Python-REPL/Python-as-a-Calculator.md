---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.9'
    jupytext_version: 1.5.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Python as a Calculator

+++

Python can be used as a calculator to compute arithmetic operations like addition, subtraction, multiplication and division. Python can also be used for trigonometric calculations and statistical calculations.

+++

## Arithmetic

Python can be used as a calculator to make simple arithmetic calculations.

Simple arithmetic calculations can be completed at the Python Prompt, also called the _Python REPL_. REPL stands for Read Evaluate Print Loop. The Python REPL shows three arrow symbols ```>>>``` followed by a blinking cursor. Programmers type commands at the ```>>>``` prompt then hit ```[ENTER]``` to see the results.

Commands typed into the Python REPL are _read_ by the interpreter, results of running the commands are _evaluated_, then _printed_ to the command window.  After the output is printed, the ```>>>``` prompt appears on a new line. This process repeats over and over again in a continuous _loop_.

Try the following commands at the Python REPL:

Suppose the mass of a battery is 5 kg and the mass of the battery cables is 3 kg. What is the mass of the battery cable assembly?

```python
>>> 5 + 3
8
```

Suppose one of the cables above is removed and it has a mass of 1.5 kg. What is the mass of the leftover assembly?

```python
>>> 8 - 1.5
6.5
```

If the battery has a mass of 5000 g and a volume of 2500 $cm^3$ What is the density of the battery? The formula for density is below, where $D$ is density, $m$ is mass and $v$ is volume.

$$ D = \frac{m}{v} $$

In the problem above $m = 5000$ and $v=2500$

Let's solve this with Python.

```python
>>> 5000 / 2500
2.0
```

What is the total mass if we have 2 batteries, and each battery weighs 5 kg?

```python
>>> 5 * 2
10
```

The length, width, and height of each battery is 3 cm. What is the area of the base of the battery?
To complete this problem, use the double asterisk symbol ```**``` to raise a number to a power.

```python
>>> 3 ** 2
9
```

What is the volume of the battery if each the length, width, and height of the battery are all 3 cm?

```python
>>> 3 ** 3
27
```

Find the mass of the two batteries and two cables.

We can use Python to find the mass of the batteries and then use the answer, which Python saves as an underscore \_ to use in our next operation. (The underscore ```_``` in Python is comparable to the ```ans``` variable in MATLAB)

```python
>>> 2 * 5
10
>>> _ + 1.5 + 1
12.5
```

+++

### Section Summary

A summary of the arithmetic operations in Python is below:

| Operator | Description | Example | Result |
| --- | --- | --- | --- |
| ``` + ``` | addition | ```2 + 3 ``` | ```5``` |
| ``` - ``` | subtraction | ```8 - 6 ``` | ```2``` |
| ``` - ``` | negative number | ```-4``` | ```-4``` |
| ``` * ``` | multiplication | ``` 5 * 2 ``` | ``` 10 ``` |
| ``` / ``` | division | ``` 6 / 3 ``` | ``` 2 ``` |
| ``` ** ```| raises a number to a power | ``` 10**2 ``` | ``` 100 ``` |
| ``` _ ``` | returns last saved value  | ```_ + 7``` | ```107``` |

+++

## Trigonometry: sine, cosine, and tangent

+++

Trigonometry functions such as sine, cosine, and tangent can also be calculated using the Python REPL.

To use Python's trig functions, we need to introduce a new concept: _importing modules_.

In Python, there are many operations built into the language when the REPL starts. These include ```+``` , ```-```, ```*```, ```/``` like we saw in the previous section. However, not all functions will work right away when Python starts. Say we want to find the sine of an angle. Try the following:

```python
>>> sin(60)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sin' is not defined
```

This error results because we have not told Python to include the ```sin``` function. The ```sin``` function is part of the _Python Standard Library_. The Python Standard Library comes with every Python installation and includes many functions, but not all of these functions are available to us when we start a new Python REPL session. To use Python's ```sin``` function, first import the ```sin``` function from the ```math``` _module_ which is part of the Python Standard Library.

Importing modules and functions is easy. Use the following syntax:

```text
from module import function
```

To import the ```sin()``` function from the ```math``` module try:

```python
>>> from math import sin
>>> sin(60)
-0.3048106211022167
```

Success! Multiple modules can be imported at the same time. Say we want to use a bunch of different trig functions to solve the following problem.

An angle has a value of $\pi$/6 radians. What is the sine, cos, and tangent of the angle?

To solve this problem we need to import the ```sin()```, ```cos()```, and ```tan()``` functions. It is also useful to have the value of $\pi$, rather than having to write ```3.14....``` We can import all of these functions at the same time using the syntax:

```text
from module import function1, function2, function3
```

Note the commas in between the function names.

Try:

```python
>>> from math import sin, cos, tan, pi
>>> pi
3.141592653589793
>>> sin(pi/6)
0.49999999999999994
>>> cos(pi/6)
0.8660254037844387
>>> tan(pi/6)
0.5773502691896257
```

+++

### Section Summary

The following trig functions are part of Python's **math** module:

| Trig function | Name | Description | Example | Result |
| --- | --- | --- | --- | --- |
| ```math.pi``` | pi | mathematical constant $\pi$ | ```math.pi``` | ```3.14``` |
| ```math.sin()``` | sine | sine of an angle in radians | ```math.sin(4)``` | ```9.025``` |
| ```math.cos()``` | cosine | cosine of an angle in radians | ```cos(3.1)``` | ```400``` |
| ```math.tan()``` | tangent | tangent of an angle in radians | ``` tan(100)``` | ```2.0``` |
| ```math.asin()``` | arc sine | inverse sine, ouput in radians | ``` math.sin(4)``` | ```9.025``` |
| ```math.acos()``` | arc cosine | inverse cosine, ouput in radians | ```log(3.1)``` | ```400``` |
| ```math.atan()``` | arc tangent | inverse tangent, ouput in radians | ```atan(100)``` | ```2.0``` |
| ```math.radians()``` | radians conversion | degrees to radians | ```math.radians(90)``` | ```1.57 ``` |
| ```math.degrees()``` | degree conversion | radians to degrees | ```math.degrees(2)``` | ```114.59``` |

+++

## Exponents and Logarithms

+++

Calculating exponents and logarithms with Python is easy. Note the exponent and logarithm functions are imported from the **math** module just like the trig functions were imported from the **math** module above.

The following exponents and logarithms functions can be imported from Python's math module:

* ```log```
* ```log10```
* ```exp```
* ```e```
* ```pow(x,y)```
* ```sqrt```

Let's try a couple of examples:

```python
>>> from math import log, log10, exp, e, pow, sqrt
>>> log(3.0*e**3.4)         # note: natural log
4.4986122886681095
```

A right triangle has side lengths 3 and 4. What is the length of the hypotenuse?

```python
>>> sqrt(3**2 + 4**2)
5.0
```

The power function ```pow()``` works like the ```**``` operator. ```pow()``` raises a number to a power.

```python
>>> 5**2
25
```

<br>

```python
>>> pow(5,2)
25.0
```

### Section Summary

The following exponent and logarithm functions are part of Python's **math** module:

| Math function | Name | Description | Example | Result |
| --- | --- | --- | --- | --- |
| ``` math.e ``` | Euler's number | mathematical constant $e$ | ``` math.e ``` | ``` 2.718 ``` |
| ``` math.exp() ``` | exponent | $e$ raised to a power | ``` math.exp(2.2) ``` | ``` 9.025 ``` |
| ``` math.log() ``` | natural logarithm | log base e | ``` math.log(3.1) ``` | ``` 400 ``` |
| ``` math.log10() ``` | base 10 logarithm| log base 10 | ``` math.log10(100) ``` | ``` 2.0 ``` |
| ``` math.pow() ``` | power | raises a number to a power | ``` math.pow(2,3) ``` | ``` 8.0 ``` |
| ``` math.sqrt() ``` | square root | square root of a number | ``` math.sqrt(16) ``` | ``` 4.0 ``` |

+++

## Statistics

+++

To round out this section, we will look at a couple of statistics functions. These functions are part of the Python Standard Library, but not part of the **math** module. To access Python's statistics functions, we need to import them from the **statistics** module using the statement ```from statistics import mean, median, mode, stdev```. Then the functions ```mean```, ```median```, ```mode``` and ```stdev``` (standard deviation) can be used.

```python
>>> from statistics import mean, median, mode, stdev

>>> test_scores = [60, 83, 83, 91, 100]

>>> mean(test_scores)
83.4

>>> median(test_scores)
83

>>> mode(test_scores)
83

>>> stdev(test_scores)
14.842506526863986
```

Alternatively, we can import the entire **statistics** module using the statement ```import statistics```. Then to use the functions, we need to use the names ```statistics.mean```, ```statistics.median```, ```statistics.mode```, and ```statistics.stdev```. See below:

```python
>>> import statistics

>>> test_scores = [60, 83, 83, 91, 100 ]

>>> statistics.mean(test_scores)
83.4

>>> statistics.median(test_scores)
83

>>> statistics.mode(test_scores)
83

>>> statistics.stdev(test_scores)
14.842506526863986
```

+++

### Section Summary

The following functions are part of Python's **statistics** module. These functions need to be imported from the ```statistics``` module before they are used.


| Statistics function | Name | Description | Example | Result |
| --- | --- | --- | --- | --- |
| ``` mean() ``` | mean | mean or average | ``` mean([1,4,5,5]) ``` | ``` 3.75 ``` |
| ``` median() ``` | median | middle value | ``` median([1,4,5,5]) ``` | ``` 4.5 ``` |
| ``` mode() ``` | mode | most often | ``` mode([1,4,5,5]) ``` | ``` 5 ``` |
| ``` stdev() ``` | standard deviation | spread of data | ``` stdev([1,4,5,5]) ``` | ``` 1.892 ``` |
| ``` variance() ``` | variance | variance of data | ``` variance([1,4,5,5]) ``` | ``` 3.583 ``` |

```{code-cell} ipython3

```
