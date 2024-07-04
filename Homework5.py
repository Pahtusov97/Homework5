immutable_var = ([1, 2], "a", "b")
immutable_list = [1, 2, 6, 7, 8]
immutable_list.extend("Хочу есть")
immutable_list[2] = 15
immutable_var[0] = 25 # нельзя изменить элемент кортежа, но если элементом кортежа является список, то можно изменить элемент самого списка)
print(immutable_list, immutable_var)