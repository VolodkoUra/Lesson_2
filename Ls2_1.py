# Строки
my_string = "Hello World"
print(my_string)

print(my_string.lower()) #Все буквы маленькие
print(my_string.islower()) #Проверка все ли маленькие
print(my_string.isdigit()) #Проверка есть ли в строке цифры
print(my_string.find("l")) # Индекс первого вхождения
print(my_string.rfind("o")) # Индекс последнего вхождения

# Списки, множества, кортежи, словари
my_list = [3,4,5,6,7]
my_list2 = [2,8,5]
my_list.append(8) #Добавление
print(my_list)
my_list.remove(4) # Удаление по значению
print(my_list)

del my_list[1] # Удаление по индексу
print(my_list)

my_list.extend(my_list2)  # Добавляет к первому спску второй
print(my_list)

my_list.insert(1,9) #Вставляет значение по индексу
print(my_list)

"""Создать два списка произвольного содержания.
Добавить к каждому списку по одному элементу в конец и в начало.
Расширить первый список вторым.Все изменения выводить на экран"""
my_list3 = [5,12,'a', 2.3]
my_list4 = [True, 87, 9.8, 'b']
my_list3.insert(0,"FFF")
my_list3.append(77)
print(my_list3)
my_list4.insert(0, "HHH")
my_list4.append(92)
my_list3.extend(my_list4)
print(my_list4)
print(my_list3)

my_dict = {
    True : "Minsk",
    False : "Moscow",
    True : "Milan"
}
print(my_dict)

my_dict2 = {
    1 : "Gomel",
    4 : "Grodno",
    7 : "Minsk"
}
print(my_dict2)

"""Создать словарь с одной парой. 
Ключ - кортеж, значение - списокСоздать словарь с одной парой. 
Ключ - список, значение - кортеж"""
my_dict3 = {
    (1,2):["Tom", "Bob"],
    (2,3):["Rob", "Bill"]

}
#my_dict4 = {
    #["Tom", "Bob"] : (1,2),
    #["Rob", "Bill"] : (2,3)

#}   # Так нельзя
print(my_dict3)


"""Создать два списка a = [1,2,3,4] и b = [ ] Вывести на экран id 
a и b Присвоить b значение a (b=a)Вывести на экран id переменных
Добавить элемент в список bВывести на экран оба списка"""
a = [1,2,3,4]
b = []
print(id(a))
print(id(b))
b = a
print(id(a))
print(id(b))