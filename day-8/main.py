def greet():
    print("Hello, user")
    print("How are you, user? ")
    print("It's a fine day today! user ")


def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"How are you, {name}? ")
    print(f"It's a fine day today! {name} ")


def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"How are you, {name}? ")
    print(f"It's a fine day today in {location} ! {name} ")


greet()
var_name = input("Enter your name: ")
greet_with_name(var_name)
var_location = input(f"Where do you live, {var_name} ? ")
greet_with(var_name, var_location)

# Functions with keyword arguments
print("Invoking the greet_with() method using keyword Arguments in the same order as declaration")
greet_with(name=var_name, location=var_location)
print("Invoking the greet_with() method using keyword Arguments in mixed up order")
greet_with(location=var_location, name=var_name)
