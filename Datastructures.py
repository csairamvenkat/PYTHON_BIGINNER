#Data structure  collection of Data type
#Matrix collection of Data structure




#Inbuilt -->List,tuple,set,dict
#User Defined-->Stack,LinkedList,Queue,Array,Tree

#Function-->inbuilt,userdefined(def keyword is used)
#Class-->Super,abstract,inbuild,user defined,thread
#Method-->special,user defined,abstract,instance,static,magic

#list
my_list = [1, 2, 3, 4, 5]
print(my_list[0])
my_list.append(6)
print(my_list)
my_list.remove(4)
print(my_list)
print(len(my_list))
print(my_list)
print(my_list[1:3]) #Similar to array indexing...starts from 0

#tuple can have diff data types in it, immutable (cant be altered) collection of items.
my_tuple = (1, 2, 3)
print(my_tuple)
my_tuple = (10, 'hello', 3.5)
print(my_tuple[0])  # Output: 10

#dict --key value pair
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])

#sets--An unordered collection of unique elements.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

#Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # or set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

#Intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2  # or set1.intersection(set2)
print(intersection_set)  # Output: {3}

#Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2  # or set1.difference(set2)
print(difference_set)  # Output: {1, 2}


# Symmetric Difference--Returns elements that are in either of the sets, but not in both.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
sym_diff_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print(sym_diff_set)  # Output: {1, 2, 4, 5}


#string
a='sairamvenkat'
print(a[1])

#array-->Collection of same type.Indexing starts from 0
from array import array
my_array = array('i', [1, 2, 3])  # 'i' represents integers
print(my_array[1])

#Deque-- A double-ended queue that allows appending and popping from both ends
from collections import deque
my_deque = deque([1, 2, 3])
my_deque.appendleft(0)
print(my_deque)  # Output: deque([0, 1, 2, 3])
my_deque.append(4)
print(my_deque)  # Output: deque([0, 1, 2, 3, 4])

#NamedTuple (from collections module)-- subclass of tuples with named fields for easier readability.
# it is immutable

from collections import namedtuple
Person = namedtuple('Person', ['name', 'age'])
namedtuple_person = Person(name='John', age=30)
print(namedtuple_person.name)  # Output: John
namedtuple_person = Person('Sai', 20)
print(namedtuple_person.age)




