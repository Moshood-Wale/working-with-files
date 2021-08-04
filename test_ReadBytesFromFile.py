from ReadBytesFromFile import ReadBytesFromFile
import unittest


class ReadBytesFromFileTest(unittest.TestCase):
        
    def test_file_opening(self):
        check=ReadBytesFromFile('filesample/text_sample.txt').file_opening()
        self.assertIsInstance(check,list)
        
    def test_iterate_files(self):
        Iterator_method=ReadBytesFromFile('filesample/text_sample.txt').iterate_files()
        self.assertEqual(next(Iterator_method),"This is just a text practice file\n")
    
    def test_read_whole_file(self):
        result=ReadBytesFromFile('filesample/text_sample.txt').read_whole_file()
        self.assertIsInstance(result,str)
        
    def test_read_first_two_lines(self): 
        testing=ReadBytesFromFile('filesample/text_sample.txt').read_first_two_lines()
        self.assertIsInstance(testing,str)
        
    def test_read_last_two_lines(self):
        testing=ReadBytesFromFile('filesample/text_sample.txt').read_last_two_lines()
        self.assertIsInstance(testing,str)
        

if __name__ == '__main__':
    unittest.main()