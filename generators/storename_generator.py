import random

from functions.Load_file_data import LoadFileData

class StoreGenerate:
    def generate_storename(self):
        name = LoadFileData()
        store_name = random.choice(name.load_file("resource/", "store_types.txt"))
        dong = random.choice(name.load_file("resource/", "dongs.txt"))
        num = random.randint(1, 20)

        generated_storename = f'{store_name} {dong}{num}호점'
        # print(generated_storename)
        return generated_storename
