def square(num):
    return num * num
print(square(9))


square2 = lambda num: num * num 


## map
# standard function that accepts at least two arguments, a function and an iterable
# iterable - something that can be iterated over (lists,strings,dictionaries, sets,tuples
# # runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure)

nums = [2,4,6,8,10]
doubles = map(lambda x: x*2, nums)


people = ["Darcy", "Christina", "Dana", "Annabel"]
peeps = map(lambda name: name.upper(), people)
list(peeps)

## filter
## there is a lambda for each value in the iterable
# returns filter object which can be converted into other iterables
# the object contains only the values that return true to the lambda
l = [1,2,3,4]
evens = list(filter(lambda x: x % 2 == 0, 1))
evens # [2,4]

names = ["austin", "penny", "anthony", "angel", "billy"]
a_names = filter(lambda n: n[0]=='a', names)
