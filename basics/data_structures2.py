"""
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]
1
>>> squares[-1]
25
>>> sqaures[-3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqaures' is not defined
>>> squares[-3:]
[9, 16, 25]
>>> sqaures[:]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqaures' is not defined
>>> squares[;]
  File "<stdin>", line 1
    squares[;]
            ^
SyntaxError: invalid syntax
>>> squares[:]
[1, 4, 9, 16, 25]
>>>  sqauares + [36, 49, 64, 81, 100]
  File "<stdin>", line 1
    sqauares + [36, 49, 64, 81, 100]
    ^
IndentationError: unexpected indent
>>>  squares + [36, 49, 64, 81, 100]
  File "<stdin>", line 1
    squares + [36, 49, 64, 81, 100]
    ^
IndentationError: unexpected indent
>>>  squares + [36, 49, 64, 81, 100]
  File "<stdin>", line 1
    squares + [36, 49, 64, 81, 100]
    ^
IndentationError: unexpected indent
>>> sqaures[:]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqaures' is not defined
>>> squares[0]
1
>>> # this is the first comment
>>> spam = 1 # and this is the second comment
>>> # ... and now a third!
>>> text = "#This is not a comment because it's inside quuotes."
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5 # division alaways returns a floating point number
1.6
>>> 17 / 3 #classic division returns a float
5.666666666666667
>>> cubes = [1, 8, 27, 65, 125] # something's wrong here
>>> 4 ** 3 # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64 # repllace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
>>> cubes.append(216) # and the cube of 6
>>> cubes.append(7 ** 3) # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now rmove them
>>> letters[2:5] = []
>>> leters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'leters' is not defined
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list  by replacing all the elements with an emtpy list
>>> letters[:] = []
>>> letters
[]
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
>>> courses = ['History', 'Math', 'Physics', 'CompSci']
>>> course_str = ' - ', join(courses)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'join' is not defined
>>> for item in courses:
... print(course)
  File "<stdin>", line 2
    print(course)
    ^
IndentationError: expected an indented block
>>> emuerate(courses)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'emuerate' is not defined
>>> list_1 = ['History', 'Math', 'Physics', 'CompSci']
>>> list_2 = list_1
>>> print(list_1)
['History', 'Math', 'Physics', 'CompSci']
>>> print(list_2)
['History', 'Math', 'Physics', 'CompSci']
>>> # Sets
>>> cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
>>> print(cs_courses)
{'Math', 'CompSci', 'History', 'Physics'}
>>> cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
>>> print('Math' in cs_courses)
True
>>> art_courses = {'History', 'Math', 'Art', 'Design'}
>>> print(cs_courses.union(art_courses)

>>> print(cs_courses.union(art_courses))
{'Design', 'Art', 'Physics', 'History', 'CompSci', 'Math'}
>>>

"""

#List

list_a = [1, 2, 3, 2, 1]
list_b = [3, 4, 5, 6, 6, 2, 5, 5, 4]


"""

find the index of 3 in both list and print the count for both list

"""
list_a_index = list_a.index(3)
print(f"list_a_index = {list_a_index}")
list_b_index = list_b.index(3)
print(f"list_b_index = {list_b_index}")


"""


Number times "1" appear in list A and numbers of times "5" appears in list B.


"""
list_a_count =  list_a.count(1)
print(f"list_a_count = {list_a_count}")
list_b_count = list_b.count(5)
print(f"list_b_count = {list_b_count}")


"""



append the 7 8 9 to list a and the 1 2 3 to list b


"""



print(list_a)
list_a.append(7)
list_a.append(8)
list_a.append(9)
print(list_a)

print(list_b)
list_b.append(1)
list_b.append(2)
list_b.append(3)
print(list_b)



"""
create a list with letters a b c.
print list a alter itthe print list b alter it
extend list a & b with new  list.
"""

list_c = ['a', 'b', 'c']
print(list_a)
list_a.extend(list_c)
print(list_a)

print(list_b)
list_b.extend(list_c)
print(list_b)




