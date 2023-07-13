import random

from functions.Load_file_data import LoadFileData

class NameGenerate:
    def generate_name(self):
        last_name_data = LoadFileData("resource/", "last_names.txt")
        last_name = random.choice(last_name_data.load_file())
        first_name_data = LoadFileData("resource/", "first_names.txt")
        first_name = random.choice(first_name_data.load_file())

        generated_name = f'{last_name}{first_name}'
        # print(generated_name)
        return generated_name
