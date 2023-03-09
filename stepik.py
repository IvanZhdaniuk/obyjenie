from typing import Optional

# def format_name_list(names: list)-> str:
#     name_list = []
#     name_string = ''
#     for i in names:
#         name_list.append(i['name'])
#     count = len(name_list)
#     if count == 1:
#             name_string = name_list[0]
#     elif count == 2:
#             name_string = name_list[0]+ ' и '+ name_list[1]
#     elif count >2:
#         count_in = count-1
#         for i in range(count):
#             if i < count-2:
#                 name_string += name_list[i] + ', '
#
#             if i == count -2:
#                 name_string += name_list[i]
#             if i == count-1:
#                 name_string += ' и ' + name_list[i]
#     return (str(name_string))
#
#
# print('annotations', format_name_list.__annotations__)
#
#
#
#
#
#
#
#
#
#
#
#
# # код ниже не стоит удалять, он нужен для проверки
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer и Marge'
#
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'
#
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart и Lisa'
#
# assert format_name_list([{'name': 'Bart'}]) == 'Bart'
#
# assert format_name_list([]) == ''
#
# assert format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {'name': 'Bart'}, {'name': 'Moe'}]) == 'Maggie, Lisa, Barney, Homer, Bart и Moe'
#
# assert format_name_list([{'name': 'Marge'}, {'name': 'Maggie'}, {'name': 'Seymour'}]) == 'Marge, Maggie и Seymour'
#
# assert format_name_list([{'name': 'Maude'}, {'name': 'Bart'}]) == 'Maude и Bart'
#
# print('Проверки пройдены')

#
# def first_repeated_word(string:str)->Optional:
#     a: list = string.split()
#     print(a)
#     b: list = []
#
#     for i in a:
#         if i in b:
#             return i
#             break
#         else:
#             b.append(i)
#
# assert first_repeated_word("ab ca bc ab") == "ab"
# assert first_repeated_word("ab ca bc Ab cA aB bc") == "bc"
# assert first_repeated_word("ab ca bc ca ab bc") == "ca"
# assert first_repeated_word("ab ca bc") == None

