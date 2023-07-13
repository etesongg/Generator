from datetime import date

class AgeCale:
    @staticmethod
    def calculate_age(birthdate):
        today = date.today()

        birthdate_str = date.fromisoformat(birthdate)
        generated_age = today.year - birthdate_str.year + 1
        # print(birthdate)
        # print(generated_age)
        return birthdate, generated_age
    # main에서 매개변수 birthdate 값 처리 잘 하기(AgeCale에서return birthdate 지우기) 

