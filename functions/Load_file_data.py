import csv

# 텍스트 파일을 읽는다.
class LoadFileData:
    def load_file(self, filepath, text_file_name):
        with open(filepath + text_file_name, 'r', encoding='utf-8-sig') as file:
            lines = file.readlines()
        
        data = []
        for line in lines:
            data.append(line.strip())
        
        return data
    
    def csv_load_file(self, filepath, csv_file_name):
        with open(filepath + csv_file_name, 'r', encoding='utf-8-sig') as file:
            lines = file.readlines()
        
        data = []
        for line in lines:
            line = line.split(',')
            data.append(line[0])

        return data
    
# a = LoadFileData("../resource/", "first_names.txt")
# a.load_file()

    
