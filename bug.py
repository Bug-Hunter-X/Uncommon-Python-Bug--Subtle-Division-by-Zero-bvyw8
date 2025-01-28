def my_function(x):
    if x == 0:
        return 0  # Correct handling of x == 0
    else:
        return 1 / x

print(my_function(0))  # Output: 0
print(my_function(2))  # Output: 0.5
print(my_function(1))  # Output: 1.0
print(my_function(0.5)) # Output: 2.0
print(my_function(-1)) # Output: -1.0
print(my_function("abc")) # Output: TypeError: unsupported operand type(s) for /: 'int' and 'str'