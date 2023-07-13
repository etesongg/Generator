import csv

# 텍스트 파일을 읽는다.
class LoadFileData:
    def __init__(self, filepath, text_file_name):
        self.filepath = filepath
        self.text_file_name = text_file_name

    def load_file(self):
        with open(self.filepath + self.text_file_name, 'r', encoding='utf8') as file:
            lines = file.readlines()
        
        data = []
        for line in lines:
            data.append(line.strip())
        return data
    
# a = LoadFileData("../resource/", "first_names.txt")
# a.load_file()

    
