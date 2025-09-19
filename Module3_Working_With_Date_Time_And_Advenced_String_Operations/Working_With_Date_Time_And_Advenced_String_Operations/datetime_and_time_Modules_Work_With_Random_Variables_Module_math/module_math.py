# The math package in Python provides access to the mathematical functions defined by the C language standard. 
# This package includes functions for various mathematical operations, including trigonometric calculations, 
# logarithms, square roots, and more.
# Let's take a look at some of the key features and constants that this package provides:
# Constants:
#  - math.pi - the constant 𝜋 (approximately 3.14159...); 
#  - math.e - the constant 𝑒, the base of natural logarithms (approximately 2.71828...); 
#  - math.tau - the constant 𝜏, equal to 2𝜋 (approximately 6.28318...); 
#  - math.inf - the infinity notation; 
#  - math.nan - the 'Not a Number' notation;
# Functions for rounding numbers:
#  - math.ceil(x) - rounds a real number x to the nearest larger integer; 
#  - math.floor(x) - rounds a real number x to the nearest smaller integer; 
#  - math.trunc(x) - truncates the fractional part of a real number x, and returns the integer part of the number;
# Example of use:
import math

x = 3.14

ceil_result = math.ceil(x)
floor_result = math.floor(x)
trunc_result = math.trunc(x)

print(f"ceil: {ceil_result}; \nfloor: {floor_result}; \ntrunc: {trunc_result}")



# Trigonometric functions
# - math.sin(x) - sine of x, where x is in radians; 
# - math.cos(x) - cosine of x; 
# - math.tan(x) - tangent of x; 
# - math.asin(x) - arcsine of x; 
# - math.acos(x) - arccosine of x; 
# - math.atan(x) - arctangent of x;
# Exponential and logarithmic functions
# - math.exp(x) - the number 𝑒 in the power of x; 
# - math.log(x[, base]) - the logarithm of x with base. If base is not specified, the natural logarithm is calculated;
# Degree and root
# - math.pow(x, y) - x to the power of y; 
# - math.sqrt(x) - the square root of x;
# Some other functions
# - math.fabs(x) - the modulus (absolute value) of x; 
# - math.factorial(x) - the factorial of x; 
# - math.gcd(x, y) - the greatest common divisor for x and y;
# An example of using the math package
import math

print(f"\npi: {math.pi}")
angle = math.radians(50)
print(f"sin: {math.sin(angle)}")
print(f"sqrt: {math.sqrt(9)}")
print(f"log: {math.log(10, 2)}")



# The math.isclose function is used to compare two numbers with a certain acceptable error. 
# This is useful for comparing real numbers where a direct comparison may not be reliable.
import math

r = math.isclose(0.14 + 0.100, 0.2)
print(f"\nr: {r}")



# We can also perform comparisons with a small margin of error:
import math

r = math.isclose(0.1, 0.10000000009)
print(f"\nr: {r}")





import datetime

now = datetime.datetime.now()
formatted_date = "%d.%m.%Y %H:%M:%S"
formatted_weekday = "%A"
print(f"Today: {now.strftime(formatted_date)}")
print(f"Wd: {now.weekday()}")
    

