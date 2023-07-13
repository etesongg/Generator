import csv

class Printer:
    @staticmethod
    def input_count(make_name):
        try:
            count = int(input(f'{make_name} 데이터를 생성할 개수를 입력해주세요: '))

            if count < 0:
                raise ValueError()
            else:
                return count
        except ValueError:
            print("양수를 입력해주세요")
            count = Printer.input_count()

    @staticmethod
    def output_type(data, csv_name):
        try:
            select_type = input("출력될 결과물 타입을 입력해주세요(console, csv): ")
            if select_type == "csv":
                with open(csv_name, "w", newline='',encoding='utf-8-sig') as file:
                    csv_file = csv.writer(file)
                    for item in data:
                        fields = item.split(',')
                        csv_file.writerow(fields)  # 각 필드를 따옴표로 묶어 쓰기
                        # 줄마다 , 기준으로 나눠서 각 셀에 넣어지게 하기

                print(f'{csv_name} write done')
            elif select_type == "console":
                print(data)
            else:
                raise ValueError()
        except ValueError:
            print("console, csv 중 하나를 정확하게 입력해주세요.")
            Printer.output_type(data, csv_name)