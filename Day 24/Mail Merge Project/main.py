# This code will generate letters with the proper name in the invited names text document.
PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt", "r") as names:
    name_list = names.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as reference_letter:
    letter_content = reference_letter.read()
    for name in name_list:
        clean_name = name.strip()
        finished_letter = letter_content.replace(PLACEHOLDER, clean_name)
        with open(f"./Output/ReadyToSend/letter_for_{clean_name}.txt", "w") as completed_letter:
            completed_letter.write(finished_letter)
