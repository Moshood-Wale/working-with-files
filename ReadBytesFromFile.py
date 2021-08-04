
from module_Interface import ModuleInterface
import re


class ReadBytesFromFile:
    """
    This class reads bytes from files. It takes in a txt, csv and tsv file.
    """

    def __init__(self, filename):
        self.filename = filename

    def file_opening(self):

        try:
            file_extension = re.split('\.', self.filename)
            if file_extension[1] == 'txt' or file_extension[1] == 'csv' or file_extension[1] == 'tsv' :
                with open(self.filename) as file:
                    return file.readlines()
            else:
                return None
        except FileNotFoundError:
            return None
    
    def iterate_files(self):

        try:
            file_content_list = self.file_opening()
            iterator = iter(file_content_list)
            return iterator
        except:
            return("This file is not supported")
    
    def read_whole_file(self):

        try:
            opened_file = self.file_opening()
            read_all = ''
            for lines in opened_file:
                read_all += lines
            return read_all
        except:
            return("This file is not supported or found")
    
    def read_first_two_lines(self):

        try:
            listed_lines = self.file_opening()
            return f"{listed_lines[0]}{listed_lines[1]}"
        except:
            return("This file is not supported or found")
    
    def read_last_two_lines(self):

        try:
            listed_lines = self.file_opening()
            return f"{listed_lines[-2]}{listed_lines[-1]}"
        except:
            return("This file is not supported or found")


if __name__ == '__main__':
    
    
    ReadBytesFromFile = ReadBytesFromFile("filesample/tsv_sample.tsv")
    reader = ReadBytesFromFile.file_opening() 
    reader1 = ReadBytesFromFile.read_whole_file()
    reader2 = ReadBytesFromFile.read_first_two_lines()
    reader3 = ReadBytesFromFile.read_last_two_lines()


    # print(reader)
    print(reader1)
    # print(reader2)
    # print(reader3)













