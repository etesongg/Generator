import random

from functions.Load_file_data import LoadFileData

class AddrGenerate:
    def generate_addr(self):
        addr = LoadFileData()
        citie = random.choice(addr.load_file("resource/", "cities_kr.txt"))
        gu = random.choice(addr.load_file("resource/","gu_kr.txt"))
        addr_num = random.randint(1, 100)
        addr_road = random.choice(["길", "로"])
        
        generated_addr = f'{citie} {gu} {addr_num}{addr_road} {addr_num}'
        # print(generated_addr)
        return generated_addr
