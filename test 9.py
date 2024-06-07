def name_func(arg):
    #начало тела функции
...
#Конец тела функции

#Структурирование кода
#Сколько времени понадобавится, чтобы понять, какой общий смысл здесь заложент?
list_ = [1, 2, 3, 4, 5]
a = list_[len(list_) // 3]
for b in range(len(list_)):
    if list_[b] < a:
        a = list_[b]
print(a)

list_ = [1, 2, 3, 4, 5]
a = list_[len(list_) // 3]
for b in range(len(list_)):
    if list_[b] < a:
        a = list_[b]
    return a
list_ = [1, 2, 3, 4, 5]
min_(list_) #ищем минимум, как будем искать будем разбираться на мере необходимости

#Задача 1
list_1 = [1, 2, 3]
list_2 = [6, 5, 4]
min_1 = list_1[0]
for value in list_1:
    if value < min_1:
        min_1 = value
min_2 = list_2[0]
for value in list_2:
    if value < min_2:
        min_2 = value
result = min_1 + min_2
result

def min_(list_):
    min_value = list_[0]
    for value in list_:
        if value < min_value:
            min_value = value
    return min_value
list_1 = [1, 2, 3]
list_2 = [6, 5, 4]
result = min_1 + min_2
result

#Пример простейшей функции
def empty_func():
    pass #pass можно заменить на ...
result = empty_func() #но даже такая функция всёравно возвращает результат None
print(result) #None

#Функция которая просто печатает строку, почему бы и  нет
def hello_world(): #Объявление функции
    print("Hello world")
hello_world() #Вызов функции
hello_world() #Вызов функции

#Функции возвращает значение
def return_hello_world():
    return "Hello World" + "!!!"
return_value = return_hello_world()
print(return_value)
def return_tuple_with_values():
    return 1, 2, 3 #По умолчанию python возвращет кортеж
result = return_tuple_with_values()
print(type(result), result)

a, b, с = return_tuple_with_values()
print(a, b, c)
result = return_tuple_with_values()
a, с = result[0], result[-1]
print(a, с)

a, _, с = return_tuple_with_values()
print(a, c)

def return_first_value():
    ...
    return 1
    return 2
print (return_first_value())

def

def multi_return():
    number =... # Какое-то целое число
    if number % 2 == 0:
        return “Число четное”
    else:
        return “число нечетное”

def multi_return():
    first_number = ...
    second_number = ...
    if first_number > second_nunber:
        return “Первое число больше”
    elif first_nunber < second_number:
        return “Второе число больше”
    else:
        return “числа равны”

def pow_func(base, pow_=2):
    return  base ** pow_
print(pow_func(4))
print(pow_func(3, pow_ = 3))
print(pow_func(5))
print(pow_func(2, 5))
print(pow_func(pow_ = 2, base = 8))
