# Compie
### Compie is the successor to Whirlcalc
#### Compie is made with ❤️ on Python

#### Compie can do a lot of computations and other related stuffs (more features adding..)
#### It is a small module as of now so there isn't any docs out there.. everything you need to know is just here in this page.

This module includes:
```
FUNCTIONS:
- make_penguin()            added in version 1.0
- isprime(number)           added in version 2b1
- ratio(int,int)            added in version 2b1
- factorial(int)            added in version 0.1b
- arithmetic_mean(list)     added in version 1.4
- decimal2binary(int)       added in version 1.6.1
- binary2decimal(int)       added in version 1.6.2
- decimal2octal(int)        added in version 1.6.3
- octal2decimal(int)        added in version 1.6.4
- hexadecimal2decimal(str)  added in version 1.6.5
- decimal2hexadecimal(int)  added in version 1.6.6
- evaluate(str)             added in version 0.1b

CLASSES:
- decimal(value)            added in version 2b0
- binary(value)             added in version 2b0
- octal(value)              added in version 2b0
- hexadecimal(value)        added in version 2b0
```
NOTE: `evaluate()` only supports `factorial()` and `pi`.


Can I use it?
> Yeah! Of course! you can use it.. (Only if you are a cute penguin!)

and if you are not a penguin.. then.. try this:
```
>>> from compie import *
>>> make_penguin()
```


# Documentation:

FUNCTIONS: 

make_penguin():
>### SECRET EASTER EGG ☺

Some Functions:
Decimal to Binary:
```
>>> from compie import *
>>> print(binary2decimal('110001001'))
>>> 393
```
Factorial:
```
>>> from compie import *
>>> print(factorial(5))
>>> 120
```
Evaluate:
```
>>> from compie import *
>>> print(evaluate("2*3+100-190+factorial(3)-pi"))
>>> -81.1415926535898
```
Isprime:
```
>>> from compie import *
>>> print(isprime(2))
True
>>> #EXAMPLE 2:
>>> print(isprime(1))
ValueError: 1 is neither prime nor composite.
```
ratio:
```
>>> from compie import *
>>> print(ratio(10,51390))
1:51390
```
### You may have figured out how to use other functions.

CLASSES:

decimal:
```
>>> from compie import *
>>> my_decimal_class = decimal(10)
>>> print(my_decimal_class.hex) #note hex stands for hexadecimal..
A
```
```
Classes Tree:
 decimal:
  variables:
    - value (assigned value)
    - dec (decimal value)
    - bin (binary value)
    - hex (hexadecimal value)
    - oct (octal value)
  functions:
    - setvalue(value,numtype)
      - value is the value in any number system (if using another system then numtype must be specified)
      - numtype is argument about number type (default is "dec")
 binary:
  variables:
    - value (assigned value)
    - dec (decimal value)
    - bin (binary value)
    - hex (hexadecimal value)
    - oct (octal value)
  functions:
    - setvalue(value,numtype)
      - value is the value in any number system (if using another system then numtype must be specified)
      - numtype is argument about number type (default is "bin")
 hexadecimal:
  variables:
    - value (assigned value)
    - dec (decimal value)
    - bin (binary value)
    - hex (hexadecimal value)
    - oct (octal value)
  functions:
    - setvalue(value,numtype)
      - value is the value in any number system (if using another system then numtype must be specified)
      - numtype is argument about number type (default is "hex")
 octal:
  variables:
    - value (assigned value)
    - dec (decimal value)
    - bin (binary value)
    - hex (hexadecimal value)
    - oct (octal value)
  functions:
    - setvalue(value,numtype)
      - value is the value in any number system (if using another system then numtype must be specified)
      - numtype is argument about number type (default is "oct")

Well.. This is probably enough for you to understad! you may look at the functions list for list of all functions!
```


<br>

# CHANGELOG:
```
v2.0.1:
> fixed bugs
  > a very stupid testing bug in __init__.py of the module that i made for testing (a "print(ratio(10,51390))")
  > a small coding mistake in this README file..

v2b1:
> added function
  > ratio
  > isprime

v2b0:
> added classes
  > decimal
  > binary
  > octal
  > hexadecimal

v1.0.0:
> added functions
  > decimal2binary
  > binary2decimal
  > hexadecimal2decimal
  > decimal2hexadecimal
  > octal2decimal
  > decimal2octal
  > make_penguin
```
