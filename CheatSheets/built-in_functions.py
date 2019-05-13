### all
# Return true if all elements of the iterable are truthy (or if the iterable is empty)
all([0,1,2,3]) # False
all([char for char in 'eio' if char in 'aeiou']) # False
all([num for num in [4,2,10,6,8] if num % 2 == 0]) # True





### any 
# return true if any element of the iterable is truthy. if the iterable is empty, return False

any([0, 1, 2, 3])
any([val for val in [1,2,3] if val > 2]) # true 
any([val for val in [1,2,3] if val > 5]) # false 

### sorted
# work on anything that is iterable
more_numbers = [6,1,8,2]
sorted(more_numbers) # [1,2,6,8]

## max
# return the largest item in an iterable or the largest of two or more arguments
max('c', 'd', 'a') # d


# reversed
# return a reverse iterator
nuns = [1,2,3,4]
nuns.reverse()

## abs 
# return the absolute value of a number. The argument may be an integer or a floating point number 
abs(-23) # 23


## sum 
# Takes an iterable and an optional start
# Returns the sum of start and the itemas of an iterable from left to right and returns the total
sum([1,2,3], 10) # 16


## round 
# return number rounded to ndigits precision after the decimal point. if ndigits is omitted or is None, it returns the nearest integer to its input. 
round(10.2) #10
round(1.212121, 2) # 1.21 


## zip 
# makes an iterator that aggregates elements from each od the iterables. 
# returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables