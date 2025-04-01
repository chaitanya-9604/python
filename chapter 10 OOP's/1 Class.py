class employee:
    language = "py" # this is an class atribute
    salary = 1200000

chaitanya = employee()
chaitanya.name = "Chaitanya" #this is an instance atribute
print(chaitanya.salary, chaitanya.language)


avinash = employee()
avinash.name = "Avinash"
print(avinash.salary, avinash.language, avinash.name)

# object attributes == instance attributes
'''here name is instance attribute and salary and language are class
attributes as they directly belong to the class''' 

