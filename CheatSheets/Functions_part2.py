def sum_all_nums(*args):
    total = 0 
    for num in args:
        total += num
    return total

print (sum_all_nums(4,6,9))

## **kwargs    # special operator we can pass to functions,  gathers remaining keyword arguments as a dictionary 

def fav_olors(**kwargs):
    print(kwargs)
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

fav_colors(cold="purple", ruby="red", ethel="teal")

def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"

## parameter ordering
# parameters
# *args
# default parameters
# **kwargs


### tuple unpacking

def sum_all_values(*args):
    total = 0 
    for num in args:
        total += num
    print(total)

nums = (1,2,3,4,5,6)
sum_all_values(*nums)


### dictionary unpacking

def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

display_names(**names)
