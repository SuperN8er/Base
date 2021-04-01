"""This module will describe data structures"""

"""There are four different data stuctures"""

"""
1. Lists

+ A list is ordered
+ A list is mutable
+ Use brackets for a list []

-----------------------------------------

2. Tuples

+ A tuple is ordered
+ A tuple is immutable
+ Use parenthesis for a tuple ()

-----------------------------------------

3. Sets

+ A set is unordered
+ A set is unique (it cannot have duplicate values)

-----------------------------------------

4. Dicts

+ A dict is ordered
+ A dict is mutable
+ A dict contains key/value pairs

"""


# my_list = []  # this is how you specify an empty list

my_list = ["hello", 999, 3.14]

# print(my_list[0])
# # hello
# print(my_list[-1])
# # 3.14

# my_list[0] = "goodbye"
# print(my_list)
# # ['goodbye', 999, 3.14]


my_list.append("piss")
# print(my_list)
# # ['hello', 999, 3.14, 'piss']


# print(my_list.count(999))
# print(my_list.index(999))
# print(my_list[1])


# print(my_list[my_list.index("piss")])
index = my_list.index("piss")
value = my_list[index]
print(value)


# ==========================================================

# my_tuple = ()  # or my_tuple = tuple()

# my_tuple = ("hello", 999, 3.14)

# print(my_tuple[0])
# # hello
# print(my_tuple[-1])
# # 3.14

# my_tuple[0] = "goodbye"
# print(my_tuple)
# # Traceback (most recent call last):
# #   File "C:\Users\adams\Desktop\SHIT\data_structures.py", line 61, in <module>
# #     my_tuple[0] = "goodbye"
# # TypeError: 'tuple' object does not support item assignment

# ==========================================================

# my_set = set()  # this is how you make an empty set
# YOU CANNOT DO `my_set = {}` because this is a dict

# my_list = [1, 2, 4, 1, 3, 4]
# print(set(my_list))  # removes duplicates
# # {1, 2, 3, 4}

# ==========================================================

# my_dict = {}  # or dict()

# my_dict = {
#     "key1": "hello",
#     "key2": 999,
#     "key3": 3.14
# }

# print(my_dict["key3"])
# # 3.14

# my_dict["key4"] = "GOODBYE"
# print(my_dict)
# # {'key1': 'hello', 'key2': 999, 'key3': 3.14, 'key4': 'GOODBYE'}

# my_dict["key1"] = "Anyting I want"
# print(my_dict)
# # {'key1': 'Anyting I want', 'key2': 999, 'key3': 3.14}


