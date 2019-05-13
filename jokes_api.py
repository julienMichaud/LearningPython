import requests
from random import choice


user_input = input("what would like to search for ?")
url = "https://icanhazdadjoke.com/search"



res = requests.get(
    url ,
    headers={"Accept": "application/json"},
    params={"term": user_input}
    ).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print ("there are many jokes")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print ("there is one joke")
    print (res["results"][0]['joke'])
else:
    print ("there are no jokes")

