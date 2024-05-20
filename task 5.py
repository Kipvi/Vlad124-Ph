list_players = ["Маша", "Петя", "Саша","Оля", "Кирилл"]
last_player = list_players[-1]
reestr = {"Первый участник": list_players[0]}
print("Последний участник:", last_player)
print("Первый участник:", reestr["Первый участник"])

list_participants = ["Орлов", "Петров", "Иванов", "Сидоров", "Васильев", "Черепахин"]
last_player = list_participants[-1]
reestr = {"Первый участник": list_participants[0]}
print("Последний участник:", last_player)
print("Первый участник:", reestr["Первый участник"])

sps_Book=["Дубровский", "Горе от ума", "Кавказский пленник", "Хамелеон","Ревизор", "Гранатовый браслет"]
last_Book = sps_Book[-1]
reestr = {"Первая книга": sps_Book[0]}
print("Последния книга:", last_Book)
print("Последния книга:", reestr["Первая книга"])

shopping_list = ["Палатка", "Спальник", "Котелок", "Тренога", "Рюкзак", "Спальник","Рюкзак", "Термос", "Миска", "Ветровка", "Коврик" ]
unique_items = set(shopping_list)
print("Количество уникальных товаров:", len(unique_items))
