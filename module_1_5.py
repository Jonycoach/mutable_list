# tuple = ([1, 2, 3], False, 1)
# immutable_var = tuple
# print(immutable_var)
# immutable_var [0] = 1
#Данные внутри кортежа не могут быть изменены

mutable_list = [(1, 2, 3), "Stringus", 158]
mutable_list[0] = [15]
print(mutable_list)
mutable_list[2] = True
print(mutable_list)
mutable_list[1] = tuple
print(mutable_list)
print(type(mutable_list[1]))