# There are 100 doors in a row that are all initially closed.
# You make 100 passes by the doors. The first time through, visit every door and 'toggle' the door
# (if the door is closed, open it; if it is open, close it). The second time, only visit every 2nd door
# (i.e., door #2, #4, #6, ...) and toggle it. The third time, visit every 3rd door (i.e., door #3, #6, #9, ...), etc.,
# until you only visit the 100th door.

# Implement a function to determine the state of the doors after the last pass. Return the final result in an array,
# with only the door number included in the array if it is open.


variable_dictionary = {}

for i in range(1, 101):
    variable_dictionary[f"door_number_{i}"] = "closed"

print(variable_dictionary)

for key in variable_dictionary:
    variable_dictionary[key] = "open"
print(variable_dictionary)

for index, key in enumerate(variable_dictionary):
    # enumerate counts from 0 automatically, so the dict will product index, key like "0: door_number_1" etc
    # add 1 to counter the 0
    if (index + 1) % 2 == 0:
        variable_dictionary[key] = "closed"
print(variable_dictionary)

for index, key in enumerate(variable_dictionary, start=1):
    # by adding start=1 to the arguments, it makes enumerate count from 1 not 0
    if index % 3 == 0:
        if variable_dictionary[key] == "open":
            variable_dictionary[key] = "closed"
        else:
            variable_dictionary[key] = "open"
print(variable_dictionary)