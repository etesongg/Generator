import random

from functions.Load_file_data import LoadFileData

class NameGenerate:
    def generate_name(self):
        name = LoadFileData()
        last_name = random.choice(name.load_file("resource/", "last_names.txt"))
        first_name = random.choice(name.load_file("resource/", "first_names.txt"))

        generated_name = f'{last_name}{first_name}'
        # print(generated_name)
        return generated_name
