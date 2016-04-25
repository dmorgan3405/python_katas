FIZZ = "FiZz"
BUZZ = "BuZz"

def is_fizzy(value):
    return value % 3 == 0

def is_buzzy(value):
    return value % 5 == 0

def formatter(value):
    if is_fizzy(value) and is_buzzy(value):
        return FIZZ + BUZZ
    if is_fizzy(value):
        return FIZZ
    if is_buzzy(value):
        return BUZZ

def resolve(x):
    if is_fizzy(x) or is_buzzy(x):
        return formatter(x)
    return x
