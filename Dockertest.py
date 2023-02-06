import os  
import sys 
import scipy 

#print(os.getcwd())

foods =['falfal' , 'Apple' ,'Banana' , ' Tomatom']

foods.insert(2 ,'Ma7shi')
foods.pop()

for food in foods:
    print(food)


print(foods)

type(foods)

print("your favourite dash {0} , and another dash {1}" .format(foods[0] , "Bazngan"))

