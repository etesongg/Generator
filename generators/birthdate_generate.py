import random

class BirthdateGenerate:
    def generate_birthdate(self):
        year = random.randint(1950, 2015)
        month = random.randint(1, 12)

        if month == 2:
            max_day = 28
        elif month in [4, 6, 9, 11]:
            max_day = 30
        else:
            max_day = 31

        day = random.randint(1, max_day)

        generated_brithdate = f'{year}-{month:02d}-{day:02d}'
        # print(generated_brithdate)
        return generated_brithdate