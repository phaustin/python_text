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

# Review Questions

+++ {"latex": {"environment": "problems"}}

## Arithmetic

Q03.01 $2 + \frac{1}{2}$

Q03.02 $4 \times 2 + \frac{2}{4}$

Q03.03 $\frac{5}{2} \times 3 + 4$

Q03.04 $4^2 + 3$

Q03.05 $\sqrt{16}$

Q03.06 $3^{4-5}$

Q03.07 $\frac{1+3+5}{2+4+6}$

Q03.08 $1 - 2 + \frac{9}{6} -3 + 5$

Q03.09 $(3 + 5 -2)^{2/3}$

Q03.10 $\frac{5+3}{2 \times 5}$

Q03.11 $\sqrt{6^2 + 4}$

Q03.12 $1 + 9 \times \frac{8}{4^2} + 1^{3-4} \times \frac{1}{2.5}$

+++

## Strings

Q03.15 Define the string "Problem"

Q03.16 Two strings "Problem" and "Solving with Python". Combine these strings to produce "Problem Solving with Python". Hint: Don't forget the space.

Q03.17 Compare the strings "Problem" and "problem" with the comparison operator ```==```. Explain the result.

Q03.18 Compare the output of the code ```1 + 2 == 3``` and ```'1 + 2' == '3'```. Explain why the output is different.

+++ {"latex": {"environment": "problems"}}

## Trigonometry

Q03.30 Find the sine of $0$, $\pi/4$, $\pi/2$, $3\pi/4$, and $\pi$.

Q03.31 Find the cosine of 0 degrees, 30 degrees, 60 degrees and 90 degrees.

Q03.32 Find the tangent of 3/4, 5/12, and -8/6.

Q03.33 Find the sin of 0.1 radians. Then find the arcsine of the result and see if it equals 0.1 radians.

Q03.34 The U.S. Forest service can use trigonometry to find the height of trees. The height of a tree, $h$ is equal to the distance $d$ between an observer and the base of the tree multiplied by the tangent of the angle $\theta$ between looking straight along the ground and looking up at the top of tree according to the formula:

$$ h = d\tan(\theta) $$

If a Forest Service ranger is 20 feet away from the base of a douglas fir tree and looks up at a 63 degree angle relative to straight ahead to see the top of the tree, what is the height of the douglas fir tree?

Q03.35 The tangent of an angle is equal to the sine of the angle divided by the cosine of the angle. Make two calculations, one for the tangent of -29 degrees and another calculation for the sine of -29 degrees divided by the cosine of -29 degrees. Do you observe the same output?

Q03.36 A simple model of water level based on tides (assuming high tide is at midnight) is:

$$ h = (4.8)\sin(\pi/6)(t+3)+5.1 $$

Where $h$ is the water height and $t$ is the number of hours since midnight. Using this model, calculate the water level $h$  at 6am ($t=6$ hours since midnight).

Q03.37 The x-component of a force $F_x$ is equal to the magnitude of the force $|\vec{F}|$ multiplied by the cosine of the angle $\theta$ of the force relative to the positive x-axis.

$$ F_x = |\vec{F}|\cos(\theta) $$

If the magnitude of a force $|\vec{F}| = 12.4$ and the force acts at $\theta=110$ degrees relative to the positive x-axis, what is the x-component of the force $F_x$?

Q03.37 The distance $d$ a free-thrown projectile travels is dependent on the projectile's initial velocity $v_0$, the acceleration due to gravity $g=9.81 m/s^2$ and the angle $\theta$ at which the project is launched according to:

$$ d = \frac{{v_0}^2}{g} \sin(2\theta) $$

If a projectile is launched at a 12 degree angle with an initial velocity of 150 m/s, how far will the projectile travel?

+++ {"latex": {"environment": "problems"}}

## Logarithms and Exponents

Q03.41 Show that the natural log of Euler's number, $\ln(e)$, is equal to one.

Q03.42 Logarithms turn multiplication into addition. Complete both of the calculations below to see if the expressions are equal to each other:

$$ \log(87.1 \times 210 \times 10^{3}) $$

$$ \log(87.1) + \log(210) + \log(10^{3}) $$

Q03.43 Logarithms turn exponents into multiplication and multiplication into addition. Complete both of the calculations below to see if the expressions are equal. Remember, Python has a couple log functions including ```log()``` and ```log10()```.

$$ \log(6.02 \times 10^{23}) $$

$$ 23+\log(6.02) $$

Q03.44 Python's math module has the natural log ($\ln$) function ```math.log()``` and the log (base 10) function ```math.log10()```. If you want to find the log with an arbitrary base, $b$, of a number $n$, you can use a ratio of natural logarithms (log base $e$) according to:

