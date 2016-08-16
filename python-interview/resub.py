import re

def multiply(m):
    # Convert group 0 to an integer.
    v = int(m.group(0))
    # Multiply integer by 2.
    # ... Convert back into string and return it.
    return str(v * 2)

# Use pattern of 1 or more digits.
# ... Use multiply method as second argument.
result = re.sub("\d+", multiply, "10 20 30 40 50")
print(result)
