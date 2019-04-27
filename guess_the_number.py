import random 

random_number = random.randint(1,10)

player_number = int(input ("input your choice "))

while player_number != random_number:
    if player_number < random_number: 
        print ("go higher")
        player_number = int(input ("input your choice "))
    elif player_number > random_number: 
        print ("go lower")
        player_number = int(input ("input your choice "))
#elif player_number == random_number:
print (f"the number was {random_number}")
