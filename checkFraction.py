# to start with fraction in python,firstly import module
# A fraction has a numerator and a denominator, both of which are integers. This module has support for rational number arithmetic.

import fractions
print(fractions.Fraction(10, 3))
print(fractions.Fraction(1000, 245))

'''While creating Fraction from float, we might get some unusual results. This is due to the imperfect binary floating point number
 representation.Fortunately, Fraction allows us to instantiate with string as well. 
 This is the preferred options when using decimal numbers.'''

print(fractions.Fraction(2.1))  # as floating number

print(fractions.Fraction('2.1'))  # as a string
print(fractions.Fraction('1023.12'))
