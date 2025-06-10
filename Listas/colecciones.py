#### Listas 

my_list = [1,2,3, 'x', 'xd', True, 2.3, [0,1]]

print(my_list)
print(my_list[6])
my_list[7] = 10

my_list.append('inserta valores')
print(my_list.pop())
print(my_list)

##Diccionarios 

my_dict = {
    "name": "Peter",
    "last_name": "Parker",
    "age": 20,
    "hero": "Spiderman",
    "power": "super strong",
    "is_single": True,
    "height": 1.80
}

print(my_dict["name"])
print(f"{my_dict["name"]} {my_dict["last_name"]} es {my_dict["hero"]}")

my_dict["power"]


print(my_dict)

print(my_dict.keys)
print(my_dict.values)