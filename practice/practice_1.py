# file = open('my_file.txt')
# content = file.read()
# print(content)

# with open('my_file.txt') as file:
#     content = file.read()
#     print(content)

# with open('my_file.txt', mode="a") as file:
#     file.write('\nNew text is here!')

# with open('/Users/rustam/Desktop/PieProjects/PRO2/mail_merge_practice.py/my_file_2.txt', mode="w") as file:
#     file.write('\nI will replace all text!')
#
# with open('/Users/rustam/Desktop/PieProjects/PRO2/mail_merge_practice.py/my_file_2.txt', mode="r") as file:
#     content = file.read()
#     print(content)

letter = '''Hello [name]!
Tomorrow come to my birthday party at 5pm!'''

names_list = ['Aaron', 'Ron', 'Bob']

# personalized_letters = [letter.replace('[name]', name) for name in names_list]
p = []
for name in names_list:
    p_l = letter.replace('[name]', name)

print('========')
