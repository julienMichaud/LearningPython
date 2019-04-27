list = ["toto", "lala", 1.4, 3]

list2 = list(range(1, 101))

list[1] = julien # change lala to julien 
list [-1] # print 3 

"toto" in list # return True 

#loop a list
# for x in list: 
#  print (x) 

# # while with a list
# i = 0 
# while i < len(list):
#     print (list[i])
#     i =+ 1


### method for lists ###

list.append(5) ## add 5 at the end of the list "list "
list.extend(["toto","lala","lili"]) ## add 5, 4, 3 to the end of the list
list.insert (2,salut) ## insert salut to the index2 of the list 

list.clear() ## remove all items from the list
list.pop(2) ## remove the item at the index 2 of the list
list.remove(3) # remove the item 3, not the item where the index is 3 ! 
list.index(3) # return the index where item 3 is 
list.count(3) # return the number of time the item 3 is in the list
list.reverse() # reverse the items of a list
list.sort() #  sort the items of a list
' '.join(list) # toto lala lili 


### slicing ###
list[1:] # return lala, 1.4, 3
list [1:3] # return lala, 1.4   (it's exclusive, dont return index 3) 
list[1::2] ## return lala, 3
list [::2] #return toto, 1.4 
list[:1:-1] # return 3, 1.4 

### list comprehension ###

numbers = [1, 2, 3]
doubled_numbers = [num * 2 for num in numbers] ## print list [2, 4, 6]

name = 'colt'
[char.upper() for char in name] # ['C', 'O', 'L', 'T']
[char[0].upper() for friend in name] # ['Colt']

string_list = [str(num) for num in numbers] ## convert the numbers in string 

### list comprehension with conditionnal logic

numbers = [1, 2, 3, 4 ,5 ,6]
evens = [num for num in numbers if num % 2 == 0] 
odd = [num for num in numbers if num % 2 != 0] 



### nested list ###
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
nzsted_list[0][1] # 2
nested_list[1][-1] # 6

board = [[num for num in range(1,4)] for val in range(1,4)] # [1,2,3], [1,2,3], [1,2,3]

[["x" if num % 2 != 0 else "0" for num in range (1,4)] for val in range(1,4)] # [['X', '0', 'X'], ['X', '0', 'X'], ['X', '0', 'X']]