# write function that checks if even number
def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Not even"

# take str and return true if len > 5 else false
def is_great_length(digit):
    if len(digit) > 5:
        return True
    else:
        return False
    