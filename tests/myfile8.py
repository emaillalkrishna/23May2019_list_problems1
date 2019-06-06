# # Python3 code to iterate through all keys in a dictionary
#
# states_and_capitals = {
#                         'Gujarat'  : 'Gandhinagar',
#                         'Maharashtra': 'Mumbai',
#                         'Rajasthan': 'Jaipur',
#                         'Bihar': 'Patna'
#                     }
#
# print('List Of given states:\n')
#
# # Iterating over keys
# for i in states_and_capitals:
#     print(i)

# # ------------------------------------

# # Python3 code to iterate through all keys in a dictionary in a specific order
#
# from collections import OrderedDict
#
# states_and_capitals = OrderedDict([
#                                     ('Gujarat', 'Gandhinagar'),
#                                     ('Maharashtra', 'Mumbai'),
#                                     ('Rajasthan', 'Jaipur'),
#                                     ('Bihar', 'Patna')
#                                 ])
#
# print('List Of given states:\n')
#
# # Iterating over keys
# for state in states_and_capitals:
#     print(state)

# # -------------------------------------

# # Python3 code to iterate through all values in a dictionary
#
# states_and_capitals = {
#                         'Gujarat': 'Gandhinagar',
#                         'Maharashtra': 'Mumbai',
#                         'Rajasthan': 'Jaipur',
#                         'Bihar': 'Patna'
#                     }
#
# print('List Of given capitals:\n')
#
# # Iterating over values
# for capital in states_and_capitals.values():
#     print(capital)

# # ---------------

# # Python3 code to iterate through all key, value pairs in a dictionary
#
# states_and_capitals = {
#                         'Gujarat': 'Gandhinagar',
#                         'Maharashtra': 'Mumbai',
#                         'Rajasthan': 'Jaipur',
#                         'Bihar': 'Patna'
#                     }
#
# print('List Of given states and their capitals:\n')
#
# # Iterating over values
# for state, capital in states_and_capitals.items():
#     print(state, ":", capital)


## ------------------------
# my_dict = {'x': 1, 'y': 2, 'z': 3}
# for i in my_dict:
#     print("{}: {}".format(i, my_dict[i]))


my_dict = {'x': 1, 'y': 2, 'z': 3}
for i in my_dict.values():
    print(i)

# my_dict = {'x': 1, 'y': 2, 'z': 3}
# for x, y in my_dict.items():
#     print("{}: {}".format(x, y))