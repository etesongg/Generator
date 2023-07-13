import random
from ..functions.Load_file_data import LoadFileData


def get_id(filepath, csv_file_name):
    id = LoadFileData()
    csv_id = id.csv_load_file(filepath, csv_file_name)
    print(csv_id)
    generated_getid = random.choice(csv_id)
    # print(generated_getid)
    return generated_getid

get_id("","user_info.csv")