import json
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}
print(programming_dictionary)

# Adding a new item
programming_dictionary["Loop"] = "The action of doing something over a fixed number of times."
print(programming_dictionary)

# emty dicitionary
empty_dictionary = {}
empty_dictionary["first_item"] = "This is the first item."
empty_dictionary["second_item"] = "This is the second item."
# json_obj = json.loads(str(empty_dictionary))
json_frm_str = json.dumps(empty_dictionary, indent=4)
print(json_frm_str)

# Edit an item
programming_dictionary["Bug"] = "A moth in your computer."
print(json.dumps(programming_dictionary, indent=4))

# Looping thru a dictionary
for key in programming_dictionary:
    print(programming_dictionary[key])

# clear an existion dictionary
programming_dictionary = {}
print(json.dumps(programming_dictionary, indent=4))
