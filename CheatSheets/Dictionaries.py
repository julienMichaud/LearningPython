

cat {"name": "blue", "age": 3.5, "isCute": True }
cat2 = dict(name="kitty", age=0.5)

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

cat['age'] ## find the key age in the dictionari and return the value 

for v in instructor.values(): ## change "values" to "keys" if you want the keys to be returned. 
    print v ## return the values

for k,v in instructor.items(): ## access key and values 
    print (f"key is {k} and Value is {v}")


## Does dictionary have a key ? 
"name" in instructor ## return True

## Does dictionary have a value ?

"Colt" in instructor.values() # Return True 

## Dictionary methods

instructor.clear() ## clear the dictionary 
instructor2= instructory.copy() ## copy the dictionary to the variable instructor2
new_user= {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
instructor.get('name') ## Return Colt
instructor.get('adress') ## Return None and NOT False ! 
instructor.pop("own_dog") ## remove they key/value 
instructor.popitem() ## delete the last k/v pair of the dictionary
## update method
person = {"city": "Antigue"} 
person.update(instructor) ## add the k/v from instructor to the person dic

## Dictionary comprehension

{___:___for___in___} # syntax

[num: num**2 for num in [1,2,3,4,5]] ## {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range (0,len(str1))}
print (combo) # {'A': '1', 'B': '2', 'C': '3'}

yelling_instructor = {k.upper():v.upper() for k,v in instructor.items()}

num_list = [1,2,3,4]
{ num:("even" if num % 2 == 0 else "odd") for num in num_list }
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
