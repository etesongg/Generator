import random
import csv

from datetime import data

from functions.Load_file_data import LoadFileData
from generators.name_generator import NameGenerate

class User_generator:
    def __init__(self):
        data = load_file()
        self.name = Name_generator(data)
        self.gender = Gender_generator()
        self.birthdate = Birthdate_generator()
        self.age = Age_generator()
        self.address = Addr_generate(data)

