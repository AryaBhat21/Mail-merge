from docx import Document

PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        doc = Document()
        doc.add_paragraph(new_letter)

        #print(new_letter)
        # with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx","w") as completed_letter:
        #     completed_letter.write(new_letter)

        output_path = f"./Output/ReadyToSend/letter_for_{stripped_name}.docx"
        doc.save(output_path)

print("Successfully printed! ")
