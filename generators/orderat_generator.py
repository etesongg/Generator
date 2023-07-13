import random 
from datetime import datetime
import datetime

class OrderatGenerator:
    def generate_orderat(self):
        datestring = datetime.datetime.strftime(datetime.datetime( \
        2023, \
        random.randint(1, 12), \
        random.randint(1, 28), \
        random.randrange(23), \
        random.randrange(59), \
        random.randrange(59), \
        random.randrange(1000000)), '%Y-%m-%d %H:%M:%S')

        generated_orderat = datestring
        # print(generated_orderat)
        return generated_orderat