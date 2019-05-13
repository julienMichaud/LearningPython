class = blueprint for objects. Classes can contain methods (functions) and attributes (similar to keys in a dict)
instances = objects that are constructed from a class blueprint that contain their class's methods and properties 
encapsulation = the grouping of public and private attributes and methods into a programmatic class, making abstraction possible
abstraction = exposing only "relevant" data in a class interface, hiding private attrbitues and methods (aka the "inner workings") from UserString
the self keyword refers to the current class instance 
class attributes= We can also define attributes directly on a class that are shared by all instances of a class and the class itself 
class methods = methods (with the @classmethod decorator) that are not concerned with instances, but the class itself 
the __repr__ method is one of several ways to provide a nice string representation

class User:

    active_users = 0  # class attribute

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first,last,age = data_str.split(",")
        cls(first, last, age)
        return cls(first, last, int(age))

    def __init__(self,first, last, age):
        self.first = first
        self.last = last
        self.age
        User.active_users += 1 ## refer to class atribute

    def __repr__(self):
        return f"{self.first} is {self.age}"

    def logout(self):
        User.active_user -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age +=
        return f"Happy {self.age}th, {self.first}"


user1 = User("Joe", "Smith", 68)
user2 = User("blanca", "lopez", 41)
tom = User.from_string("Tom","Jones","89") # class method
print(User.display_active_users()) # show class method
print(user2.is_senior())








class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat'] ## class attribute

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species


cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")

