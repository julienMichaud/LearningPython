def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(color) is not str:
        raise TypeError("color must be instance of str")

    if type(text) is not str:
        raise TypeError("text must be a string")

    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")

colorize("hello", "red")


### exception

def get(d,key)
    try:
        d[key]
    except KeyError:
        return None


d = {"name": "Ricky"}
print (get(d, "city"))



### try, except, else, finally
while True:
    try: 
        num = int(input("please enter a number: "))
    except ValueError:
        print ("that's not a number !")
    else: 
        print("good job, you entered a valid number")
        break
    finally: 
        print(" RUNS NO MATTER WHAT")




## another example

def divide(a,b): 
    try:
        return a/b
    except (ZeroDivisionError, TypeError) as err:

        print ("something went wrong")
        print (err)
    else:
        print(f"{a} divided by {b} is {result}")

divide('a'/2)




## use the debugging 
# at start of file
# import pdb

#pdb.set_trace() to stop at a giving line 