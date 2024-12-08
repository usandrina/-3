# TODO Напишите функцию find_common_participants

def find_common_participants(a, b, c):
    list_1 = a.split(c)
    list_2 = b.split(c)
    for i, current_item in enumerate(list_1):
        for j, current_item_2 in enumerate(list_2):
            if current_item_2 == current_item:
                return current_item

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group,"|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
