months = ('January', 'February', "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
## tuples = immutable list, cant add, remove or replace any elements once you declare it
# Tuples in a dictionary

location = {
    (35.6895, 39.6917): "Tokyo Office"
    (40.7128, 74.0060): "New York Office"
    (37.7749, 122.4194): "San Francisco Office"
}

locations[(37.7749, 122.4194)] ## Return San Francisco Office

### Looping tuples


for month in months:
    print month()

i = len(months) -1
while i >= 0:
    print (months[i])
    i -= 1 

## methods
# 
x = (1,2,3,3,3)
x.count(1) # 1
x.count(3) # 3

t.index(1) # 0
t.index(5) ## value error
t.index(3) #2 - only the first matching index is returned 


### Sets ### array of unique elements and its has no order. 

s = set({1, 2, 3, 4, 5, 5, 5}) # {1, 2, 3, 4, 5}

s = set({1, 4, 5})

s = {1, 4 ,5} # same as above

4 in s # True 

8 in s # False 

cities = ["Los Angeles", "Boulder", "Kyoto", "Florence", "Santiago", "Los Angeles", "Shangai", "Boulder", "San Francisco", "Oslo", "Tokyo"]
print(len(set(cities))) # print number of unique cities

print(list(set(cities))) ## list of unique cities only 


## set methods

s = set([1, 2, 3])
s.add(4)
s # {1, 2, 3, 4}
s.add(4)
s # {1, 2, 3, 4} ## elemets already present in the set (4)

s.remove(3)
print(s) # {1,2}
## can use .discard instead of remove to avoid an error if an element is not in the set

another_s= s.copy()


#use set1 & set2  to return the elements present in the two sets only

### Set comprehension

{x**2 for x in range(10)} # {0, 1, 64, 4, 36, 9,, 16, 49, 81, 25}
{char.upper() for char in 'hello'} # {'O', 'L', 'H', 'E'}