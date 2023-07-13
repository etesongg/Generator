from generators.name_generator import NameGenerate
from generators.addr_generator import AddrGenerate
from generators.gender_generator import GenderGenerate



def main():
    name = NameGenerate()
    name.generate_name()
    addr = AddrGenerate()
    addr.generate_addr()
    gender = GenderGenerate()
    gender.generate_gender()

if __name__ == "__main__":
    main()