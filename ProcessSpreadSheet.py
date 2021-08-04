import pandas as pd
import re
from module_Interface import ModuleInterface



class ProcessSpreadSheet(ModuleInterface):

    def __init__(self, filename):
        self.filename = filename

    def file_opening(self):
        try:
            file_extension = re.split('\.', self.filename)
            if file_extension[1] == 'tsv':
                df = pd.read_csv(self.filename, sep="\t")
                return df
            elif file_extension[1] == 'csv':
                df = pd.read_csv(self.filename)
                return df
        except FileNotFoundError:
            return 'File not found or supported'

    def iterator(self):
        
        try:
            data = self.file_opening()
            iterate_data = data.iterrows()
            return iterate_data
        
        except Exception:
            return 'File not found or supported'
    
    def iterate_files(self):
        try:
            data = self.file_opening()
            for row in data.iterrows():
                print(row)
        except FileNotFoundError:
            return "File not found"
        except Exception:
            return "File not supported"
    
    def read_whole_file(self):
        try:
            data = self.file_opening()
            whole_content = data.to_string()
            return whole_content
        except FileNotFoundError:
            return "File not found"
        except Exception:
            return "File not supported"
    
    def read_first_two_lines(self):
        try:
            data = self.file_opening()
            first_two_lines = data.head(2)
            return first_two_lines
        except FileNotFoundError:
            return "File not found"
        except Exception:
            return "File not supported"
    
    def read_last_two_lines(self):
        try:
            data = self.file_opening()
            last_two_lines = data.tail(2)
            return last_two_lines
        
        except FileNotFoundError:
            return "File not found"


if __name__ == '__main__':
    
    ProcessSpreadSheet = ProcessSpreadSheet("filesample/tsv_sample.tsv")
    
    reader = ProcessSpreadSheet.file_opening()
    reader1 = ProcessSpreadSheet.read_whole_file()
    reader2 = ProcessSpreadSheet.read_first_two_lines()
    reader3 = ProcessSpreadSheet.read_last_two_lines()


    print(reader)
    # print(reader1)
    # print(reader2)
    # print(reader3)
