PLACEHOLDER = '[name]'

with open("../Mail Merge Project Start/input/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("../Mail Merge Project Start/input/letters/starting_letter.txt") as letter_to_automate:
    letter_contents = letter_to_automate.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
        with open(f'../Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}', mode = 'w') as completed_letter:
            completed_letter.write(new_letter)




