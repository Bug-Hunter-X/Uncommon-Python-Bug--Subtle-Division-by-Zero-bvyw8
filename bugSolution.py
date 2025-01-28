def my_function(x):
    try:
        if abs(x) < 1e-9:  # Check for numbers extremely close to zero
            return 0  # Return 0 for values practically equal to 0
        elif isinstance(x,(int,float)):
            return 1 / x
        else:
            raise TypeError("Input must be a number.")
    except TypeError as e:
        return f"Error: {e}"
    except ZeroDivisionError:
        return "Error: Division by zero"

print(my_function(0))  # Output: 0
print(my_function(2))  # Output: 0.5
print(my_function(1e-10)) # Output: 0
print(my_function(1))  # Output: 1.0
print(my_function(0.5)) # Output: 2.0
print(my_function(-1)) # Output: -1.0
print(my_function("abc")) # Output: Error: Input must be a number.