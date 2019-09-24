# Write a function that converts a string to a float and returns the result.

def string_to_float(str):
    try:
        return float(str)
    except ValueError:
        print("Could not make conversion.")

c = string_to_float("ham")
print(c)