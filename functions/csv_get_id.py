import random
from functions.Load_file_data import LoadFileData

class CsvGetId:
    def get_id(self, filepath, csv_file_name):
        id = LoadFileData()
        csv_id = id.csv_load_file(filepath, csv_file_name)
        generated_getid = random.choice(csv_id[1:])
        # print(generated_getid)
        return generated_getid
        
# a = CsvGetId()
# a.get_id("../","user_info.csv")       