$$ \log_b(n) = \frac{\ln(n)}{\ln(b)} $$

Calculate the base 4 logarithm of $3.9 \times 10^{-9}$

$$ log_{4}(3.9 \times 10^{-9}) $$

Q03.45 The magnitude of a vector $|\vec{v}|$ is equal to the square root of the sum of the squares of the vector's components $v_x$, $v_y$, and $v_z$ according to:

$$ |\vec{v}| = \sqrt{{v_x}^2 + {v_y}^2 + {v_z}^2} $$

What is the magnitude of a vector $\vec{v}$ that has components $v_x = 76.3$, $v_y = 70.9$, $v_z = 93.6$ ?

Q03.46 Moore's Law, a relationship that states the number of transistors that fit on a microchip doubles every two years can be modeled as:

$$ P_n = P_0 \times 2^n $$

Where $P_0$ is the original number of transistors on a microchip and $P_n$ is the number of transistors on a microchip after $n$ number of years since the original microchip.  If the original microchip has 1000 transistors, how many transistors are projected to be on a microchip 40 years later according to Moore's Law?

+++ {"latex": {"environment": "problems"}}

## Variables in Calculations

Q03.71 $a = 2$, $b = 3$, calculate $\frac{4}{5}(a^2 - b^3)$

Q03.72 The area of a circle, $a$, is dependent on the circle's radius, $r$, according to:

$$ a=\pi r^2 $$

What is the area of a circle with radius $r=4$?

Q03.73 The area of a circle, $a$, is dependent on the circle's diameter, $d$, according to:

$$ a=\pi (\frac{d}{2})^2 $$

What is the area of a circle with diameter $d=6$?

Q03.74 The volume of a sphere, $v$, is dependent on the sphere's radius, $r$, according to:

$$ v=(\frac{4}{3})\pi r^3 $$

What is the volume of a sphere with radius $r=1.5$?

Q03.75 The volume of a cylinder, $v$, is dependent on the cylinder's radius, $r$, and height, $h$, according to:

$$ v=\pi r^2 h $$

What is the volume of a cylinder with radius $r=5$ and height $h=10$ ?

Q03.76 The surface area of a sphere, $a_s$ is related to the sphere's radius, $r$, according to:

$$ a_s=4\pi r^2 $$

What is the surface area $a_s$ of a sphere with radius $r=2.5$?

Q03.77 The general equation for the distance, $d$, that a free falling body travels (neglecting air resistance) is:

$$ d = \frac{1}{2}gt^2 $$

$g$ is the acceleration due to gravity and $t$ is the fall time. Assume the acceleration due to gravity $g = 9.81$. How far (what distance) will a ball fall in time $t = 12$?

Q03.78 The general equation for the fall time, $t$, that a free falling body takes (neglecting air resistance) to cover a distance, $d$ is:

$$t = \sqrt{\frac{d}{0.5g}}$$

$g$ is the acceleration due to gravity. Assume the acceleration due to gravity $g = 9.81$. How long (what time) will it take a base jumper to fall distance $d = 2000$?

Q03.79 The value of an investment $v$ compounded annually at an interest rate of $r\%$ after $n$ years is dependent on the original investment $P$ according to:

$$ v = P(1 + r/100)^n $$

If $P=1000$ dollars at a rate of $r=7\%$, what will the value $v$ be after $n=20$ years?

Q03.80 The original principal $P$ needed to produce a total savings of value $v$ at a rate of $r\%$ over $n$ years is calculated by:

$$ P = \frac{v}{(1+r/100)^n} $$

What is the principal $P$ needed to save one million dollars at a rate $r=10\%$ over $n=40$ years?

Q03.81 Electrical power $P$ is related to current $I$ and resistance $R$ according to:

$$ P = I^2R$$

An electrical load with a resistance $R = 10,000$ running at a current $I=0.200$ draws how much power $P$ ?

+++

## Errors, Explanations, and Solutions

For each of the problems below, run the line of code. Then explain the error in your own words. Give an explanation more specific than ```invalid syntax```. Then suggest and run a line of code that fixes the error.

Q03.91

```python
>>> 9 x 10
```

Q03.92

```python
>>> 1 1/2 + 2 2/3
```

Q03.93

```python
>>> 3cos(35)
```

Q03.94

```python
>>> 8.31 x 10^9
```

Q03.95

```python
>>> (2+3)**(2-3e(4)
```

Q03.96

```python
>>> 7% + 8% + 9%
```

Q03.97

```python
>>> (-)54.2 + 9.2
```

Q03.98

```python
>>> '5' / '4'
```

Q03.99

```python
>>> ln(e) - log(10)
```

```{code-cell} ipython3

```
