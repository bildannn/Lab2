# 1
# def list_reorder(ref_list):
#     names = ref_list[0]
#     surnames = ref_list[1]
#
#     reordison_list = []
#     for name, surname in zip(names, surnames):
#         reordison_list.append([name, surname])
#
#     return reordison_list
#
#
# ref_list = [['Александр', 'Анастасия'], ['Смирнов', 'Иванова']]
# result = list_reordison(ref_list)
# print(result)

# 2
# def del_rep(num):
#     linfes_nums = list(set(num))
#     sorted_nums = sorted(linfes_nums)
#     return sorted_nums


# Пример использования
# num = [1, 2, 1, 2, 3, 1, 2, 3, 4]
# result = del_rep(num)
# print(result)
# Ответ: [1, 2, 3, 4]


# 5
# def check_phn(phones):
#     formatted_phones = []
#     for phone in phones:
#         # Удаление разделителей
#         digits = ''.join(filter(str.isdigit, phone))
#
#         # Проверка длины номера
#         if len(digits) != 11:
#             formatted_phones.append(-1)
#             continue
#
#         # Проверка первой цифры
#         if digits[0] not in ['7', '8']:
#             formatted_phones.append(-1)
#             continue
#
#         # Форматирование номера с разделителями
#         formatted_phone = '+7(' + digits[1:4] + ')' + digits[4:7] + '-' + digits[7:9] + '-' + digits[9:11]
#         formatted_phones.append(formatted_phone)
#
#     return formatted_phones
#
#
# phones = ['+7(123)456-7890', '8(123)456-7890', '+7 123 456 78901', '123 456 7890']
# result = check_phn(phones)
# print(result)