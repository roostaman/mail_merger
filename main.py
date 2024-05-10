with open('./Input/Letters/starting_letter.txt', mode='r') as template_file:
    template_letter = template_file.read()

names_list = []

with open('./Input/Names/invited_names.txt', mode='r') as names_file:
    for line in names_file:
        names_list.append(line.strip())

for name in names_list:
    new_letter = template_letter.replace('[name]', name)
    with open(f'./Output/ReadyToSend/{name}_letter.txt', mode='w') as ready_file:
        ready_file.write(new_letter)
