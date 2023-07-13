from generators.name_generator import NameGenerate
from generators.addr_generator import AddrGenerate

def main():
    name = NameGenerate()
    name.generate_name()
    addr = AddrGenerate()
    addr.generate_addr()

if __name__ == "__main__":
    main()