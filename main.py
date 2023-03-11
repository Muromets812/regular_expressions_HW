import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def name_normal(rows):
    result = [' '.join(item[0:3]).split(' ')[0:3] + item[3:7] for item in rows]
    return result


def del_duplicates(correct_list):
    result_list = []
    for item1 in correct_list:
        for item2 in correct_list:
            if item1[0:2] == item2[0:2]:
                list_employee = item1
                item1 = list_employee[0:2]
                for i in range(2, 7):
                    if list_employee[i] == '':
                        item1.append(item2[i])
                    else:
                        item1.append(list_employee[i])
        if item1 not in result_list:
            result_list.append(item1)

    return result_list


def updating_phone_numbers(rows, pb_pattern, new):
    pattern = re.compile(pb_pattern)
    phonebook = [[pattern.sub(new, string) for string in strings] for strings in rows]

    return phonebook


correct_list = name_normal(contacts_list)
relult_list = del_duplicates(correct_list)
pb_pattern = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s]*[(доб.\s]*(\d+)[)]*'
correct_pb = updating_phone_numbers(relult_list, pb_pattern, r'+7(\2)\3-\4-\5 доб.\6')

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(correct_pb)
