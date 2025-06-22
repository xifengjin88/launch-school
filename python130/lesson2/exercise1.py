def combine(a, b, c):
    return a, b, c

def multiply(a, b, /):
    return a * b

def describe_pet(pet_type, /, *, name=""):
    return f"{name} is a {pet_type}"

def find_person(**kwargs):
    for name, profession in kwargs.items():
        if name == "Antonina":
            return profession
    return None

def concat_strings(*args, sep=" "):
    return sep.join(args)

def register(username, age, *,  password):
    return username, age, password

def print_message(*, message, level="INFO"):
    print(f"{level}: {message}")
    
def printer(message):
    print(message)
    
def later(fn, msg):
    return lambda: fn(msg)



if __name__ == '__main__':
    print_warning = later(printer, "The system is shutting down!")
    print_warning()  # The system is shutting down!
