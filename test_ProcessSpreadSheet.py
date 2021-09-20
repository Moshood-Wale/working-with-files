import unittest
from ProcessSpreadSheet import ProcessSpreadSheet


class ProcessSpreadsheetTest(unittest.TestCase):
        
    def test_file_opening(self):
        open_file=ProcessSpreadSheet('filesample/csv_sample.csv').file_opening()
        self.assertIsNotNone(open_file)
        
    def test_read_whole_file(self):
        read_all=ProcessSpreadSheet('filesample/csv_sample.csv').read_whole_file()
        self.assertIsInstance(read_all,str)
    
    
if __name__ == '__main__':
    unittest.main()