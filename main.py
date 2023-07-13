from generators.name_generator import NameGenerate
from generators.addr_generator import AddrGenerate
from generators.gender_generator import GenderGenerate
from generators.birthdate_generate import BirthdateGenerate
from generators.age_calc import AgeCale


def main():
    name = NameGenerate()
    name.generate_name()
    addr = AddrGenerate()
    addr.generate_addr()
    gender = GenderGenerate()
    gender.generate_gender()
    birthdate = BirthdateGenerate()
    birthdate.generate_birthdate()
    age = AgeCale()
    age.calculate_age(birthdate.generate_birthdate())

if __name__ == "__main__":
    main()