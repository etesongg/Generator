from generators.name_generator import NameGenerate
from generators.addr_generator import AddrGenerate
from generators.gender_generator import GenderGenerate
from generators.birthdate_generate import BirthdateGenerate
from generators.age_calc import AgeCale
from generators.uuid_generator import Uuidenerate
from generators.storename_generator import StoreGenerate
from generators.orderat_generator import OrderatGenerator
from generators.itemname_generator import ItemDataGenerate

from functions.printer import Printer
from functions.csv_get_id import CsvGetId


class Human_generate:
    def __init__(self):
        self.id = Uuidenerate()
        self.name = NameGenerate()
        self.addr = AddrGenerate()
        self.gender = GenderGenerate()
        self.birthdate = BirthdateGenerate()
        self.age = AgeCale()

    def generate_data(self):
        data = ["Id, Name, Gender, Age, BirthDate, Address"]
        
        for _ in range(Printer.input_count("user")):
            id = self.id.generate_uuid()
            name = self.name.generate_name()
            addr = self.addr.generate_addr()
            gender = self.gender.generate_gender()
            birthdate = self.birthdate.generate_birthdate()
            age = self.age.calculate_age(birthdate)
            
            data.append(f'{id},{name},{gender},{age},{birthdate},{addr}')

        Printer.output_type(data, "user_info.csv")

class Store_generate:
    def __init__(self):
        self.id = Uuidenerate()
        self.storename = StoreGenerate()
        self.addr = AddrGenerate()

    def generate_data(self):
        data = ["Id, Name, Type, Address"]
        
        for _ in range(Printer.input_count("store")):   
            id = self.id.generate_uuid()
            storename = self.storename.generate_storename()
            storetype = (storename.split())[0]
            addr = self.addr.generate_addr()
            
            data.append(f'{id},{storename},{storetype},{addr}')

        Printer.output_type(data, "store_info.csv")

class Order_generate:
    def __init__(self):
        self.id = Uuidenerate()
        self.orderat = OrderatGenerator()
        self.storeid = CsvGetId()
        self.userid = CsvGetId()
        
    def generate_data(self):
        data =["Id, OrderAt, StoreId, UserId"]

        for _ in range(Printer.input_count("order")):
            id = self.id.generate_uuid()
            orderat = self.orderat.generate_orderat()
            storeid = self.storeid.get_id("", "store_info.csv")
            userid = self.userid.get_id("", "user_info.csv")

            data.append(f'{id},{orderat},{storeid},{userid}')

        Printer.output_type(data, "order_info.csv")

class Item_generate:
    def __init__(self):
        self.id = Uuidenerate()
        self.itemdata = ItemDataGenerate()

    def generate_data(self):
        data = ["Id, Name, Type, UnitPrice"]

        for _ in range(Printer.input_count("item")):
            id = self.id.generate_uuid()
            itemdata = self.itemdata.generate_itemdata()

            data.append(f'{id},{itemdata}')
        Printer.output_type(data, "item_info.csv")

class OrderItem_generate:
    def __init__(self):
        self.id =Uuidenerate()
        self.orderid = CsvGetId()
        self.itemid = CsvGetId()

    def generate_data(self):
        data = ["Id, OrderId, ItemId"]

        for _ in range(Printer.input_count("orderitem")):
            id = self.id.generate_uuid()
            orderid = self.orderid.get_id("", "order_info.csv")
            itemid = self.itemid.get_id("", "item_info.csv")

            data.append(f'{id},{orderid},{itemid}')

        Printer.output_type(data, "orderitem_info.csv")


if __name__ == "__main__":
    human = Human_generate()
    human.generate_data()
    store = Store_generate()
    store.generate_data()
    order = Order_generate()
    order.generate_data()
    item = Item_generate()
    item.generate_data()
    orderitem = OrderItem_generate()
    orderitem.generate_data()
