from generators.name_generator import NameGenerate
from generators.addr_generator import AddrGenerate
from generators.gender_generator import GenderGenerate
from generators.birthdate_generate import BirthdateGenerate
from generators.age_calc import AgeCale
from functions.printer import Printer

class Human_generate:
    def __init__(self):
        self.name = NameGenerate()
        self.addr = AddrGenerate()
        self.gender = GenderGenerate()
        self.birthdate = BirthdateGenerate()
        self.age = AgeCale()

    def generate_data(self):
        data = []
        for _ in range(Printer.input_count()):
            name = self.name.generate_name()
            addr = self.addr.generate_addr()
            gender = self.gender.generate_gender()
            birthdate = self.birthdate.generate_birthdate()
            age = self.age.calculate_age(birthdate)
            data.append(f'{name}, {gender}, {age}, {birthdate}, {addr}')

        Printer.output_type(data)


if __name__ == "__main__":
    human = Human_generate()
    human.generate_data()